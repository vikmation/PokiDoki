class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.image = self.assign_image(suit, rank)

    def assign_image(self, suit, rank):
        # Convert suit and rank to lowercase and replace spaces with underscores
        suit = suit.lower().replace(' ', '_')
        rank = rank.lower().replace(' ', '_')

        # Construct the filename
        filename = f"English_pattern_{rank}_of_{suit}.svg"

        return filename

    def __repr__(self):
        return f"{self.rank} of {self.suit}"