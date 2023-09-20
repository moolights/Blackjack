import random
import time
import cardvalues

MAX_BET = 100
MIN_BET = 1
INIT_HAND = 2
BLACKJACK = 21
ACE_ONE = 1
ACE_ELEVEN = 11

class PlayerHand:
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

# Need function to deal cards when hitting********************

# The value of the player hand
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
    for card in player.cards:
        print(f"[{card}]", end= " ")
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
    
    print("\nLet's get started. First, let's shuffle the deck...\n")
    time.sleep(1)
    deck = shuffle(get_deck())
    
    print("\nNow lets deal your cards...\n\n")
    starting_deal = initial_deal(deck)
    temp_hand = PlayerHand(starting_deal)
    player = PlayerHand(starting_deal, balance, hand_total(temp_hand))
    display_cards(player)
    print(f"Total: {player.hand_total}")
    
    bet = get_bet(player)
    player.balance -= bet
    
    return player
    
def main():
    player = start()
    

if __name__ == "__main__":
    main()