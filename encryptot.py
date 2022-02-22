start = '1234567890!@#$%^&*()-=_+`~qwertyuiopasdfghjklzxcvbnm[]\;<>?,./|QWERTYUIOPASDFGHJKLZXCVBNM'
start = list(start)
print(start)
while True:
    en_or_de = input('would you like to encrypt = e or decrypt = d? >')
    if en_or_de == 'e' or en_or_de == 'd':
        break
    else:
        print('what')
while True:
    statement = input('what would you like to encrypt or decrypt? >')
    statement = list(statement)
    true = 't'
    for i in start:
        for z in statement:
            if z == i:
                true = 'f'
    if true == 'f':
        print('what')
    else:
        break
