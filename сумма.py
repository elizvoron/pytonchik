def get_sum():
    n = 0
    for i in range(1, 501):
        n += i
    return n


print(f'Сумма чисел от 0 до 500 равна:{get_sum()}')