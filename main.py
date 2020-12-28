from Chips import Chips
from Deck import Deck
from Hand import Hand

playing = True


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How much would you like to bet?"))
        except ValueError:
            print("Please input a a valid number")
        else:
            if chips.bet > chips.total:
                print(f"Not enough chips! You have: {chips.total}$")
            else:
                break


def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_aces()


def hit_or_stand(deck, hand):
    global playing
    while True:
        letter = input("Hit or Stand? Enter h or s")
        if letter[0].lower() == "h":
            hit(deck, hand)
        elif letter[0].lower() == "s":
            print("Player Stands, Dealer's turn")
            playing = True
        else:
            print("Please enter h or s")
            continue
        break


def show_some(player, dealer):
    print("\nDealer's Hand: \n"
          f"<card hidden> \n{dealer.cards[1]}")
    print("\nPlayer's hand:", *player.cards, sep='\n')


def show_all(player, dealer):
    print("\nDealer's Hand: ", *dealer.cards, sep='\n')
    print("Dealer's Hand = ", dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep='\n')
    print("Player's Hand = ", player.value)


def player_busts(player, dealer, chips):
    print("You busted! You lost")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("You won!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer busted! You win")
    chips.lose_bet()


def dealer_wins(player, dealer, chips):
    print("You lost!")
    chips.lose_bet()


def push(player, dealer):
    print("Tied. Push")


while True:
    print("Welcome to my blackjack game!")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)
            show_all(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand)
        print(f"\nPlayer total chips are: {player_chips.total}")

        new_game = input("Play again? y/n")

        if new_game[0] == 'y':
            playing = True
            continue
        else:
            print("Tank you for playing!")
            break
