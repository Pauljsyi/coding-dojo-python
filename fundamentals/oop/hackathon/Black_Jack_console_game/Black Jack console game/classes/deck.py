from . import card
import random

class Deck:

    

    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = []
        self.player1 =[]
        self.player2 = []
        self.player1_points = 0
        self.player2_points = 0
        self.deck_spot = 0
        
        for s in suits:
            for i in range(1,14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append( card.Card( s , i , str_val ) )

    def show_cards(self):
        for card in self.cards:
            card.card_info()
        return self

    def shuffle_cards(self):
        random.shuffle(self.cards)
        return self

    def deal_cards(self, player):
        player.append(self.cards[self.deck_spot])
        if self.deck_spot == len(self.cards)-1:
            self.shuffle_cards()
            self.deck_spot = 0
        else:
            self.deck_spot += 1
        return self


    def player1_deal(self):
        self.deal_cards(self.player1)
        return self

    def player2_deal(self):
        self.deal_cards(self.player2)
        return self

    def show_single_card(self):
        cards[self.deck_spot].card_info()

    def show_cards_player1(self):
        for card in self.player1:
            card.card_info()
        return self

    def show_cards_player2(self):
        for card in self.player2:
            card.card_info()
        return self
    
    def add_point_value1(self, player_list, player_points):
        for card in player_list:
            player_points += card.point_val
        self.player1_points = player_points
        return self
    
    def add_point_value2(self, player_list, player_points):
        for card in player_list:
            player_points += card.point_val
        self.player2_points = player_points
        return self
    
    def player1points(self):
        self.add_point_value1(self.player1,self.player1_points)
        print(self.player1_points)
        return self
    
    def player2points(self):
        self.add_point_value2(self.player2, self.player2_points)
        print(self.player2_points)
        return self

    def player_most_points(self):
        if self.player1_points == self.player2_points:
            print('tie')
        elif self.player1_points > 21:
            print('Player 1 Bust')
        elif self.player2_points > 21:
            print('Player 2 Bust')
        elif self.player1_points > self.player2_points:
            print('Player 1 Wins!')
        elif self.player2_points > self.player1_points:
            print('Player 2 Wins!')
        return self

    def check_tie(self):
            if self.player1_points == self.player2_points:
                self.player1_deal
                self.player2_deal