from random import randint


def f(x):
    return randint(0, 10)


def new_list(n: int) -> list:
    arr = [f(x) for x in range(0, n)]
    return arr



# Старый код

# import random


# def fill(arg):
#     el = 0
#     num = []
#     while el < arg:
#         a = int(random.randint(0, 9))
#         num.append(a)
#         el += 1
#     return num
