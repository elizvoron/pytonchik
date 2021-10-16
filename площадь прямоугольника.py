x, y = open('переменные.txt', mode='r').read().split()
wit = int(x)
hit = int(y)


def squer(wit, hit):
    return wit * hit


print(f'Площадь прямоугольника: {wit} * {hit} равна: {squer(wit, hit)}')
