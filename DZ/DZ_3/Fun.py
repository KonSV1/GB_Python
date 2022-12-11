
import random
import math


def new_list(arr: list, n: int)-> list:   # list creation
    el = 0
    while el < n:
        a = int(random.randint(1, 100))
        arr.append(a)
        el += 1
    return arr


def sum_nech(arr: list)-> tuple:  # sum of elements in odd positions
    el = 0
    a = 0
    num_1 = []
    while el <= len(arr)-1:
        if el % 2 == 0:
            el += 1
            continue
        else:
            num_1.append(arr[el])
            a = a + arr[el]
            el += 1
    return num_1, a


def mult_el(arr: list)-> list:  # pairwise multiplication
    el = 0
    el_l = 0
    el_r = len(arr)-1
    num_1 = []
    while el < len(arr)/2:
        num_1.append(arr[el_l + el] * arr[el_r - el])
        el +=1
    return num_1


def dex_in_bin(n):
    leng = int(math.log2(n) + 1)
    bi = []
    el = 0
    while el < leng:
        bi.insert(el, int(n % 2))
        n = n // 2
        el += 1
    bi = ("".join(map(str,bi[::-1])))
    return bi