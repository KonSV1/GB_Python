# Задание 2:
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

print('\nРазложение числа на простые множители')
while (n := int(input('Введите положительное число, больше 0 --->'))) <= 0:
    print('Число не отвечает критериям ввода. Попробцй еще раз')
list_factor = []
for i in range(1, n):
    if n % i == 0:
        j = int(n / i)
        list_factor.append((i, j))
print(f'Простые множители числа {n} -> {list_factor}')