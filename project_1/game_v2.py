"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Угадываем рандомное число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Загаданное число находится в пределах от number_min до number_max
    number_min = 1
    number_max = 101

    count = 0

    while True:
        count += 1
        predict_number = (number_min + number_max)//2
        if predict_number > number:
            number_max = predict_number
        elif predict_number < number:
            number_min = predict_number
        else:
            break

    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов
    угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []  # список для сохранения количества попыток
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=1000)  # список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")

    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
