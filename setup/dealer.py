import random
import time

INIT_HAND = 2

class Deck:
    cards = []
    
    def __init__(self, cards):
        self.cards = cards
    
    def get_cards(self):
        return self.cards
    
    def shuffle(self):
        print("\nLet's shuffle the deck...\n")
        time.sleep(1)
        n = len(self.cards)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
            print(self.cards[i], end= " ")
            time.sleep(.05)
            if i % 13 == 0:
                print("\n")
    
        print(f"\n\nTotal card count: {len(self.cards)}")
    
    def initial_deal(self):
        starting_cards = []
        for _ in range(0, INIT_HAND):
            card = random.choice(self.cards)
            starting_cards.append(card)
            self.cards.remove(card)
        return starting_cards

def create_deck():
    cards = []
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

    cards = [card for card, card_count in ranks.items() for _ in range(card_count)]
    
    deck = Deck(cards)
    return deck

# Displays the shuffling deck to console using Fisher-Yates Algorithm
# def shuffle(deck):
#     print("\nLet's get started. First, let's shuffle the deck...\n")
#     time.sleep(1)
#     n = len(deck)
#     for i in range(n - 1, 0, -1):
#         j = random.randint(0, i)
#         deck[i], deck[j] = deck[j], deck[i]
#         print(deck[i], end= " ")
#         time.sleep(.05)
#         if i % 13 == 0:
#             print("\n")
    
#     shuffled_deck = deck
#     print(f"\n\nTotal card count: {len(shuffled_deck)}")
#     return shuffled_deck

# def initial_deal(deck):
#     starting_cards = []
#     for _ in range(0, INIT_HAND):
#         card = random.choice(deck)
#         starting_cards.append(card)
#         deck.remove(card)
#     return starting_cards   

# Need function to deal cards when hitting********************

