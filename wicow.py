def cow(x):
    return f"все говорят {x}, а ты возьми и купи бычка"


while True:
    a = input()
    if a == 'xxx':
        print('Конец бычку, всех купили!')
        break
    else:
        print(cow(a))
