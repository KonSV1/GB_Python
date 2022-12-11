#Реализуйте алгоритм перемешивания списка.


import random

print('Создадим список состоящий из целых чисел от 1 до 100')
n = int(input('Введите количество элементов в списке: '))
r = int(input('Введите количество перемешиваний: '))
el = 0
num = []
while el <= n:
    a = int(random.randint(1, 100))
    num.append(a)
    el+=1
print(f'Исходный список\t\t {num}')
el =0
while el < r:
    if r<=0: break
    i1 = int(random.randint(0, len(num)-1))
    i2 = int(random.randint(0, len(num)-1))
    if i1 == i2: continue
    num[i1], num[i2] = num[i2],  num[i1]
    el+=1
print(f'Перемешаный список\t {num}')
