import random

from takehome1.slay_the_spire.player import Player
from takehome1.slay_the_spire.foe import Foe
from takehome1.slay_the_spire.drawpile import DrawPile
from takehome1.slay_the_spire.discardpile import DiscardPile
from takehome1.slay_the_spire.hand import Hand
from takehome1.slay_the_spire.card import Card
from takehome1.slay_the_spire.game import Game


def main():
    print("Welcome to Slay the Spire!")
    print("This is a simplified version of the game.")
    print("You will be playing against a foe.")
    print("You will have a draw pile, a discard pile, and a hand of cards.")
    print("You will take turns playing cards from your hand to attack the foe.")
    print("The goal is to reduce the foe's health to 0 before they reduce yours to 0.")
    print("Good luck!")
    name = input("Enter your name: ").strip() or "Player"
    player = Player(name, 80, 10)
    player.set_hand(Hand())
    foe = Foe("The Guardian", 100, 10)
    cards = [
        Card(name, 1, "attack" if name == "Strike" else "skill", "foe")
        for name in ["Strike"] * 20 + ["Defend"] * 10
    ]
    random.shuffle(cards)
    drawpile = DrawPile(cards=cards)
    discardpile = DiscardPile(cards=[])
    game = Game(player, foe, drawpile, discardpile)
    game.run()
