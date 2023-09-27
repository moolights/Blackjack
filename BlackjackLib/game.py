import time
from BlackjackLib import player
from BlackjackLib import dealer
from BlackjackLib import gameAI

INIT_HAND = 2

#This can be scaled up for numerous players
def initial_deal(player, dealer_hand, dealer):
    player_cards = []
    dealer_cards = []
    for _ in range(0, INIT_HAND):
        player_cards.append(dealer.deal_card())
        dealer_cards.append(dealer.deal_card())
    player.cards = player_cards
    dealer_hand.cards = dealer_cards

def display(player, dealer):
    print("\nDealer Cards:\n")
    time.sleep(1)
    for card in dealer.cards:
        print(f"[{card}]", end= " ")
        time.sleep(.8)
    print("\n")
    dealer.value()
    dealer.show_total()

    print("\nYour cards:\n")
    time.sleep(1)
    for card in player.cards:
        print(f"[{card}]", end= " ")
        time.sleep(.8)
    print("\n")
    player.value()
    player.show_total()

# Need to code this for player**************
def hit_or_stay():
    pass
    
player_1 = player.create_player()
the_dealer = dealer.create_dealer()
dealer_hand = dealer.DealerHand()
initial_deal(player_1, dealer_hand, the_dealer)

def start():

    display(player_1, dealer_hand)
    gameAI.decision(dealer_hand)

    # while True:

    #     if dealer.hit_or_stay():
    #         player_1.cards.append(the_dealer.deal_card())
    #     player_1.display_cards()
    #     player_1.value()
        
    #     # Need to code for "stay" and the dealer hand

    #     if player_1.bust:
    #         player_1.cards.clear()
    #         if player_1.balance < 1:
    #             print(f"Balance below minimum bet. Balance: ${player_1.balance}")
    #             player_1.deposit()

    #         player_1.bet()
    #         for _ in range(0, INIT_HAND):
    #             player_1.cards.append(the_dealer.deal_card())
    #         player_1.display_cards()
    #         player_1.value()