# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

#     *Примеры:*

#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5


# Мое решение
a = int(input('Введите число:  '))
if a > 0:
    a_n = a*-1
    arr = list(range(a_n, a + 1))
else: arr = list(range(a, (a*-1) + 1))
print(f' {a} -> {arr}')

# Решения других студентов
# n = int(input("Write count n: "))
# lst = []
# for i in range(-n-1, n):
#  lst.append(i+1)
# print(f' {n} -> {lst}')
