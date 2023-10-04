class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
class GameEngine(metaclass=Singleton):
    def __init__(self, table):
        self.table = table

    def start_round(self):
        # Deal 2 hole cards to each player
        for player in self.table.players:
            player.hand.append(self.table.deck.deal_card())
            player.hand.append(self.table.deck.deal_card())

        # Deal the flop
        self.table.deal_community_cards(3)

    def bet_round(self):
        for player in self.table.players:
            bet = player.make_bet()
            self.table.pot += bet

    def deal_turn(self):
        self.table.deal_community_cards(1)

    def deal_river(self):
        self.table.deal_community_cards(1)

    def evaluate_hands(self):
        # This is a placeholder. You'll need to implement hand evaluation logic.
        return self.table.players[0]

    def end_round(self):
        winner = self.evaluate_hands()
        winner.chips += self.table.pot
        self.table.reset_community_cards()

    def is_game_over(self):
        # This is a placeholder. You'll need to implement game over logic.
        return False

    def reset_game(self):
        for player in self.table.players:
            player.reset_hand()
        self.table.reset_deck()

    def get_game_state(self):
        game_state = {
            "players": [player.get_state() for player in self.table.players],
            "community_cards": [str(card) for card in self.table.community_cards],
            "pot": self.table.pot,
        }
        return game_state
