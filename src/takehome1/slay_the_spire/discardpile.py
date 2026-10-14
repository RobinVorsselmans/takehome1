class DiscardPile():
    def __init__(self, cards):
        self.cards = cards

    def shuffle_and_add_to_drawpile(self, drawpile):
        # Shuffle the discard pile and add its cards to the draw pile
        import random
        random.shuffle(self.cards)
        drawpile.cards.extend(self.cards)
        self.cards.clear()