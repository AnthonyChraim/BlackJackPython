from Cards import *
import random


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_content = ""
        for card in self.deck:
            deck_content += "\n" + card.__str__()
        return f"The current content of the deck is: \n{deck_content}"

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()
