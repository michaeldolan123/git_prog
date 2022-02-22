from random import shuffle


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
print(shuffle_hand)
dealer_1st_card = input('What is the dealers first card? >')
user_first_card = input('What is your first card? >')
user_second_card = input('What is your second card? >')
for card in shuffle_hand:
    if card == dealer_1st_card:
        shuffle_hand.remove(card)
        break

