# # Пример 0: Написать программу сложения двух чисел.
# Запрос двух переменных и вывод в консоль результата сложения
x = int(input('x = '))
y = int(input('y = '))
print(f'{x} + {y} = {x + y}')      # 5 + 6 = 11

# Метод принимающий на вход два аргумента и возвращающий их сумму
def sum(a, b):
 return a + b
print(sum(5, 6))                    # 11

# Использование анонимной функции Lambda
def calc(func, arg1, arg2):
    return func(arg1, arg2)

sum = (calc(lambda a, b: a + b, 5, 6))
print(sum)                          # 11