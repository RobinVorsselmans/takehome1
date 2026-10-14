from takehome1.slay_the_spire.turn import Turn


class Game:
    def __init__(self, player, foe, drawpile, discardpile):
        self.player = player
        self.foe = foe
        self.drawpile = drawpile
        self.discardpile = discardpile

    def run(self):
        while self.player.health > 0 and self.foe.health > 0:
            if not self.drawpile.cards and self.discardpile.cards:
                self.discardpile.shuffle_and_add_to_drawpile(self.drawpile)

            turn = Turn(self.player, self.foe, self.drawpile, self.discardpile)
            self.player.reset_defense()
            self.player.reset_energy()
            turn.start_turn()
            print(
                f"\n{self.player.name} — HP: {self.player.health}, "
                f"Block: {self.player.defense}, Energy: {self.player.energy}"
            )
            print(
                f"{self.foe.name} — HP: {self.foe.health}, "
                f"Block: {self.foe.defense}, Attack: {self.foe.damage} damage"
            )
            print(
                f"Intent: {self.foe.name} will attack for "
                f"{self.foe.damage} damage when you end your turn."
            )

            while self.player.energy > 0 and self.player.hand.cards:
                for index, card in enumerate(self.player.hand.cards, start=1):
                    print(f"{index}. {card.name} ({card.cost} energy)")
                choice = input("Choose a card number, or 'end': ").strip().lower()
                if choice in {"end", "e"}:
                    break

                try:
                    card_index = int(choice) - 1
                except ValueError:
                    print("Choose a listed card number or enter 'end'.")
                    continue
                if not 0 <= card_index < len(self.player.hand.cards):
                    print("Choose a listed card number or enter 'end'.")
                    continue

                card = self.player.hand.cards[card_index]
                if not self.player.play_card(card, self.foe):
                    print(f"Not enough energy to play {card.name}.")
                    continue

                self.player.hand.update_after_play(card, self.discardpile)
                if card.name == "Strike":
                    print(f"You deal 6 damage to {self.foe.name}.")
                else:
                    print("You gain 5 Block.")

                if self.foe.health <= 0:
                    break

            if self.foe.health <= 0:
                break

            turn.end_turn()
            damage_taken = self.foe.attack(self.player)
            damage_blocked = self.foe.damage - damage_taken
            print(
                f"{self.foe.name} attacks for {self.foe.damage}: "
                f"{damage_blocked} blocked, {damage_taken} damage taken. "
                f"{self.player.name} has {self.player.health} HP and "
                f"{self.player.defense} Block remaining."
            )

        if self.foe.health <= 0:
            print(f"You defeated {self.foe.name}!")
        else:
            print(f"{self.player.name} was defeated.")