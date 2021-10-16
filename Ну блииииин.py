gets = [', блин,', ', ну,', ', чтоб это ...,', ', твою на ..., ', 'ААА!']

string = open('переменные.txt', encoding="utf-8", mode='r').read().split()
if len(string) <= len(gets):
    for i in range(len(string) - 1):
        string[i] += gets[i]
else:
    for i in range(len(gets) - 1):
        string[i] += gets[i]


print(*string)