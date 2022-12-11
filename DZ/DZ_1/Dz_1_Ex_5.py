# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример: AB = √(xb - xa)2 + (yb - ya)2

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math


x_a = int(input('Введите координату Х точки А:  \n'))
y_a = int(input('Введите координату Y точки А:  \n'))
x_b = int(input('Введите координату Х точки B:  \n'))
y_b = int(input('Введите координату Y точки B:  \n'))
s = round(math.sqrt((x_a - x_b)**2 + (y_a - y_b)**2),2)
print(f'\n\n5А ({x_a},{y_a}); B ({x_b},{y_b}) --> {s}\n\n')
