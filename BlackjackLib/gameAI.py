from BlackjackLib import game

BLACKJACK = 21
SOFT = 16

def hit(bot):
    bot.cards.append(game.the_dealer.deal_card())
    bot.value()

def decision(bot):
    while not bot.bust:
        if bot.hand_total < BLACKJACK and bot.hand_total < SOFT:
            hit(bot)
        else:
            break;

#     BLACKJACK STRATEGIES
# Always double down on a hard 11
# Split a pair of 8s & Aces
# Never split a pair of 5s and 10s
# Always hit a hard 12 vs. dealer's 2 or 3 upcard
# Hit soft 18 vs. dealer's 9, 10 or Ace upcard
# Double down on 10 vs. dealer's 9 upcard or less
# Tips on if the dealer must hit on soft 17
# Double down A-2 through A7 vs. 5 or 6 upcard
# Stand with a pair of 9s vs. a a 7 upcard
# Surrender strategy tips
# Double down on 8 vs. 5 or 6 upcard
# Strategies for low pairs
# Never make the insurance bet
# Should you stand on a hard 16?
# Don't play a 6 to 5 blackjack game

