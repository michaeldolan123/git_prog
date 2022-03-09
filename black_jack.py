neglist = ['10', 'a']
poslist = ['2', '3', '4', '5', '6']

count = 0
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

card_in_deck = how_many_decks * 52

def high_low(card):
    global count
    global card_in_deck
    card_in_deck -= 1
    if card in neglist:
        count -= 1
    if card in poslist:
        count += 1
    cards = card_in_deck / 52
    final_count = count / cards
    final_count = final_count * 100
    return final_count

def mod_basic_strat(user1, user2, user_spair, dealer):
    

while True:
    dealer_1st_card = input('What is the dealers first card? >')
    for card in shuffle_hand:
        if card == dealer_1st_card:
            shuffle_hand.remove(card)
            print(high_low(dealer_1st_card))
            break

    user_first_card = input('What is your first card? >')
    for card in shuffle_hand:
        if card == user_first_card:
            shuffle_hand.remove(card)
            print(high_low(user_first_card))
            break

    user_second_card = input('What is your second card? >')
    for card in shuffle_hand:
        if card == user_second_card:
            shuffle_hand.remove(card)
            print(high_low(user_second_card))
            break
    
    if user_first_card == 'a' and user_second_card != 'a' and dealer_1st_card != 'a':



    
