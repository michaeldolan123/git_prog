from random import shuffle
from xxlimited import new


suites = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10', '11']
deck_of_cards = []

for card in suites:
    for number in range(4):
        deck_of_cards.append(card)

shuffle_hand = []

how_many_decks = int(input('How many decks are you using? >'))

for card in deck_of_cards:
    for number in range(how_many_decks):
        shuffle_hand.append(card)

def stat_of_deck(deck):
    new_deck = deck
    user_points = 0
    dealer_points = 0
    no_ones_points = 0
    for user_card1 in new_deck:
        for user_card2 in new_deck:
            for dealer_card1 in new_deck:
                for dealer_card2 in new_deck:
                    if int(user_card1) + int(user_card2) == int(dealer_card1) + int(dealer_card2):
                        no_ones_points += 1
                    if int(user_card1) + int(user_card2) >= int(dealer_card1) + int(dealer_card2):
                        user_points += 1
                    if int(user_card1) + int(user_card2) <= int(dealer_card1) + int(dealer_card2):
                        dealer_points += 1
    total_points = user_points + dealer_points + no_ones_points
    






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

