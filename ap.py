from random import shuffle
from xxlimited import new


suites = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10', 'a']
deck_of_cards = []

for card in suites:
    for number in range(4):
        deck_of_cards.append(card)

shuffle_hand = []

how_many_decks = int(input('How many decks are you using? >'))

for card in deck_of_cards:
    for number in range(how_many_decks):
        shuffle_hand.append(card)

def stat_of_deck(deck, deal1c, use1c, use2c):
    new_deck = deck
    user_points = 0
    dealer_points = 0
    for card in deck:
        
stat_of_deck(shuffle_hand)






#print odds
dealer_1st_card = input('What is the dealers first card? >')
for card in shuffle_hand:
    if card == dealer_1st_card:
        shuffle_hand.remove(card)
        break

user_first_card = input('What is your first card? >')
for card in shuffle_hand:
    if card == user_first_card:
        shuffle_hand.remove(card)
        break

user_second_card = input('What is your second card? >')
for card in shuffle_hand:
    if card == user_second_card:
        shuffle_hand.remove(card)
        break

while True:
    #print odds
    question = input('Did you get another card? y or n >')
    if question == 'y':
        user_n_card = input('What was that card >')
        for card in shuffle_hand:
            if card == user_n_card:
                shuffle_hand.remove(card)
                break
    else:
        break

    question = input('Did the dealer get another card? y or n >')
    if question == 'y':
        dealer_n_card = input('What was that card >')
        for card in shuffle_hand:
            if card == dealer_n_card:
                shuffle_hand.remove(card)
                break
    else:
        break

