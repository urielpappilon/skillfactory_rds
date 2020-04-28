import numpy as np
import time


def simple_score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


def score_game(game_core, guess_range=(1, 101), seed=1, iterations=1000):
    """ """
    count_ls = []
    np.random.seed(seed)
    random_array = np.random.randint(guess_range[0], guess_range[1], size=iterations)
    start_time = time.perf_counter()
    for number in random_array:
        count_ls.append(game_core(number))
    end_time = time.perf_counter()
    avg_runtime = 10e3*(end_time - start_time)/iterations
    mean = np.mean(count_ls)
    min_guess = np.amax(count_ls)
    max_guess = np.amax(count_ls)
    score = round(mean/(guess_range[1]-guess_range[0]), 3)
    timing_score = round((mean+max_guess+min_guess)*avg_runtime, 3)
    print(f"Ваш алгоритм угадывает число в среднем за {mean} попыток")
    print(f"Счёт за сложность (меньше -> лучше): {score}\nСчёт за время (меньше -> лучше): {timing_score}")
    return mean
