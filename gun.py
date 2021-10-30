from random import randint


def gun():
    a = randint(1, 6)
    if a <= 5:
        return True
    else:
        return False


n1 = []
for i in range(300):
    n2 = 0
    while gun() is True:
        n2 += 1
    n1.append(n2)
print(sum(n1) / len(n1))
n1 = []
for i in range(3000):
    n2 = 0
    while gun() is True:
        n2 += 1
    n1.append(n2)
print(sum(n1) / len(n1))
n1 = []
for i in range(30000):
    n2 = 0
    while gun() is True:
        n2 += 1
    n1.append(n2)
print(sum(n1) / len(n1))
n1 = []
for i in range(300000):
    n2 = 0
    while gun() is True:
        n2 += 1
    n1.append(n2)
print(sum(n1) / len(n1))
