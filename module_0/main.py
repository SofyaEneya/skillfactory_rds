import numpy as np
def game_core_v1(number):
    min = 1
    max = 100
    count = 0
    number = np.random.randint(1,100)    # загадали число
    predict = np.random.randint(1,100) # предполагаемое число
    while number != predict:
        count +=1
        if number > predict:
            min = predict
            predict += (max-min)//2
        elif number < predict: 
                max=predict
                predict -= (max-min)//2
    return(count) # выход из цикла, если угадали
   
def score_game(game_core_v1):
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v1(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# запускаем
score_game(game_core_v1)   