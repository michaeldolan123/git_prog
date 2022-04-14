# setting lists
suites = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10', '11']
deck = []
spair_deck = []

#making the deck of cards
how_many_decks = int(input('How many decks are you using? >')) * 4
for card in suites:
    for num in range(how_many_decks):
        deck.append(card)

#checking the odds of winning or losing
def odds(user1, user2, user_spair, deal1, deal_other):
    deck.remove(user1)
    deck.remove(user2)
    deck.remove(deal1)
    positive_odds = 0
    negative_odds = 0
    while True:
        #if user gets 21 on there draw they get a black jack and win automaticly
        if int(user1) + int(user2) == 21:
            print('good job')
            break
        for card in deck:
            #adding ever card to the hand
            if int(user1) + int(user2) + int(card) <= 21:
                positive_odds += 1
            if card == '11' and int(user1) + int(user2) + int(card) > 21:
                if int(user1) + int(user2) + 11 <= 21:
                    positive_odds += 1
            if card != '11' and int(user1) + int(user2) + int(card) > 21:
                negative_odds += 1
        sum = negative_odds + positive_odds
        print(f'you have a {negative_odds / sum * 100}% chance of busting')
        break

while True:
    user_1_card = input('what is your first card >')
    user_2_card = input('what is your second card >')
    dealer_1_card = input('what is the dealers first card >')
    odds(user_1_card, user_2_card, 0, dealer_1_card, 0)
