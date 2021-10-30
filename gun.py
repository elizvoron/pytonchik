from random import randint


def gun():
    a = randint(1, 6)
    if a < 5:
        return 1
    else:
        raise ValueError


n1 = 0
for i in range(300):
    try:
        vv = gun()
    except ValueError:
        vv = 0
    if vv == 1:
        n1 += 1
print(n1 / 300)
n1 = 0
for i in range(3000):
    try:
        vv = gun()
    except ValueError:
        vv = 0
    if vv == 1:
        n1 += 1
print(n1 / 3000)
n1 = 0
for i in range(30000):
    try:
        vv = gun()
    except ValueError:
        vv = 0
    if vv == 1:
        n1 += 1
print(n1 / 30000)
n1 = 0
for i in range(300000):
    try:
        vv = gun()
    except ValueError:
        vv = 0
    if vv == 1:
        n1 += 1
print(n1 / 300000)
