suites = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10', 'a']
deck = []
spair_deck = []

how_many_decks = int(input('How many decks are you using')) * 4
for card in suites:
    for num in range(how_many_decks):
        deck.append(card)

def odds(user1, user2, user_spair, deal1, deal_other):
    deck.remove(user1)
    deck.remove(user2)
    deck.remove(deal1)
    
    while True:

    


while True:
    user_1_card = input('what is your first card')
    user_2_card = input('what is your second card')
    dealer_1_card = input('what is the dealers first card')
    odds(user_1_card, user_2_card, 0, dealer_1_card, 0)
