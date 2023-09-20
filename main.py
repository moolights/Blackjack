import time
import cardvalues
import dealer
from dealer import get_deck

MAX_BET = 100
MIN_BET = 1
INIT_HAND = 2
BLACKJACK = 21

class Player:
    cards = []
    balance = 0
    hand_total  =  0
    ace_in_hand = False

    def __init__(self, cards, balance= 0, hand_total= 0):
        self.cards = cards
        self.balance = balance
        self.hand_total = hand_total

    def has_bust(self):
        return self.hand_total > BLACKJACK
    
    # Test this against initial hand of [A][8] then draw a card that puts in over 21
    def set_ace(self):
        self.ace_in_hand = True
        if self.hand_total <= 21:
            return cardvalues.CARDS["Ace_Eleven"]
        else: 
            return cardvalues.CARDS["Ace_One"]

# Maybe move this and display_cards() to the player class
def hand_total(player):
    hand_total = 0
    for card in player.cards:
        if card == "A":
            hand_total += player.set_ace()
        else:
            hand_total += cardvalues.CARDS[card]
    
    if player.has_bust():
        print("You busted!")
          
    return hand_total
    
def display_cards(player):
    print("\nNow lets deal your cards...\n")
    time.sleep(1)
    for card in player.cards:
        print(f"[{card}]", end= " ")
        time.sleep(.8)
    print("\n")
    
# Need to ask user for addition deposits if balance is insufficient or user just wants to keep going****************
def deposit():
    while True:
        amount = input("\n\nHow much would you like to deposit? $")
        if amount.isdigit(): # For some reason negative values aren't registering
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than $0")
        else:
            print("Please enter a number")
            
    return amount

def get_bet(player):
    while True:
        bet = input("\nHow much would you like to bet? $")
        if bet.isdigit():
            bet = int(bet)
            if bet > player.balance:
                print(f"${bet} is greater than your balance of ${player.balance}")
            elif MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Your bet must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number...")
    
    return bet

def start():
    print("\nWelcome to Blackjack!")
    balance = deposit()
    
    deck = dealer.shuffle(get_deck())
    
    starting_deal = dealer.initial_deal(deck)
    temp_hand = Player(starting_deal)
    
    # This will change if I move hand_total and display_cards to class
    player = Player(starting_deal, balance, hand_total(temp_hand))
    
    bet = get_bet(player)
    player.balance -= bet
    
    display_cards(player)
    print(f"Total: {player.hand_total}")
    
    return player
    
def main():
    player = start()
    

if __name__ == "__main__":
    main()