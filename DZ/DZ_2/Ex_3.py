# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

n = int(input('Введите число:\n'))
num = []
sum = 0
for el in range(1, n+1):
    num.append(round(((1 + 1/el)**el), 2))
    sum = sum + float(num[el-1])
print(f'Для N = {n}: {(num)} Сумма {sum}\n')
