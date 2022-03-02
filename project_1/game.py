"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


# Загаданное число находится в пределах от number_min до number_max
number_min = 1
number_max = 101
number = np.random.randint(number_min, number_max)
# Количество попыток
count = 0

while True:
    count += 1
    predict_number = (number_min + number_max)//2
    if predict_number > number:
        number_max = predict_number
    elif predict_number < number:
        number_min = predict_number
    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break
