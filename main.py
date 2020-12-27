from Deck import Deck
from Hand import Hand

playing = True

testdeck = Deck()
testdeck.shuffle()

test_player = Hand()
pulled_card = testdeck.deal()
print(pulled_card)
test_player.add_card(pulled_card)

print(test_player.value)