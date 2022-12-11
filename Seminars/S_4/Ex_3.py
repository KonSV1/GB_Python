#3. Задайте два числа. Напишите программу,
# которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

while (a := int(input('Введите А (положительное число больше 0) --->'))) <= 0:
    print('Число не отвечает критериям ввода. Попробцй еще раз')
while (b := int(input('Введите А (положительное число больше 0) --->'))) <= 0:
    print('Число не отвечает критериям ввода. Попробцй еще раз')
list_factor_a = set([i for i in range(2, a+1) if a % i == 0])
print(list_factor_a)
list_factor_b = set([i for i in range(2, b+1) if b % i == 0])
print(list_factor_b)
res =  list_factor_a.intersection(list_factor_b)
print(res)
res = min(res)
print(res)