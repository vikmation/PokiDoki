#init players

#create card deck 

#player set small and big blind 

#give first two cards

#betting round 

#first three cards 

#betting round 

#deal turn

#betting round 

#deal_river

#betting round 

#evaluate_hands

#end round
import random
import yaml
from poker import Suit, Rank, Card, Hand
import openai
import logging

"""logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a console handler
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

# Create a logging format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(handler)"""


class PokerGame:
    def __init__(self, players):
        #player init happens during calling class
        self.players = players
        self.player_data = {}  
        self.deck = list(Card)
        # Create a deck of cards
        self.community_cards = []
        self.pot = 0
        self.current_bet = 0

    def init_players(self):
        for player_file in self.players:
            with open(player_file, 'r') as file:
                self.player_data[player_file] = yaml.safe_load(file)

    def start_round(self):
        #start the round and load data attributes from player and give each player two cards
        self.init_players()
        for player_name, player_attributes in self.player_data.items():
            player_attributes['hand'] = [self.deck.pop(), self.deck.pop()]

    def set_blinds(self):
        # Get the players who are currently the small and big blind
        small_blind_player = next((player for player, attributes in self.player_data.items() if attributes.get('small_blind')), None)
        big_blind_player = next((player for player, attributes in self.player_data.items() if attributes.get('big_blind')), None)

        # If the small and big blind players exist, rotate them
        if small_blind_player and big_blind_player:
            # Remove the small and big blind attributes from the current players
            self.player_data[small_blind_player]['small_blind'] = False
            self.player_data[big_blind_player]['big_blind'] = False

            # Get the list of players
            players = list(self.player_data.keys())

            # Set the small blind to the player after the current big blind
            new_small_blind_player = players[(players.index(big_blind_player) + 1) % len(players)]
            self.player_data[new_small_blind_player]['small_blind'] = True

            # Set the big blind to the player after the new small blind
            new_big_blind_player = players[(players.index(new_small_blind_player) + 1) % len(players)]
            self.player_data[new_big_blind_player]['big_blind'] = True
        else:
            # If the small and big blind players don't exist, assign them randomly
            players = list(self.player_data.keys())
            random.shuffle(players)
            self.player_data[players[0]]['small_blind'] = True
            self.player_data[players[1]]['big_blind'] = True
        #print(self.player_data)

    def openai(self, prompt, temperature):
        openai.api_key = "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"
        model = "gpt-3.5-turbo"
        temperature = temperature
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=1000,
        )
        result = response.choices[0]['message']['content']
        return result

    def player_action(self, next_player, round_history, round):
        player_data = self.player_data[next_player]
        player_personality = f"""
        name: {player_data["playerName"]}
        personality description: {player_data["description"]}
        aggressiveness: {player_data["attributes"]["aggressiveness"]}
        risk tolerance: {player_data["attributes"]["riskTolerance"]}
        strategy: {player_data["attributes"]["strategy"]}
        """        
        rounds = [
            "It's pre-flop and there are no community cards on the table.",
            f"It's the flop and the community cards on the table are {self.community_cards}.",
            f"It's the turn and the community cards on the table are {self.community_cards}.",
            f"It's the river and the community cards on the table are {self.community_cards}.",
            f"It's post-river, the final betting round and the community cards on the table are {self.community_cards}."
        ]
        prompt = f"""
        You are playing a 4 player Texas No-limit Holdem poker game. You have the following personality:

        {player_personality}

        {rounds[round-1]} and your hand is {player_data["hand"]}. the history of the current round is {round_history}.

        Your decisions can be one of fold, raise or limp. Provide your decision without any explanation in the following format:
        DECISION(Raise, Fold, Limp), N BB (if placing a bet, replace N by bet amount)
        """    
        result = self.openai(prompt, 0.0)    
        return result

    def current_bet(self):
        current_bet = max(player['bet'] for player in self.player_data.values() if 'bet' in player)
        return current_bet
    
    def determine_starting_player_index_in_betting_round(self):
        big_blind_player = next((player for player, attributes in self.player_data.items() if attributes.get('big_blind')), None)
        players = list(self.player_data.keys())
        next_player = players[(players.index(big_blind_player) + 1) % len(players)]
        i = players.index(next_player)
        return i
    
    def extract_action(self, action):
        #openai response is not always clean - need to extract action appropriately
        pass

    def handle_player_action(self, player, action):
        if action == 'fold':
            self.player_data[player]['option'] = 'fold'
        elif action == 'call':
            self.player_data[player]['bet'] = self.current_bet
        elif action == 'raise':
            self.player_data[player]['bet'] = action  # Assuming action is the raised amount
            self.current_bet = action

    def skip_folded_player(self, i):
        if self.player_data[self.players[i]].get('option') == 'fold':
            i = (i + 1) % len(self.players)
        return i
    
    def check_end_of_round(self, i):
        # Check if all players have had a chance to act and all remaining players have bet the same amount
        if i == len(self.players) and all(player['bet'] == self.current_bet for player in self.player_data.values() if player.get('option') != 'fold'):
            return True
        # Check if all but one player have folded
        if sum(player.get('option') == 'fold' for player in self.player_data.values()) == len(self.players) - 1:
            return True
        return False
    
    def betting_round(self):
        #set small and big blinds
        self.set_blinds()
        #person after big blind is starting the bet 
        i = self.determine_starting_player_index_in_betting_round()
        round_history = []
        for round in range(1, 6):
            print("---ROUND {}---".format(round))
            #each round needs a while loop which runs during the total time of when the betting round is happening 
            while True:
                #if player folded already skip to next player
                i = self.skip_folded_player(i)
                #let player make an action 
                action = self.player_action(self.players[i], round_history, round)
                #function for extracting decision made by player
                action_extracted = self.extract_action(action)
                print("action extracted: {}".format(action_extracted))
                #todo need to add action and in case of raise/call specific amount also
                round_history.append({self.players[i]: action_extracted})

                self.handle_player_action(self.players[i], action_extracted)

                i = (i + 1) % len(self.players)
                # Check if all players have had a chance to act and all remaining players have bet the same amount
                if self.check_end_of_round(i):
                    break

    def deal_flop(self):
        pass 

    def deal_turn(self):
        pass

    def deal_river(self):
        pass

    def evaluate_hands(self):
        pass

    def end_round(self):
        #pot goes to winner
        pass

# Create players
#players = [Player("Alice", 1000), Player("Bob", 1000)]
#todo make this the path to the yaml file
players = ['player_one.yaml', 'player_two.yaml', 'player_three.yaml', 'player_four.yaml']
# Create game
game = PokerGame(players)
# Play a round
game.start_round()
#play one round 
game.betting_round()
#game.deal_flop()
#game.betting_round()
#game.deal_turn()
"""game.betting_round()
game.deal_river()
game.betting_round()
game.evaluate_hands()
game.end_round()"""
