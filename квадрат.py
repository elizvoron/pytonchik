from dotenv import dotenv_values


def rect(x):
    rectt = []
    for i in range(x):
        rectt.append('* ' * x + '\n')
    return rectt


config = dotenv_values('.env')
string_x = config['x']
x = int(string_x)
print(*rect(x))
