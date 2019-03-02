# file name: problemSetDay4.py
num = 2
guess = int(input('pick a number between 1-10'))
while guess != 2:
    guess = int(input('try again'))
print('good job')

strength = 5
print(strength)
while strength <= 10:
    strength += 2
    print(strength)
print('you are strong enough to advance')

n = 3
m = 2
print(n ** m)

n = 3
m = 2
while n  != 3** m:
    n *= n
    print(n)