# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной идексах.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

import Fun_2 as f

print('\nСоздадим список состоящий из целых чисел от 1 до 100')
n = int(input('Введите количество элементов в списке: '))
num = f.new_list(n)
print(f'\n{num} -> на нечетных индексах: {f.sum_nech(num)[0]} ответ: {f.sum_nech(num)[1]}\n')
