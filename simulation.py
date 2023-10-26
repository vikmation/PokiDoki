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
POT = 0

#lets make it again with methods only. 
def main():
    player_one, player_two, player_three, player_four = init_players()
    print(player_one)
    players = [player_one, player_two, player_three, player_four]
    blinds = set_blinds_first_round(players)
    #adjust player chips and blinds
    #need to update pot, i.e. need to update respective player values + pot
    #update_pot_and_players()
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

def adjust_player_chips(player_and_chips):
    """
    receives a list which contains player and chips to be adjusted
    """
    for item in player_and_chips:
        for chips, player in item.items():
            player['chips'] -= chips

def adjust_pot(chips):
    """
    gets a list containing chips which need to be summed
    """
    pot = sum(chips)
    
def set_blinds_first_round(players):
    random_player = get_random_player(players)
    random_player['blind'] = 'small'
    next_player = get_next_player(players, random_player)
    next_player['blind'] = 'big'
    adjust_player_chips([{SMALL_BLIND: random_player}, {BIG_BLIND: next_player}])
    adjust_pot([SMALL_BLIND, BIG_BLIND])

def set_blinds():
    #pick a random player 
    pass

