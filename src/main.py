#from PokiDoki import poker_agent

#poker_agent(num_players, number_rounds, player_one:{budget, description},player_two_desc,player_three_desc,player_four_desc)
#gradio is giving possibiliy of adding profile pictures 
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades'] for value in range(1, 14)]

    def shuffle(self):
        # Code to shuffle the deck

    def deal(self):
        # Code to deal cards

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        # Code to draw a card from the deck

    def show_hand(self):
        # Code to show the player's hand

class PokerGame:
    def __init__(self, num_players, number_rounds):
        self.num_players = num_players
        self.number_rounds = number_rounds
        self.players = [Player(f'Player {i}') for i in range(num_players)]
        self.deck = Deck()

    def start_game(self):
        # Code to start the game