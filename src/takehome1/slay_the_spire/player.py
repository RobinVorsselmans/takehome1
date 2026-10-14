class Player:
    def __init__(self, name, health, energy):
        self.name = name
        self.health = health
        self.energy = energy
        self.defense = 0

    def play_card(self, card, target):
        if self.energy < card.cost:
            return False

        self.energy -= card.cost
        card.play(self, target)
        return True

    def gain_health(self, amount):
        self.health += amount

    def gain_defense(self, amount):
        self.defense += amount

    def reset_defense(self):
        self.defense = 0

    def take_damage(self, amount):
        damage_taken = max(0, amount - self.defense)
        self.health -= damage_taken
        if self.health < 0:
            self.health = 0
        return damage_taken

    def reset_energy(self):
        # Reset energy at the start of the player's turn
        self.energy = 3  # Assuming the player starts with 3 energy each turn

    def draw_cards(self, drawpile):
        # Draw cards from the draw pile into the player's hand
        self.hand.draw(drawpile, 5)

    def discard_hand(self, discardpile):
        # Discard any remaining cards in the player's hand at the end of the turn
        for card in self.hand.cards:
            discardpile.cards.append(card)
        self.hand.cards.clear()

    def start_turn(self, drawpile):
        self.reset_energy()
        self.draw_cards(drawpile)

    def end_turn(self, discardpile):
        self.discard_hand(discardpile)

    def set_hand(self, hand):
        self.hand = hand

    def set_drawpile(self, drawpile):
        self.drawpile = drawpile

    def set_discardpile(self, discardpile):
        self.discardpile = discardpile

    def set_foe(self, foe):
        self.foe = foe

    def set_game(self, game):
        self.game = game

    def set_turn(self, turn):
        self.turn = turn

    def set_card_library(self, card_library):
        self.card_library = card_library

    def set_deck(self, deck):
        self.deck = deck
        