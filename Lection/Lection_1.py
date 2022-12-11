# print('Введите "а"')  # Вывод на экран фразы
# a = input()  # Считываение введенного числа и присвоение введеного значения переменной
# print('Введите "b"')  # Вывод на экран фразы
# b = input()  # Считываение введенного числа и присвоение введеного значения переменной
# print(a, b)  # Простой вывод
# print('{} -- {}'.format(a, b))  # вывод с использованием формата
# # Вывод с использованием интерполяции строки
# print(f' Число "А" = {a}, Число "B" = {b} ')


# print('Введите "а"')
# a = int(input())
# print('Введите "b"')
# b = int(input())
# c = a + b
# print(f'{a} + {b} = {c}')


# a = 1.3
# print(f' "a" -  {type(a)}')
# b = 2
# print(f' "b" -  {type(b)}')
# c = 'qwert'
# print(f' "c" -  {type(c)}')


# a = 2**3 - 10/5 + 2*3
# print(a)
# print(2**3 - 10/5 + 2*3)


# a = 7
# b = 3
# c = a/b
# print(c)
# print(round(a/b, 2)) # вычисление и округление внутри команды вывода
# c = round(a/b, 2) # Округление до 2-х знаков
# print(c)


# a = 2
# a -= 4 # a = a - 4
# print(a)


# a = 2 > 3
# print(f' выражение 2 > 3 - {a}')
# b = 3 > 2
# print(f' выражение 3 > 2 - {b}')
# c = 1 > 0 and 5 > 2
# print(f' выражение 1 > 0 and 5 > 2 - {c}')
# d = 2 == 2
# print(f' выражение 2 равно 2 - {d}')
# e = 2 != 3
# print(f' выражение 2 не равно 3 - {d}')
# f = 1 < 3 < 5
# print(f'выражение "1 меньше 3 и меньше 5" - {d}')
# a = 1 > 2 or 6 > 5
# print(a)


# a = [1, 3, 4, 7, 9, ]
# print(a)
# print(f'"3" содержится в списке? - {3 in a} ')
# print(f'"2" не содержится в списке? - {not 2 in a} ')
# print(f'"3" не содержится в списке? - {not 3 in a} ')
# c = not a[0] % 2
# print(c)
# c = not a[2] % 2
# print(c)


# username = input('Введите имя: ')
# if (username == 'Маша'):
#     print('Ура, это же МАША!')
# else:
#     print('Привет, ', username)


# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)


# a = 2359
# print(a)
# inv = 0
# while a != 0:  # Условие  пока "а" не равно "0"
#     # Определение последней цифры и добавление после нее следующей на последующей итераци
#     inv = inv * 10 + (a % 10)
#     a //= 10  # удаление последнего знака
# print(inv)


# a = 6934
# print(a)
# inv = 0
# while a != 0:
#     inv = inv * 10 + (a % 10)
#     a //= 10
# else:
#     print('разворот завершен')
# print(inv)

# a = [1, -2, 3, 14, 5]
# for _ in a:
#     print(f' квадрат числа {_} равен {_**2}, куб числа {_} равен {_**3}')


# for i in "в чащах юга":
#     print(i)


# l = ''
# for i in range(5):
#     l = ''
#     for j in range(5):
#         l += '*'
#     print(l)


# numbers = [1, 2, 3, 4, 5] # Создаем фиксированый список
# print(numbers)
# r = range(0, 10, 2)
# print(type(r))
# num = list(r)
# print(type(num))
# print(num)
# numbers = list(range(0, 10, 2))  # Создаем список с помощю range
# print(numbers)  # [0,2,4,6,8]
# numbers[0] = 10  # присвоение нулевому элементу списка значения равное 10
# print(numbers)  # [10, 2, 3, 4, 5]
# for i in numbers:
#     i *= 2
#     print(i)  # [20, 4, 6, 8, 10]
# print(numbers)  # [10, 2, 3, 4, 5]
# print(numbers*2)  # повторить дважды


# num = list(range(0, 10, 2))  # Создаем список с помощю range
# print(num)  # [0,2,4,6,8]
# num.append(39)
# print(num)  # [0, 2, 4, 6, 8, 39]
# num.remove(6)
# print(num)  # [0, 2, 4, 8, 39]


# def f(x):
#     return x**2

# print(f(5))

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)