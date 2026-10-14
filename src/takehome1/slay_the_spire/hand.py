class Hand():
    def __init__(self):
        self.cards = []

    def draw(self, drawpile, count=5):
        for _ in range(count):
            if drawpile.cards:
                self.cards.append(drawpile.cards.pop())
            else:
                break

    def update_after_play(self, card, discardpile):
        # Remove the played card from the hand and add it to the discard pile
        if card in self.cards:
            self.cards.remove(card)
            discardpile.cards.append(card)