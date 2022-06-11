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


answer_1 = rd.randint(0, 9)
answer_2 = rd.randint(0, 9)
answer_3 = rd.randint(0, 9)
answer_4 = rd.randint(0, 9)
while True:
    if answer_1 != answer_2 and answer_1 != answer_3 and answer_1 != answer_4 and answer_2 != answer_1 and answer_2 != answer_3 and answer_2 != answer_4 and answer_3 != answer_1 and answer_3 != answer_2 and answer_4 != answer_1 and answer_4 != answer_2 and answer_3:
        break
while True:
    answer = str(answer_1) + str(answer_2) + str(answer_3) + str(answer_4)
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
    print("命中次数:", number_of_hits, "本垒打次数:", home_run_times)
    if home_run_times == 4:
        break
