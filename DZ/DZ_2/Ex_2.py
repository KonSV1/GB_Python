# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
import math

# Было
# n = int(input('Введите число:\n'))
# num = []
# el = 0
# while el < n:
#     el +=1
#     num.append(math.factorial(el))
# print(f'пусть N = {n}, тогда {num}\n')


# Стало
n = int(input('Введите число:\n'))
num = [i for i in range(1, n+1)]
num  = list(map(lambda x: math.factorial(x), num))
print(f'пусть N = {n}, тогда {num}\n')