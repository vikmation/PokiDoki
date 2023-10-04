from card.deck import Deck 

class PokerTable:
    def __init__(self):
        self.community_cards = []
        self.pot = 0
        self.players = []
        self.deck = Deck()  # Create a deck instance
        self.deck.shuffle()  # Optionally shuffle the deck at the start

    # ... (other methods)

    def deal_community_cards(self, num_cards):
        for _ in range(num_cards):
            self.community_cards.append(self.deck.deal_card())

    def reset_community_cards(self):
        self.community_cards = []

    def reset_deck(self):
        self.deck = Deck()
        self.deck.shuffle()