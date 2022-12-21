from random import randint
# import logging

def f(x):
    # logging.debug(x)
    return randint(1, 100)


def new_list(n: int) -> list:   # list creation
    arr = [f(x) for x in range(0, n)]
    # logging.debug(arr)
    return arr


def sum_nech(arr):
    num = [el for i, el in enumerate(arr) if i % 2]
    res = sum(num)
    # logging.debug(res)
    return num, res





# Старый код
# def new_list(arr: list, n: int)-> list:   # list creation
#     el = 0
#     while el < n:
#         a = int(random.randint(1, 100))
#         arr.append(a)
#         el += 1
#     return arr

# def sum_nech(arr: list)-> tuple:  # sum of elements in odd positions
#     el = 0
#     a = 0
#     num_1 = []
#     while el <= len(arr)-1:
#         if el % 2 == 0:
#             el += 1
#             continue
#         else:
#             num_1.append(arr[el])
#             a = a + arr[el]
#             el += 1
#     return num_1, a
