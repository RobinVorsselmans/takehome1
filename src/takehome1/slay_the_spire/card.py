class Card:
    def __init__(self, name, cost, type, target):
        self.name = name
        self.cost = cost
        self.type = type
        self.target = target

    def play(self, player, target):
        if self.name == "Strike":
            target.take_damage(6)
        elif self.name == "Defend":
            player.gain_defense(5)

    def _discard(self, discard_pile):
        discard_pile.cards.append(self)