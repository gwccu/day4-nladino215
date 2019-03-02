# File name: warmupDay4.py
from random import randint
player = input('rock (r), paper (p), or scissors (s)?')
print(player,'vs')
chosen = randint(1,3)
#print(chosen)
if chosen == 1:
    computer = 'r'
elif chosen == 2:
    computer = 'p'
else:
    computer = 's'
print(player, 'vs', end= '')
print(computer)
if player == computer:
    print('DRAW!')
elif player == 'r' and computer == 's':
    print('Computer Wins!')
elif player == 'p' and computer == 's':
    print('Computer Wins!')
elif player == 'r' and computer == 's':
    print('Player Wins!')
elif player == 's' and computer == 'p':
    print('Player Wins!')

player = input('what month is it Jan (1), Feb (2), Mar (3), Apr (4), May (5), Jun (6), Jul (7), Aug (8), Sep (9), Oct (10), Nov (11), Dec (12)?')