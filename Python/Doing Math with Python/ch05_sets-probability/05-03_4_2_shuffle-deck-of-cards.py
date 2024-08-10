'''
Purpose: demo the shuffle deck of 52 cards
Author: Yasen Zhao
Date: 2024/02/25
'''

import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

def initialize_deck():
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    cards = []
    for suit in suits:
        for rank in ranks:
            card = Card(suit, rank)
            cards.append(card)
            # print(card.suit, card.rank)
    return cards

def shuffle_and_print(list):
    random.shuffle(list)
    for card in list:
        print('{0} in {1}'.format(card.rank, card.suit))
    
if __name__ == '__main__':
    cards = initialize_deck()
    shuffle_and_print(cards)