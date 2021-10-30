from random import randint


def gun():
    a = randint(1, 6)
    if a < 5:
        return 'ладно'
    else:
        raise ValueError


while True:
    try:
        print(gun())
    except ValueError:
        print('Доигрался...')
