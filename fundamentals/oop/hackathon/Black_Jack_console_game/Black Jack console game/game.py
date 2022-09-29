from classes.deck import Deck

bicycle = Deck()

bicycle.shuffle_cards()
bicycle.player1_deal()
bicycle.player1_deal()
print('Player 1 hand')
bicycle.show_cards_player1()
print('Player 1 points')
bicycle.player1points()
bicycle.player2_deal()
bicycle.player2_deal()
print('Player 2 hand')
bicycle.show_cards_player2()
print('Player 2 points')
bicycle.player2points()
#bicycle.check_tie()
bicycle.player_most_points()

# -shuffle deck
# give player 1 card 1, 2
# give player 2 card 3,4 
#     player 1 combine value of cards
#         if higher then 21 bust
#     player 2 combine value of cards
#         if higher then 21 bust

# compare player 1 vale vs player 2 value
#     if tie deal player 1, 2 another card
#     rerun compare
#     player closer to 21 wins