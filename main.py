from setup import player
from setup import dealer
from setup import cardvalues

def main():

    player_1 = player.create_player()
    the_dealer = dealer.create_dealer()
    player_1.cards = the_dealer.initial_deal()
    player_1.display_cards()
    player_1.value()
    
if __name__ == "__main__":
    main()