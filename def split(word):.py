def split(word):
    return [char for char in word]

list = []
word = '0123456789'
for one in split(word):
  for two in split(word):
    for three in split(word):
      for four in split(word):
        for five in split(word):
          for six in split(word):
            print(one+two+three+four+five+six)

'''+seven+eight+nine+ten'''

'''            for seven in split(word):
              for eight in split(word):
                for nine in split(word):
                  for ten in split(word):'''