import time
import cardvalues
from dealer import create_deck

MAX_BET = 100
MIN_BET = 1
BLACKJACK = 21

class Player:
    cards = []
    balance = 0
    hand_total  =  0
    ace_in_hand = False

    def __init__(self, cards = None, balance= 0):
        self.cards = cards
        self.balance = balance

    def has_bust(self):
        return self.hand_total > BLACKJACK
    
    # Test this against initial hand of [A][8] then draw a card that puts in over 21
    def set_ace(self):
        self.ace_in_hand = True
        if self.hand_total <= 21:
            return cardvalues.CARDS["Ace_Eleven"]
        else: 
            return cardvalues.CARDS["Ace_One"]
    
    def value(self):
        for card in self.cards:
            if card == "A":
                self.hand_total += self.set_ace()
            else:
                self.hand_total += cardvalues.CARDS[card]
        if self.has_bust():
            print("You busted!")
        print(f"Total: {self.hand_total}")
        
    def display_cards(self):
        print("\nNow lets deal your cards...\n")
        time.sleep(1)
        for card in self.cards:
            print(f"[{card}]", end= " ")
            time.sleep(.8)
        print("\n")
    
    # Need to ask user for addition deposits if balance is insufficient or user just wants to keep going****************
    def deposit(self):
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
        self.balance += amount
        
    def bet(self):
        while True:
            bet = input("\nHow much would you like to bet? $")
            if bet.isdigit():
                bet = int(bet)
                if bet > self.balance:
                    print(f"${bet} is greater than your balance of ${self.balance}")
                elif MIN_BET <= bet <= MAX_BET:
                    break
                else:
                    print(f"Your bet must be between ${MIN_BET} - ${MAX_BET}")
            else:
                print("Please enter a number...")
        self.balance -= bet

def main():
    print("\nWelcome to Blackjack!")
    player = Player()
    player.deposit()
    player.bet()
    deck = create_deck()
    deck.shuffle()
    player.cards = deck.initial_deal()
    player.display_cards()
    player.value()
    
if __name__ == "__main__":
    main()