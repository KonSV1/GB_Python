# Переменной можно присвоит функцию (т.е. переменная будет хранить ссылку на функцию)
# def f(x):
#     return x**2

# g = f

# print(type(f))
# print(type(g))

# print(f(4))
# print(g(4))


# Функция в функции
# def calc(x):
#     return x + 10


# def calc1(x):
#     return x * 10


# def calc2(x):
#     return x ** 2

# def calc(func, arg):    # Функция, где в качестве перврвого аргумента выступает другая функция,
#     return func(arg)    # а в качестве второго аргумента - аргумент вызываемой функции

# print(calc(calc, 2))           # 12
# print (calc(calc1, 2))         # 20
# print(calc(calc2, 2))          # 4


# Функция  в функции с двумя аргументами
# def sum(x, y):
#     return x + y

# def mult(x, y):
#     return x * y

# def deg(x, y):
#     return x ** y

# def calc(func, arg1, arg2):    # Функция, где в качестве перврвого аргумента выступает другая функция,
#     # а в качестве остальных аргументов - аргументы вызываемой функции
#     return func(arg1, arg2)

# print(calc(sum, 10, 2))             # 12
# print(calc(mult, 10, 2))            # 20
# print(calc(deg, 10, 2))             # 100


# функия в переменной
# def sum(x, y):
#    return x + y

# def calc(func, arg1, arg2):
#     return func(arg1, arg2)
# f = sum
# print(calc(f,2,10))


# Появление лямбды
# sum = lambda x, y: x+y
# def calc(func, arg1, arg2):
#     return func(arg1, arg2)

# print(calc(sum,2,10))


# Второй шаг

# def calc(func, arg1, arg2):
#     return func(arg1, arg2)


# print(calc(lambda x, y: x+y, 2, 10))


# List Comprehension
# Создадим список состоящий из четных чисел от 1 до 50
# arr =[]
# for i in range(1, 51):
#     if (i % 2 == 0):
#         arr.append(i)
# print(arr)

# без условия
# arr =[i for i in range(1, 51)]
# print(arr)

# # Пары чисел
# arr =[(i, i) for i in range(1, 11) if i % 2 == 0]
# print(arr)
# # Число и его квадрат
# arr =[(i, i**2) for i in range(1, 11) if i % 2 == 0]
# print(arr)
# # Число, квадрат и куб
# arr =[(i, i**2, i**3) for i in range(1, 11) if i % 2 == 0]
# print(arr)

# # Использование функции для обработки элементов списка
# def f(x):
#     return x**5
# arr =[(i, f(i)) for i in range(1, 11) if i % 2 == 0]
# print(arr)


# # В файле хранятся числа, нужно выбрать четные и составить список пар (Число, квдрат числа)
# # Пример: 1 2 3 5 8 15 23 38
# # Получить: [(2, 4), (8, 64), (38, 1444)]

# f = open('Test_lec.txt', 'r')               # Получение данных из файла
# data = f.read() + ' '                       # Добавление пробела
# f.close()
# numbers = []                                # Формирование списка
# while data != '':                           # Цикл работает до пустой строки
#     space_pos = data.index(' ')             # Находим позицию первого пробела
#     numbers.append(int(data[:space_pos]))   # Взять все до первого пробела, превратить в число, добавить в список
#     data = data[space_pos+1:]               # Пропуск позиции первого пробела (далее пропуск позиций уже добавленых чисел(пробелов))
# out = []                                    # Формирование списка (из кортежей) числа и его квадрата
# for e in numbers:
#     if not e % 2:
#         out.append((e, e ** 2))
# print(out)

# # вариант с использованием lambda b LC
# def select(f, col: list) -> list:           # Принимает на вход функцию и список (набор данных])
#     return [f(x) for x in col]              # Преобразует список по "закону" функции


# def where(f, col):                          # Принимает на вход функцию и список
#     return [x for x in col if f(x)]         #Обрабатывает элементы списка по "закону" функции

# f = open('Test_lec.txt', 'r')               # Получение данных из файла
# data = f.read() + ' '                       # Добавление пробела
# f.close()
# data = data.split()                         # ['1', '2', '3', '5', '8', '15', '23', '38']
# data = select(int, data)                    # [1, 2, 3, 5, 8, 15, 23, 38]
# data = where(lambda e: not e % 2, data)     #[ 2, 8, 38]
# data = list(select(lambda e: (e, e**2), data))
# print(data)                                 # [(2, 4), (8, 64), (38, 1444)]


# Функция MAP
# li =[i for i in range(1, 11)]
# print(li)
# li =  list(map(lambda x: x+10, li))
# print(li)

# li = list(map(int, '1 2 3 55'.split()))
# for i in li:
#     print(i)
# print("----")
# for i in li:
#     print(i)


# вариант с использованием функции MAP

# def where(f, col):                          # Принимает на вход функцию и список
#     return [x for x in col if f(x)]         #Обрабатывает элементы списка по "закону" функции

# f = open('Test_lec.txt', 'r')
# data = f.read() + ' '
# f.close()
# data = data.split()
# data = map(int, data)
# print(type(data))                           # <class 'map'>
# data = where(lambda e: not e % 2, data)
# print(type(data))                           # <class 'list'>
# data = list(map(lambda e: (e, e**2), data))
# print(data)                                 # [(2, 4), (8, 64), (38, 1444)]


# Функция FILTER
# li = [i for i in range(21)]
# print(li)           # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# li  = list(filter(lambda i: not i % 2, li))
# print(li)           # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# вариант решения с использованием функций MAP и FILTER
# f = open('Test_lec.txt', 'r')
# data = f.read() + ' '
# f.close()
# data = data.split()
# data = map(int, data)
# data = filter(lambda e: not e % 2, data)
# data = list(map(lambda e: (e, e**2), data))
# print(data)                                 # [(2, 4), (8, 64), (38, 1444)]

# Функция ZIP
users = ['user1', 'user2', 'user3', 'user4']
id = [111, 222, 333, 444]
zp = [10000, 15000, 14500]

# li = list(zip(users, id, zp))
# print(li)                # [('user1', 111, 10000), ('user2', 222, 15000), ('user3', 333, 14500)]

# li = list(zip(users, id))
# print(li)               # [('user1', 111), ('user2', 222), ('user3', 333), ('user4', 444)]  

#Функция enumerate

li = list(enumerate(users, 1))
print(li)               #[(1, 'user1'), (2, 'user2'), (3, 'user3'), (4, 'user4')] 

# path = 'Test_lec.txt'
# data = open(path, 'r')
# str = data.read()
# data.close()
# num = (list(map(int, str.split())))
# print(num)
# out = []
# for i in num:
#     if not i % 2:
#         out.append((i, i ** 2))
# print(out)
# pr int(type(out))
