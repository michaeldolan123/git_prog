suites = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10', 'a']
deck = []
how_many_decks = int(input('How many decks are you using')) * 4
for card in suites:
    for num in range(how_many_decks):
        deck.append(card)
print(deck)