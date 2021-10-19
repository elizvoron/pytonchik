from dotenv import dotenv_values
from random import uniform, randint


def blin(string, chance):
    gets = [', блин,', ', ну,', ', чтоб это ...,', ', твою на ..., ', ', ААА']
    if len(string) <= len(gets) / int(1 / chance):
        for i in range(0, len(string) - 1, int(1 / chance)):
            string[i] += gets[i]
    else:
        for i in range(0, len(string) - 1, int(1 / chance)):
            chan = randint(0, len(gets) - 1)
            string[i] += gets[chan]
    return ' '.join(string)


config = dotenv_values('.env')
string11 = config['text']
string1 = string11.split()
chance = uniform(0, 1)
print(chance)
print(blin(string1, chance))
