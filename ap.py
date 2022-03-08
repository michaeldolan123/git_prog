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
    if deal1c == 'a':
        deal1c = int(input('what is the value of the dealers ace? >'))
    if use1c == 'a':
        use1c = int(input('what is the value of your ace? >'))
    if use2c == 'a':
        use2c = int(input('what is the value of your ace? >'))
    user_points = int(use1c) + int(use2c)
    user_odds = 0
    dealer_odds = 0
    for card in deck:
        if card == 'a':
            if int(deal1c) + 11 > 22 and user_points:
                dealer_odds += 1
            if int(deal1c) + 11 < user_points:
                user_odds += 1
            if int(deal1c) + 1 > user_points:
                dealer_odds += 1
            if int(deal1c) + 1 < user_points:
                user_odds += 1
        else:
            if int(deal1c) + int(card) > user_points:
                dealer_odds += 1
            if int(deal1c) + int(card) < user_points:
                user_odds += 1
            if int(deal1c) + int(card) > user_points:
                dealer_odds += 1
            if int(deal1c) + int(card) < user_points:
                user_odds += 1
    sum_of_points = user_odds + dealer_odds
    deal_odds_o_beating = dealer_odds / sum_of_points 
    deal_odds_o_beating = deal_odds_o_beating * 100
    use_odds_o_beating = user_odds / sum_of_points 
    use_odds_o_beating = use_odds_o_beating * 100

    print(f'Your cance of a win is {use_odds_o_beating}%')
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
    stat_of_deck(shuffle_hand, dealer_1st_card, user_first_card, user_second_card)
    question = input('Did you get another card? y or n >')
    if question == 'y':
        user_n_card = input('What was that card >')
        for card in shuffle_hand:
            if card == user_n_card:
                shuffle_hand.remove(card)
                break
    else:
        break
while True:
    question = input('Did the dealer get another card? y or n >')
    if question == 'y':
        dealer_n_card = input('What was that card >')
        for card in shuffle_hand:
            if card == dealer_n_card:
                shuffle_hand.remove(card)
                break
    else:
        break