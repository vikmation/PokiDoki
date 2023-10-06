"""
from engine.game_engine import GameEngine
from engine.poker_table import PokerTable
from player.player import Player

# Create poker table and players
poker_table = PokerTable()
player1 = Player("Alice", 1000)
player2 = Player("Bob", 1000)

# Add players to table
poker_table.players.append(player1)
poker_table.players.append(player2)

# Create game engine
game_engine = GameEngine(poker_table)

# Start a round
game_engine.start_round()

# Print players' hands and community cards
print(f"Alice's hand: {player1.hand}")
print(f"Bob's hand: {player2.hand}")
print(f"Community cards: {poker_table.community_cards}")
---------------------------------------------------------
agent(
    path_to_player_config_files=[
        "player_one.yaml",
        "player_two.yaml",
        "player_three.yaml",
        "player_four.yaml"
    ],
    api_key="openai_key",
    model_name="model_name",
    table_config="table_config.yaml",
    logging="true"
)
"""

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
        print(self.player_data)

    def player_bet(self, next_player):
        player_data = self.player_data[next_player]
        prompt = f"""
        You are playing a 9 player Texas No-limit Holdem poker game. You have the following personality:
        
        {player_data}
        
        You will be provided with your position at the table and the hand you’yre holding. Please
        provide your pre-flop decision.
        Assume you are the first to act and everyone before you has folded, thus
        your decisions can be one of fold, raise or limp. If you are placing a bet, please
        specify your best size in terms of big blinds.
        Provide your decision without any explanation in the following format:
        DECISION(Raise, Fold, Limp), N BB (if placing a bet, replace N by bet amount)
        """
        print(prompt)
        #parse option and than return

    def current_bet(self):
        current_bet = max(player['bet'] for player in self.player_data.values() if 'bet' in player)
        return current_bet

    def betting_round(self):
        # Start with the player after the big blind
        self.set_blinds()
        #identify player after big blind and let him make a bet 
        big_blind_player = next((player for player, attributes in self.player_data.items() if attributes.get('big_blind')), None)
        players = list(self.player_data.keys())
        next_player = players[(players.index(big_blind_player) + 1) % len(players)]
        all_bets_done = False
        # Keep track of the last player to raise (we need to keep going until we get back to them)
        #last_raiser = start_player
        # Keep going until we get back to the last player to raise
        i = next_player
        while True:
            player = self.players[i]
            if self.player_data['option'] == 'fold':
                # This player has folded, so they don't get a turn
                pass
            elif self.player_data['option'] < self.current_bet:
                action = self.player_bet(player)
                if action == 'fold':
                    self.player_data['option'] = 'fold'
                elif action == 'call':
                    self.player_data['bet'] = self.current_bet
                elif action == 'raise':
                    #raise is set to value which comes back from current bet
                    self.player_data['bet'] = action
                    #raise_amount = player.get_raise_amount(current_bet)
                    last_raiser = i
            else:
                # This player has the option to check or raise
                action = player.get_action(current_bet)
                if action == 'raise':
                    raise_amount = player.get_raise_amount(current_bet)
                    current_bet += raise_amount
                    player.chips_in_pot = current_bet
                    last_raiser = i
            # Move on to the next player
            i = (i + 1) % len(self.players)
            if i == last_raiser:
                # We've gotten back to the last player to raise, so the betting round is over
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
game.betting_round()
#game.deal_flop()
#game.betting_round()
#game.deal_turn()
"""game.betting_round()
game.deal_river()
game.betting_round()
game.evaluate_hands()
game.end_round()"""
