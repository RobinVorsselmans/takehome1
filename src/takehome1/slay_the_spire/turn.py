class Turn:
    def __init__(self, player, foe, drawpile, discardpile):
        self.player = player
        self.foe = foe
        self.drawpile = drawpile
        self.discardpile = discardpile

    def start_turn(self):
        # Draw cards for the player at the start of the turn
        self.player.draw_cards(self.drawpile)

    def end_turn(self):
        # Discard any remaining cards in the player's hand at the end of the turn
        self.player.discard_hand(self.discardpile)