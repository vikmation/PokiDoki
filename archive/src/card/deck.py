import random
from .card import Card

class Deck:
    def __init__(self):
        self.cards = self.generate_deck()

    def generate_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        return [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    def __repr__(self):
        cards = ', '.join(map(str, self.cards))
        return f"Deck with {len(self.cards)} cards: {cards}"