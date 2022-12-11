import random


def fill(arg):
    el = 0
    num = []
    while el < arg:
        a = int(random.randint(0, 9))
        num.append(a)
        el += 1
    return num


def clear(str):
    x = str
    x = x.replace("+", "")
    x = x.replace(" ", "")
    x = x.replace("*", "")
    x = x.replace("(", "")
    x = x.replace(")", " ")
    x = x.replace("=", " ")
    x = x.replace("x", " ")
    x = x.split()
    return x


def prin_res(arr, k):
    mch = []
    while k >= 1:
        if k > 3:
            a = arr[len(arr) - k]
            mch.append(f'{a}*(x**{k-2}) + ')
            k-=1
        elif k == 3:
            a = arr[len(arr)-3]
            mch.append(f'{a}*x + ')
            k-=1
        elif k == 2:
            a = arr[len(arr)-2]
            mch.append(f'{a} = ')
            k-=1
        elif k == 1:
            a = arr[len(arr)-1]
            mch.append(f'{a}')
            k-=1
    return mch
