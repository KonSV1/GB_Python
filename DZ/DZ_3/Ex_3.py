# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19
import random


def new_list(arg: int) -> list:  # list creation
    el = 0
    while el < arg:
        a1 = int(random.randint(11, 14))
        a2 = int(random.randint(4, 5))
        a = float(round(a1/a2, 2))
        arr.append(a)
        el += 1
    return arr


print('\nСоздадим список состоящий из вещественных чисел')
arr = []
n = int(input('Введите количество элементов в списке: '))
new_list(n)
num = []
for el in range(n):
    num.append(round(arr[el]-int(arr[el]), 2))
print(f'{arr} => {round(max(num) - min(num), 2)}')