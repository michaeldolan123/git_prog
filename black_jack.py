neglist = ['10', 'a']
poslist = ['2', '3', '4', '5', '6']
card_in_deck = 312
count = 0
while True:
    card = input('card? >')
    card_in_deck -= 1
    if card in neglist:
        count -= 1
    if card in poslist:
        count += 1
    cards = card_in_deck 
    final_count = count * 52 / cards
    print(final_count * 100)
    
