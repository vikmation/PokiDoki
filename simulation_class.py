import random
import yaml
from poker import Suit, Rank, Card, Hand
from open_ai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('openai_key')

ROUNDS = [
            "It's pre-flop and there are no community cards on the table.",
            f"It's the flop and the community cards on the table are: ",
            f"It's the turn and the community cards on the table are: ",
            f"It's the river and the community cards on the table are: ",
            f"It's post-river, the final betting round and the community cards on the table are: "
        ]

VALUE_MAP = {
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

class PokerGame:
    def __init__(self):
        self.small_blind = 20
        self.big_blind = 10
        self.pot = 0
        self.deck = list(Card)
        self.players = self.init_players()
        self.model = OpenAI(key=OPENAI_API_KEY, model="gpt-4", temperature=0.0)
        self.community_cards = []
        self.history = []

    def init_players(self):
        players = ['player_one.yaml', 'player_two.yaml', 'player_three.yaml', 'player_four.yaml']
        player_data = []
        for player_file in players:
            with open(player_file, 'r') as file:
                player_data.append(yaml.safe_load(file))
        return player_data

    def get_random_player(self):
        random_player = random.choice(self.players)
        return random_player

    def get_next_player(self, random_player):
        current_index = self.players.index(random_player)
        next_index = (current_index + 1) % len(self.players)
        next_player = self.players[next_index]
        return next_player

    def adjust_player_chips(self, player_and_chips):
        for item in player_and_chips:
            for chips, player in item.items():
                player['chips'] -= chips

    def adjust_pot(self, chips):
        self.pot += sum(chips)

    def add_history(self, strings):
        for i in strings:
            self.history.append(i)

    def set_blinds_first_round(self):
        random_player = self.get_random_player()
        random_player['blind'] = 'small'
        next_player = self.get_next_player(random_player)
        next_player['blind'] = 'big'
        self.adjust_player_chips([{self.small_blind: random_player}, {self.big_blind: next_player}])
        self.adjust_pot([self.small_blind, self.big_blind])
        str_to_add_to_history_first_player= random_player['playerName'] + ": " + str(self.small_blind) + " chips small blind"
        str_to_add_to_history_second_player = next_player['playerName'] + ": " + str(self.big_blind) + " chips big blind"
        self.add_history([str_to_add_to_history_first_player, str_to_add_to_history_second_player])

    #first two cards are dealed
    def pre_flop(self):
        for player in self.players:
            # give each player two cards
            player['hand'] = random.sample(self.deck, 2)
            # remove dealt cards from the deck
            self.deck = [card for card in self.deck if card not in player['hand']]

    def get_player_after_big_blind(self):
        for player in self.players:
            if player['blind'] == 'big':
                return self.get_next_player(player)

    def get_player_personality(self, player):
        """
        generates player personality string which later can be inserted into the prompt
        """
        player_personality = (
            "Player Name: " + player['playerName'].strip() + "\n" +
            "Description: " + player['description'].strip() + "\n" +
            "Attributes: " + str(player['attributes']).strip()
        )
        return player_personality
    
    def get_player_hand(self, player):
        # Convert each card in the player's hand to its string representation
        hand_as_strings = [VALUE_MAP[str(card)] for card in player['hand']]
        # Join the strings together with a comma and a space
        hand_string = ', '.join(hand_as_strings)
        return hand_string
    
    def get_community_cards(self, round):
        #[Card('Q♦'), Card('3♦')]
        #need to convert community cards into string which is readable
        community_cards_as_strings = [VALUE_MAP[str(card)] for card in self.community_cards]
        # Join the strings together with a comma and a space
        final_community_cards_as_strings = ', '.join(community_cards_as_strings)
        return final_community_cards_as_strings
    
    def get_game_round(self, round):
        community_cards = self.get_community_cards(round)
        if round == 0:
            return ROUNDS[round]
        else:
            return ROUNDS[round] + community_cards + "."
        
    def get_history(self):
        """
        returns the history of the current poker game round 
        """
        # Join the history items together with a newline character
        history_string = "\n".join(self.history)
        return history_string

    def create_prompt(self, player, round):
        player_personality = self.get_player_personality(player)
        game_round = self.get_game_round(round)
        player_hand = self.get_player_hand(player)
        history = self.get_history()

        prompt = (
            "You are playing a 4 player Texas No-limit Holdem poker game. You have the following personality:\n\n" +
            "---\n" +
            player_personality + "\n" +
            "---\n\n" +
            game_round + " You have the following cards in your hand:\n\n" +
            "---\n" +
            player_hand + "\n" +
            "---\n\n" +
            "The history of the current round is the following:\n\n" +
            "---\n" +
            history + "\n" +
            "---\n\n" +
            "Your decisions can be one of fold, raise or limp. Provide your decision without any explanation in the following format:\n\n" +
            "DECISION(Raise, Fold, Limp), N BB (if placing a bet, replace N by bet amount)"
        )
        return prompt

    def generate_player_response(self, player, game_round):
        prompt = self.create_prompt(player, game_round)
        #need to add this to open ai - can first test to add raw string and later i am going to add the system prompt with the player personality maybe
        response = self.model.generate(prompt)
        print(response)

    def betting_pre_flop(self):
        player_after_big_blind = self.get_player_after_big_blind()
        #let player make bet 
        game_round = 0
        player_response = self.generate_player_response(player_after_big_blind, game_round)
        self.history.append(player_response)
        #need to add response to history
        
        

def main():
    #specify number of rounds which should be played 
    game = PokerGame()
    game.set_blinds_first_round()
    game.pre_flop()
    game.betting_pre_flop()
    #first round betting starts

if __name__ == "__main__":
    main()

