# Задание 3:
# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

import Fun as f


print('\nСоздадим случайную последовательность целых чисел от 0 до 9')
n = int(input('\nВведите количество элементов в последовательности: '))
s = f.fill(n)
s1 = []
print(s)
for i in range(0, n):
    for j in range(0, n):
        if s[i] == s[j] and i != j:
            if s[i]  not in s1:
                s1.append(s[i])
if s1 == []:
    print(s)
s= set(s)
s1 = set(s1)
res = s.difference(s1)
res = list(res)
print(res)