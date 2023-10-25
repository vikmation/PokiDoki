from poker import Suit, Rank, Card, Hand

deck = list(Card)

print(deck)

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
#deck = [value_map[str(card)] for card in deck]
cards = [Card('A♦'), Card('A♣')]
converted_cards = [value_map[str(card)] for card in cards]

print(converted_cards)

#
cards_string = ", ".join(converted_cards) + "."
