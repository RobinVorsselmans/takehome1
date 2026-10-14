class DrawPile():
    def __init__(self, cards):
        self.cards = cards

    def start_game(self, card_lib):
        # Initialize the draw pile with a set of cards from the card library
        self.cards = card_lib.get_starting_deck()