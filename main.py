from setup import player
from setup import dealer
from setup import cardvalues

INIT_HAND = 2

# This can be scaled up for numerous players
def initial_deal(player, dealer):
    initial_cards = []
    for _ in range(0, INIT_HAND):
        initial_cards.append(dealer.deal_card())
    player.cards = initial_cards
    player.display_cards()
    player.value()

def main():
   
    player_1 = player.create_player()
    the_dealer = dealer.create_dealer()
    initial_deal(player_1, the_dealer)
    
    # Need to refactor this to make it cleaner but get it working first************
    while True:

        if dealer.hit_or_stay():
            player_1.cards.append(the_dealer.deal_card())
        player_1.display_cards()
        player_1.value()
        # Need to code for "stay" and the dealer hand

        if player_1.bust:
            player_1.cards.clear()
            if player_1.balance < 1:
                print(f"Balance below minimum bet. Balance: ${player_1.balance}")
                player_1.deposit()

            player_1.bet()
            for _ in range(0, INIT_HAND):
                player_1.cards.append(the_dealer.deal_card())
            player_1.display_cards()
            player_1.value()

if __name__ == "__main__":
    main()