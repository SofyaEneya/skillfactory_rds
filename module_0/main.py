import numpy as np
def game_core_v1(number):
    min = 1
    max = 100
    count = 0
    number = np.random.randint(1,100)    # �������� �����
    predict = np.random.randint(1,100) # �������������� �����
    while number != predict:
        count +=1
        if number > predict:
            min = predict
            predict += (max-min)//2
        elif number < predict: 
                max=predict
                predict -= (max-min)//2
    return(count) # ����� �� �����, ���� �������
   
def score_game(game_core_v1):
    count_ls = []
    np.random.seed(1)  # ��������� RANDOM SEED, ����� ��� ����������� ��� �������������!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v1(number))
    score = int(np.mean(count_ls))
    print(f"��� �������� ��������� ����� � ������� �� {score} �������")
    return(score)

# ���������
score_game(game_core_v1)   