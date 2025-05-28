import random

w = ["apple", "zebra", "train"]
h = ['''
 +---+
 |   |
     |
     |
     |
     |
=======''', '''
 +---+
 |   |
 O   |
     |
     |
     |
=======''', '''
 +---+
 |   |
 O   |
 |   |
     |
     |
=======''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=======''', '''
 +---+
 |   |
 O   |
/|\\  |
     |
     |
=======''', '''
 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=======''', '''
 +---+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=======''']

word = random.choice(w)
d = ['_'] * len(word)
g = []
l = 0

while '_' in d and l < len(h)-1:
    print(h[l])
    print(' '.join(d))
    x = input("guess: ")
    if x in g:
        continue
    g.append(x)
    if x in word:
        for i in range(len(word)):
            if word[i] == x:
                d[i] = x
    else:
        l += 1

if '_' not in d:
    print("win:", word)
else:
    print(h[l])
    print("lose:", word)
