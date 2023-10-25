import json
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

value_map = {
    '2♠': 'Two of Spades',
    '2♣': 'Two of Clubs',
    '2♦': 'Two of Diamonds',
    '2♥': 'Two of Hearts',
    '3♠': 'Three of Spades',
    '3♣': 'Three of Clubs',
    '3♦': 'Three of Diamonds',
    '3♥': 'Three of Hearts',
    '4♠': 'Four of Spades',
    '4♣': 'Four of Clubs',
    '4♦': 'Four of Diamonds',
    '4♥': 'Four of Hearts',
    '5♠': 'Five of Spades',
    '5♣': 'Five of Clubs',
    '5♦': 'Five of Diamonds',
    '5♥': 'Five of Hearts',
    '6♠': 'Six of Spades',
    '6♣': 'Six of Clubs',
    '6♦': 'Six of Diamonds',
    '6♥': 'Six of Hearts',
    '7♠': 'Seven of Spades',
    '7♣': 'Seven of Clubs',
    '7♦': 'Seven of Diamonds',
    '7♥': 'Seven of Hearts',
    '8♠': 'Eight of Spades',
    '8♣': 'Eight of Clubs',
    '8♦': 'Eight of Diamonds',
    '8♥': 'Eight of Hearts',
    '9♠': 'Nine of Spades',
    '9♣': 'Nine of Clubs',
    '9♦': 'Nine of Diamonds',
    '9♥': 'Nine of Hearts',
    'T♠': 'Ten of Spades',
    'T♣': 'Ten of Clubs',
    'T♦': 'Ten of Diamonds',
    'T♥': 'Ten of Hearts',
    'J♠': 'Jack of Spades',
    'J♣': 'Jack of Clubs',
    'J♦': 'Jack of Diamonds',
    'J♥': 'Jack of Hearts',
    'Q♠': 'Queen of Spades',
    'Q♣': 'Queen of Clubs',
    'Q♦': 'Queen of Diamonds',
    'Q♥': 'Queen of Hearts',
    'K♠': 'King of Spades',
    'K♣': 'King of Clubs',
    'K♦': 'King of Diamonds',
    'K♥': 'King of Hearts',
    'A♠': 'Ace of Spades',
    'A♣': 'Ace of Clubs',
    'A♦': 'Ace of Diamonds',
    'A♥': 'Ace of Hearts'
}


import random

SMALL_BLIND = 20
BIG_BLIND = 10
#lets make it again with methods only. 
def main():
    player_one, player_two, player_three, player_four = init_players()
    print(player_one)
    players = [player_one, player_two, player_three, player_four]
    blinds = set_blinds_first_round(players)
    #adjust player chips and blinds


    #need to update pot, i.e. need to update respective player values + pot
    update_pot_and_players()
    #print(player_one)

def init_players():
    players = ['player_one.yaml', 'player_two.yaml', 'player_three.yaml', 'player_four.yaml']
    player_data = []
    for player_file in players:
        with open(player_file, 'r') as file:
            player_data.append(yaml.safe_load(file))
    return player_data

def get_random_player(players):
    random_player = random.choice(players)
    return random_player

def get_next_player(players, random_player):
    current_index = players.index(random_player)
    next_index = (current_index + 1) % len(players)
    next_player = players[next_index]
    return next_player

def adjust_player_chips():
    pass

def adjust_pot():
    pass

def set_blinds_first_round(players):
    random_player = get_random_player(players)
    random_player['blind'] = 'small'
    next_player = get_next_player(players, random_player)
    next_player['blind'] = 'big'
    adjust_player_chips()
    adjust_pot()

main()

def set_blinds():
    #pick a random player 
    pass

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
    
    def get_player_personality(self, player):
        player_personality = f"""
        name: {player["playerName"]}
        personality description: {player["description"]}
        aggressiveness: {player["attributes"]["aggressiveness"]}
        risk tolerance: {player["attributes"]["riskTolerance"]}
        strategy: {player["attributes"]["strategy"]}
        """        
        return player_personality
    
    def convert_cards_to_prompt_format(self, community_cards):
        converted_cards = [value_map[str(card)] for card in community_cards]
        return converted_cards
    
    def get_round(self, round):
        community_cards_prompt_format = self.convert_cards_to_prompt_format(self.community_cards)
        cards_string = ", ".join(community_cards_prompt_format)
        rounds = [
            "It's pre-flop and there are no community cards on the table.",
            f"It's the flop and the community cards on the table are: {cards_string}.",
            f"It's the turn and the community cards on the table are: {cards_string}.",
            f"It's the river and the community cards on the table are: {cards_string}.",
            f"It's post-river, the final betting round and the community cards on the table are: {cards_string}."
        ]
        round = rounds[round-1]
        return round
    
    def get_prompt(self, player_personality, game_round, player_data, round_history):
        """
        need to improve prompt
        1. first give personality
        2. share chipcount of other players
        3. game round with community cards
        5. history
        6. my chipcount and possible options
        """
        player_cards_prompt_format = self.convert_cards_to_prompt_format(player_data["hand"])
        prompt_one = """
        You are playing a 4 player Texas No-limit Holdem poker game. You have the following personality:

        {player_personality}

        The chip count of the other players are as follows:

        {player}: {chip_count}
        {player}: {chip_count}
        {player}: {chip_count}

        {game_round} and your hand is: {player_cards_prompt_format}. the history of the current round is {round_history}.

        
        """
        prompt = f"""
        You are playing a 4 player Texas No-limit Holdem poker game. You have the following personality:

        {player_personality}

        {game_round} and your hand is {player_data["hand"]}. the history of the current round is the following: {round_history}.

        Your decisions can be one of fold, raise or limp. Provide your decision without any explanation in the following format:
        DECISION(Raise, Fold, Limp), N BB (if placing a bet, replace N by bet amount)
        """    
        return prompt
    
    def openai_extractor(self, response):
        openai.api_key = "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"
        model = "gpt-3.5-turbo"
        temperature = 0.0
        messages = [
            {
                "role": "system",
                "content": "You will be provided with unstructured data containing an action, and in the case of a raise or call, a value for a bet. The format will be: 'DECISION(Raise, Fold, Limp), N BB (if placing a bet, replace N by bet amount)'. Your task is to parse it into JSON format."
            },
            {
                "role": "user",
                "content": "Raise, 2 BB"
            }
        ]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=100,
        )
        result = response.choices[0]['message']['content']
        return result
    
    def json_extractor(self, response):
        data = json.loads(response)
        decision = data['decision']
        bet = data['bet']
        return decision, bet

    def extract_action(self, action):
        extract_decision_openai = self.openai_extractor(action)
        decision, bet = self.json_extractor(extract_decision_openai)
        return decision, bet

    def player_action(self, next_player, round_history, round):
        player_data = self.player_data[next_player]
        player_personality = self.get_player_personality(player_data)
        game_round = self.get_round(round)
        prompt = self.get_prompt(player_personality, game_round, player_data, round_history)
        print("prompt: {}".format(prompt))
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
    
    def history_human_readable(self, round_history):
        """
        convert history looking like [{'player_one.yaml': ('Raise', '2 BB')}] to readable string format for prompt like:

        player 1 bets 2 chips
        player 2 folds
        ...

        [{'player_one.yaml': ('Raise', '2 BB')}, {'player_two.yaml': ('Raise', '2 BB')}] - whats the standard format for poker, on what was a llm most trained on?

        Poker game: Hold'em No Limit ($0.50/$1.00)

        Seat 1: PlayerA ($100 in chips)
        Seat 2: PlayerB ($100 in chips)
        Seat 3: PlayerC ($100 in chips)
        PlayerA posts small blind $0.50
        PlayerB posts big blind $1
        *** HOLE CARDS ***
        Dealt to PlayerA [Ad Kh]
        PlayerC folds
        PlayerA raises $3 to $4
        PlayerB calls $3
        *** FLOP *** [5d 7h 2c]
        PlayerA checks
        PlayerB checks
        *** TURN *** [5d 7h 2c] [9s]
        PlayerA bets $6
        PlayerB folds
        PlayerA collected $8.50 from pot
        *** SUMMARY ***
        Total pot $9 | Rake $0.50
        Board [5d 7h 2c 9s]
        Seat 1: PlayerA (small blind) showed [Ad Kh] and won ($8.50) with high card Ace
        Seat 2: PlayerB (big blind) folded on the Turn
        Seat 3: PlayerC (button) folded before Flop (didn't bet)
        """
        
        return history

    def show_options_in_prompt(self):
        """
        makes llm at the end clear how much chips you have to make clear to which value can be raised + current bet is clearly displayed
        """
        pass
    
    def betting_round(self):
        #set small and big blinds
        self.set_blinds()
        #person after big blind is starting the bet 
        i = self.determine_starting_player_index_in_betting_round()
        #add small blind and big blind to history
        round_history = []
        for round in range(1, 6):
            print("---ROUND {}---".format(round))
            #each round needs a while loop which runs during the total time of when the betting round is happening 
            while True:
                #if player folded already skip to next player
                i = self.skip_folded_player(i)
                print("player turn: {}".format(self.players[i]))
                #let player make an action 
                round_history_readable = self.history_human_readable(round_history)
                action = self.player_action(self.players[i], round_history_readable, round)
                print("action: {}".format(action))
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
#players = ['player_one.yaml', 'player_two.yaml', 'player_three.yaml', 'player_four.yaml']
# Create game
#game = PokerGame(players)
# Play a round
#game.start_round()
#play one round 
#game.betting_round()
#game.deal_flop()
#game.betting_round()
#game.deal_turn()
"""game.betting_round()
game.deal_river()
game.betting_round()
game.evaluate_hands()
game.end_round()"""
