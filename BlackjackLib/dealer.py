import random
import time
from BlackjackLib import cardvalues

INIT_HAND = 2
BLACKJACK = 21

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
    
    def deal_card(self):
        return self.cards.pop()

    def get_card_count(self):
        return len(self.cards)

# can I use inheritance on this?******************
class DealerHand:
    cards = []
    hand_total = 0
    bust = False

    def __init__(self, cards= None, hand_total= 0, bust = False):
        self.cards = cards
        self.hand_total = hand_total
        self.bust = bust

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

        if self.hand_total > BLACKJACK:
            self.bust = True
    
    def show_total(self):
        print(f"Total: {self.hand_total}")
        
def generate_deck():
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

def create_dealer():
    dealer = generate_deck()
    dealer.shuffle()
    return dealer

def hit_or_stay():
    choice = input("Hit or Stay: (H or S) ")
    return choice.upper() == 'H'
