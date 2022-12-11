# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел (time).
# import time

#def func(arg_1: int, arg_2: int=4) -> bool:   лучше так писать функции
#     return True

# def func(arg_1: int, arg_2: int=4) -> list[str | int]:
#     return ['1', 2]

# def func(a_1, a_2, *args, **kwargs):
#     return a_1, a_2, args, kwargs

# print(func(1, 2, 3, 4, 542, 124, 'wetwet', key_1=10, key_2=30))





from datetime import datetime
import time


def my_rand(start_num=1, finish_num=10):
    while True:
        num = int(round(time.time() % 1, 1) * 10)
        if start_num <= num <= finish_num:
            return num
print(my_rand())


# def get_random_number(n):
#     now = datetime.now()
#     random_number = now.time().second ** now.time().minute * now.time().microsecond
#     return random_number % 10**n


#print(get_random_number(3))
