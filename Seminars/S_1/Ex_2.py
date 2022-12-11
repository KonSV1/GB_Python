# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

#     Примеры:
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

from random import randint


num = []
for i in range(5):
    num.append(randint(-10, 10))
max_count = max(num)
print(num)
print(max_count)


# a = int(input('Введите число: '))
# b = int(input('Введите число: '))
# c = int(input('Введите число: '))
# d = int(input('Введите число: '))
# e = int(input('Введите число: '))
# max_num = a
# if b > max_num: max_num = b
# if c > max_num: max_num = c
# if d > max_num: max_num = d
# if e > max_num: max_num = e
# print(max_num)

# a, b, c, d, e = int(input('Input number: ')), int(input('Input number: ')), int(input('Input number: ')), int(input('Input number: ')), int(input('Input number: '))
# print(f'Максимальное число {max(a, b, c, d, e)}')
# print(f'Минимальное число {min(a, b, c, d, e)}')

# num = 0
# maximum = 0

# for _ in range(5):
#     num = int(input("Введите число: "))
#     if num > maximum:
#         maximum = num
# print(f' Максималное число {maximum}')
