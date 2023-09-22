from setup import player
from setup import dealer
from setup import cardvalues

def main():
    print("\nWelcome to Blackjack!")
    user = player.Player()
    user.deposit()
    user.bet()
    deck = dealer.create_deck()
    deck.shuffle()
    user.cards = deck.initial_deal()
    user.display_cards()
    user.value()
    
if __name__ == "__main__":
    main()