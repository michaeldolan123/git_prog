from posixpath import split

from numpy import isin

from pyparsing import Word

abet = 'abcdefghijklmnopqrstuvwxyz0'
split_abet  = list(abet)
true = 'T'
keep_track = 0

while True:
    en_or_de = input('would you like to encrypt = e or decrypt = d? >')
    if en_or_de == 'e' or en_or_de == 'd':
        break
    else:
        print('what')

while True:
    what = list(input('what would you like to encrypt or decrypt? (only letters) >').lower())
    keep_track = -1
    for i in what:
        keep_track += 1
        if i == ' ':
            what[keep_track] = '0'
    true = 'T'
    for i in what:
        test = 0
        for z in split_abet:
            if i != z:
                test += 1
        if test == 27:
            true = 'F'
    if true == 'F':
        print('You inputed a wrong value.')
    if true == 'T':
        break

while True:
    key = input('what is the key ie: 1, 2, 3, ... 23, 24, or 25? >')
    if key.isnumeric():
        key = int(key)
        if key >= 1 and key <= 25:
            break
        else:
            print('You inputed a wrong value.')
    else:
        print('You inputed a wrong value.')

en_word = []
if en_or_de == 'e':
    for i in what:
        keep_track = 0
        for z in split_abet:
            keep_track += 1
            if i == z:
                a = keep_track + key - 1
                if a > 26:
                    a -= 27
                en_word.append(split_abet[a])

if en_or_de == 'd':
    for i in what:
        keep_track = 0
        for z in split_abet:
            keep_track += 1
            if i == z:
                a = keep_track - key - 1
                if a < 0:
                    a += 27
                en_word.append(split_abet[a])
new_word = ''
keep_track = -1
for i in en_word:
    if i == '0':
        new_word += ' '
    else:
        new_word += i

print(new_word)