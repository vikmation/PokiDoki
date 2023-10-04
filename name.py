from poker import Suit, Rank, Card, Hand
import random

# Create a deck of cards
deck = [Card(rank, suit) for suit in Suit for rank in Rank]

# Shuffle the deck
random.shuffle(deck)

# Create players
players = ['Alice', 'Bob']

# Deal two cards to each player
hands = {player: [deck.pop(), deck.pop()] for player in players}
print(hands)

# Deal the flop, turn, and river
community_cards = [deck.pop() for _ in range(5)]

# Each player's best hand is their best 5-card combination of their own cards and the community cards
best_hands = {player: Hand.max(cards + community_cards) for player, cards in hands.items()}

# The winner is the player with the best hand
winner = max(best_hands, key=best_hands.get)

print(f"The winner is {winner} with a {best_hands[winner]}")