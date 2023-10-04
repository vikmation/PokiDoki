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
