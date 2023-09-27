import time
from BlackjackLib import cardvalues

MAX_BET = 100
MIN_BET = 1
BLACKJACK = 21

class Player:
    cards = []
    balance = 0
    hand_total  =  0
    bust = False
    stay = False

    def __init__(self, cards = None, balance= 0, hand_total= 0, bust= False, stay= False):
        self.cards = cards
        self.balance = balance
        self.hand_total = hand_total
        self.bust = bust
        self.stay = stay

    def has_bust(self):
        return self.hand_total > BLACKJACK

    def value(self):
        self.bust = False
        self.hand_total = 0
        ace_count = 0
        for card in self.cards:
            if card == "A":
                ace_count += 1
            else:
                self.hand_total += cardvalues.CARDS[card]
        
        for _ in range(0, ace_count):
            if self.hand_total + cardvalues.ACE_ELEVEN <= BLACKJACK:
                    self.hand_total += cardvalues.ACE_ELEVEN
            else: 
                self.hand_total += cardvalues.ACE_ONE

        if self.has_bust():
            print("You busted!\n")
            time.sleep(1.5)
            self.bust = True
    
    def show_total(self):
        print(f"Total: {self.hand_total}")
        
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
            bet = input(f"\nHow much would you like to bet? (balance: ${self.balance}) $")
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

def create_player():
    player = Player()
    player.deposit()
    player.bet()
    return player