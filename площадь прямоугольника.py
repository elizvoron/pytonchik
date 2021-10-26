from dotenv import dotenv_values


config = dotenv_values('.env')
string_hit = config['hit']
hit = string_hit
string_wit = config['wit']
wit = string_wit


def squer(wit, hit):
    if not hit.isdigit():
        raise ValueError('Неверный формат высота')
    if hit.isdigit() and int(hit) <= 0:
        raise ValueError('Высота меньше 1')
    if not wit.isdigit():
        raise ValueError('Неверный формат ширины')
    if wit.isdigit() and int(hit) <= 0:
        raise ValueError('Ширина меньше 1')
    if hit.isdigit() and int(hit) > 0 and wit.isdigit() and int(wit) > 0:
        return int(wit) * int(hit)


print(f'Площадь прямоугольника: {wit} * {hit} равна: {squer(wit, hit)}')
