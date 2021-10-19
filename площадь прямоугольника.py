from dotenv import dotenv_values


config = dotenv_values('.env')
string_hit = config['hit']
hit = int(string_hit)
string_wit = config['wit']
wit = int(string_wit)


def squer(wit, hit):
    return wit * hit


print(f'Площадь прямоугольника: {wit} * {hit} равна: {squer(wit, hit)}')
