import random as rd


# 避免生成重复数字
def AGDN(avoid_duplicate_number, number):
    if number != avoid_duplicate_number:
        return number
    else:
        while True:
            generate_numbers = rd.randint(0, 9)
            if generate_numbers != avoid_duplicate_number:
                return generate_numbers

while True:
    answer_1 = rd.randint(0,9)
    answer_2 = AGDN(answer_1, rd.randint(0, 9))
    answer_3_1 = AGDN(answer_1, rd.randint(0, 9))
    answer_3_2 = AGDN(answer_2, rd.randint(0, 9))
    answer_4_1 = AGDN(answer_1, rd.randint(0, 9))
    answer_4_2 = AGDN(answer_2, rd.randint(0, 9))
    answer_4_3 = AGDN(answer_3_2, rd.randint(0, 9))
    answer = str(answer_1) + str(answer_2) + str(answer_3_2) + str(answer_4_3)
    guess_the_number = input("请猜测一个四位数:")
    # 命中检测
    number_of_hits = 0
    for i in range(4):
        for o in range(4):
            if guess_the_number[o] == answer[i]:
                number_of_hits += 1
    # 本垒打检测
    home_run_times = 0
    for i in range(4):
        if guess_the_number[i] == answer[i]:
            home_run_times += 1
    number_of_hits = number_of_hits - home_run_times
    print("命中次数:" , number_of_hits, "本垒打次数:", home_run_times)