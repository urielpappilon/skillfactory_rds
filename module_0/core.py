import numpy as np


def game_core_v1(number):
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток"""
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, 101)  # предполагаемое число
        if number == predict:
            return count  # выход из цикла, если угадали


def game_core_v2(number):
    """Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток"""
    count = 1
    predict = np.random.randint(1, 101)
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return count  # выход из цикла, если угадали


def game_core_v3(number):
    """Binary search core"""
    count = 0
    # Given that number is from 1 to 100, so the interval length is 100
    # we iterate until middle integer is not our number
    low = 1
    high = 101
    lookup_range = 100
    middle = lookup_range // 2
    while middle != number:
        # increasing attempt counter
        count += 1
        # since middle is not our number - adjusting boundaries
        if number > middle:
            low = middle + 1  # shifting lower boundary to the number is bigger than guess
        elif number < middle:
            high = middle - 1  # otherwise shifting higher boundary to the middle
        middle = (low + high) // 2  # finding new middle after adjusting boundaries
    return count

