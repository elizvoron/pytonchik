from dotenv import dotenv_values


def rect(x):
    rectt = []
    if not x.isdigit():
        raise ValueError('Неверный формат длинны стороны')
    if x.isdigit() and int(x) <= 0:
        raise ValueError('Длина стороны меньше 1')
    if x.isdigit() and int(x) > 0:
        for i in range(x):
            rectt.append('*' * x + '\n')
        return rectt


config = dotenv_values('.env')
string_x = config['x']
print(*rect(string_x))
