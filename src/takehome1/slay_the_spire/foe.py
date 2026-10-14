class Foe:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = 0

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def attack(self, player):
        return player.take_damage(self.damage)

    def gain_health(self, amount):
        self.health += amount

    def gain_defense(self, amount):
        self.defense += amount