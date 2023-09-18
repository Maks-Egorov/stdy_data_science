import numpy as np

def random_predict(number:int=1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    дапазон random чисел, если загаданное число было больше,
    то диапазон начинается с random числа и до 100, если число снова
    не угадали, то диапазон random чисел снова сужаем. 
    Таким же образом в обратную сторону, если загаданное число меньше
    random числа
     
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0 # счетчик
    start_num = 1 # начало цикла
    finish_num = 101 # конец цикла

    while True:
        count += 1
        predict_number = np.random.randint(start_num, finish_num) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
        else:
            if number > predict_number:
                start_num = predict_number 
            else:
                finish_num = predict_number

    return(count)

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)