import random
import time
import cardvalues

MAX_BET = 100
MIN_BET = 1

class PlayerHand:
    cards = []
    hand_total  =  0

    def __init__(self, cards, hand_total):
        self.cards = cards[random.choice(cardvalues), random.choice(cardvalues)]
        self.hand_total = self.card[0] + self.card[1]

    def has_bust(self):
        return self.hand_total > 21
    
    


def get_deck():
    deck = []
    ranks = {
        "A" : 4,
        "2" : 4,
        "3" : 4,
        "4" : 4,
        "5" : 4,
        "6" : 4,
        "7" : 4,
        "8" : 4,
        "9" : 4,
        "10" : 4,
        "J" : 4,
        "Q" : 4,
        "K" : 4,
    }

    # for card, card_count in ranks.items():
    #   for _ in range(card_count):
    #       deck.append(card)
    
    deck = [card for card, card_count in ranks.items() for _ in range(card_count)]
    return deck 
    
# Need to ask user for addition deposits if balance is insufficient or user just wants to keep going
def deposit():
    while True:
        amount = input("\n\nHow much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than $0")
        else:
            print("Please enter a number")
            
    return amount

def get_bet():
    while True:
        bet = input("How much would you like to bet? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Your bet must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number...")
    
    return bet

# Displays the shuffling deck to console using Fisher-Yates Algorithm
def shuffle_view(deck):
    n = len(deck)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        deck[i], deck[j] = deck[j], deck[i]
        print(deck[i], end= " ")
        time.sleep(.05)
        if i % 13 == 0:
            print("\n")
    
    shuffled_deck = deck
    print(f"\n\nTotal card count: {len(shuffled_deck)}")
    return shuffled_deck
    
# Need function to deal cards

# Need class for player hand?...

def main():
    print("\nWelcome to Blackjack! Let's get started. First, let's shuffle the deck...\n")
    time.sleep(1)
    deck = shuffle_view(get_deck())
    balance = deposit()
    bet = get_bet()
    while True:
        if bet > balance:
            print(f"${bet} is greater than your balance of ${balance}")
            bet = get_bet()
        else:
            break;
    print("\nNow lets deal your cards...\n\n")

    # call function that deals cards to user
    # call function that displays values of cards to the user

if __name__ == "__main__":
    main()