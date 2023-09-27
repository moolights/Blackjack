import time
from BlackjackLib import player
from BlackjackLib import dealer
from BlackjackLib import gameAI

INIT_HAND = 2
BLACKJACK = 21

#This can be scaled up for numerous players
def initial_deal(player, dealer_hand, dealer):
    player_cards = []
    dealer_cards = []
    for _ in range(0, INIT_HAND):
        player_cards.append(dealer.deal_card())
        dealer_cards.append(dealer.deal_card())
    player.cards = player_cards
    dealer_hand.cards = dealer_cards

#  Refactor this code to make it cleaner
def display(player, dealer):
    print("\nDealer Cards:\n")
    time.sleep(1)
    for card in dealer.cards:
        print(f"[{card}]", end= " ")
        time.sleep(.5)
    print("\n")
    dealer.value()
    dealer.show_total()

    print("\nYour cards:\n")
    time.sleep(1)
    for card in player.cards:
        print(f"[{card}]", end= " ")
        time.sleep(.5)
    print("\n")
    player.value()
    player.show_total()

# Refactor this code and it can be scaled for multiple players
def hit_or_stay():
    choice = input("Hit or Stay (H or S): ")
    if choice.upper() == 'H':
        player_1.cards.append(the_dealer.deal_card())
        player_1.value()
    else:
        player_1.stay = True
        
player_1 = player.create_player()
the_dealer = dealer.create_dealer()
dealer_hand = dealer.DealerHand()
initial_deal(player_1, dealer_hand, the_dealer)

def start():

    # Display the dealer hand/total
    # Display the player hand/total
    display(player_1, dealer_hand)

    while True:
        if dealer_hand.hand_total == BLACKJACK:
            print("Dealer has Blackjack")
            break

        hit_or_stay()
        if player_1.bust or player_1.stay:
            break
        display(player_1, dealer_hand)
       
    if player_1.bust or dealer_hand.hand_total == BLACKJACK:
        player_1.cards.clear()
        player_1.stay = False
        player_1.bust = False
        dealer_hand.cards.clear()
        if player_1.balance < 1:
            print(f"Balance below minimum bet. Balance: ${player_1.balance}")
            player_1.deposit()

        player_1.bet()
        initial_deal(player_1, dealer_hand, the_dealer)
        display(player_1, dealer_hand)
    else:
        gameAI.decision(dealer_hand)

    #  Refactor code a little
    if(dealer_hand.hand_total > player_1.hand_total and dealer_hand.hand_total <= BLACKJACK):
        print("Dealer wins!")
    elif(dealer_hand.hand_total < player_1.hand_total and player_1.hand_total <= BLACKJACK):
        print("You win, bet payout")
    else:
        print("Tie, got your bet back")