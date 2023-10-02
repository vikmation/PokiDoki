class Deck:
    def __init__(self):
        self.cards = self.generate_deck()

    @staticmethod
    def generate_deck():
        """
        Generate a list of 52 cards.
        Each card is a tuple with two elements:
        - The first element is the rank (2-10, J, Q, K, A)
        - The second element is the suit (hearts, diamonds, clubs, spades)
        """
        ranks = [str(n) for n in range(2, 11)] + list('JQKA')
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        deck = [(rank, suit) for rank in ranks for suit in suits]
        return deck

    def shuffle(self):
        """
        Shuffle the deck in place.
        """
        import random
        random.shuffle(self.cards)

    def deal(self, num_cards):
        """
        Deal num_cards from the deck.
        Remove the dealt cards from the deck.
        """
        dealt_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return dealt_cards