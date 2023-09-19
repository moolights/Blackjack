import random
import time
import cardvalues

MAX_BET = 100
MIN_BET = 1
INIT_HAND = 2
BLACKJACK = 21

class PlayerHand:
    cards = []
    hand_total  =  0
    ace_in_hand = False

    def __init__(self, cards, hand_total= 0, ace_in_hand= False):
        self.cards = cards
        self.hand_total = hand_total

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

# Displays the shuffling deck to console using Fisher-Yates Algorithm
def shuffle(deck):
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

def initial_deal(deck):
    starting_cards = []
    for _ in range(0, INIT_HAND):
        card = random.choice(deck)
        starting_cards.append(card)
        deck.remove(card)
    return starting_cards   

# Need function to deal cards********************

# The value of the player hand when the cards are first dealt
def initial_hand_total(cards, player):
    hand_total = 0
    display_cards(player)
    for card in cards:
        if card == "A":
            player.ace_in_hand = True
            while True: # Maybe make this a function called set_ace_value************************
                choice = input("Do you want the Ace to be 1 or 11 (this can be changed later): ")
                choice = int(choice)
                if choice in (1, 11):
                    hand_total += choice
                    break
                else:
                    print("No cheating...number must be 1 or 11")
        else:
            hand_total += cardvalues.CARDS[card]
        
    return hand_total

# Need to finish function and use the ace in hand class variable***************
def get_hand_total(player):
    current_total = player.hand_total
    print(f"Current hand total: {current_total}\n\n")
    
def display_cards(player):
    for card in player.cards:
        print(f"[{card}]", end= " ")
    print("\n")
    
# Need to ask user for addition deposits if balance is insufficient or user just wants to keep going****************
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

# Need to refactor this code*********************
def start(deck):
    starting_deal = initial_deal(deck)
    temp_hand = PlayerHand(starting_deal)
    total = initial_hand_total(starting_deal, temp_hand)
    hand = PlayerHand(starting_deal, total)
    return hand
    
def main():
    print("\nWelcome to Blackjack! Let's get started. First, let's shuffle the deck...\n")
    time.sleep(1)
    deck = shuffle(get_deck())
    balance = deposit()
    bet = get_bet()
    while True:
        if bet > balance:
            print(f"${bet} is greater than your balance of ${balance}")
            bet = get_bet()
        else:
            break;
        
    print("\nNow lets deal your cards...\n\n")
    hand = start(deck)
    get_hand_total(hand)
    #

if __name__ == "__main__":
    main()