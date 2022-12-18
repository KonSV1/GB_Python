# with open('file.txt', 'a') as data:
#     data.write('line 11\n')
#     data.write('line 21\n')


# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w')
# data.writelines(colors)
# data.writelines(f'\n{colors}') # разделителей не будет
# data.write('\nLine10\n')
# data.write('Line20\n')
# data.close()


# path = 'file.txt'
# with open('file.txt', 'r') as data:
#     for line in data:
#         print(line)


# ФУНКЦИИ

# import Lection_1 as h
# print(h.f(2.3))


# def new_string(simbol, count):
#     return simbol * count

# print(new_string('!', 50))
# print(new_string('!'))


# def new_string(simbol, count = 25):
#     return simbol * count

# print(new_string('!', 50))
# print(new_string('!'))
# print(new_string(4))

# def new_string(arg_1 = 5, arg_2):
#     return arg_1 * arg_2

# print(new_string(2))

# def concatenatio(*arg):
#     res: str = ""
#     for item in arg:
#         res += item
#     return res


# print(concatenatio('a', 's', 'd', 'w'))  # asdw
# print(concatenatio('a', '1', 'd', '2'))  # a1d2
# print(concatenatio(1, 2, 3, 4)) # TypeError: can only concatenate str (not "int") to str

# def concatenatio(*arg):
#     res =0
#     for item in arg:
#         res += item
#     return res

# print(concatenatio(1, 2, 3, 4)) # 10

# import Lection_1 as lec

# list = []
# for e in range(1, 10):
#     list.append(lec.fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34


# КОРТЕЖИ

# t = ()
# print(type(t))              # <class 'tuple'>
# t = (1,)
# print(type(t))              # <class 'tuple'>
# t = (1)
# print(type(t))              # <class 'int'>
# t = (28, 9, 1990)
# print(type(t))              # <class 'tuple'>

# colors = ['red', 'green', 'blue']
# print(colors)               # ['red', 'green', 'blue'] - Список
# print(type(colors))         # <class 'list'>
# rgb = tuple(colors)         # Преобразуем список в кортеж
# print(rgb)                  # ('red', 'green', 'blue') - Кортеж
# print(type(rgb))            # <class 'tuple'>


# t = tuple(['red', 'green', 'blue'])
# print(t[0])                         # red
# print(t[2])                         # blue
# #print(t[10])                        # IndexError: tuple index out of range
# print(t[-2])                        # green
# #print(t[-200])                      # IndexError: tuple index out of range

# for e in t:
#     print(e)                        # red green blue

# t[0] = 'black'                      # TypeError: 'tuple' object does not support  item assignmen


# t = tuple(['red', 'green', 'blue'])
# x, y, z = t
# print(t)                                # ('red', 'green', 'blue')
# print(x)                                # red
# print(y)                                # green
# print(z)                                # blue
# print(f'r:{x} g:{y} b:{z}')             # r:red g:green b:blue


# СЛОВАРИ

# dictionary = {}             # Пустой словарь
# print(type(dictionary))     # <class 'dict'>
# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }
# dic_1 = { 'f1': '164', 'f2': '165'}
# # Печать всего словаря
# print(dictionary)            # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dic_1)                 # {'f1': '164', 'f2': '165'}

# # Печать элемента словоря по ключу
# print(dictionary['left'])   # ←
# # Замена элемента
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# # Удаление элемента
# del dictionary['left']

# for item in dictionary: # for (k,v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))

# for k in dictionary.keys():
#     print(k)

# for k in dictionary.values():
#     print(k)


# МНОЖЕСТВА
# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a))  # <class 'set'>
# print(type(b))  # <class 'set'>

# # Уникальность значений
# v = {1, 1, 2, 3, 4, 2, 3, 8}
# print(v)                    # {1, 2, 3, 4, 8}


# colors = {'red', 'green', 'blue'}
# print(colors)                       # {'red', 'green', 'blue'}
# # Добавление элемента
# colors.add('red')
# print(colors)                       # {'red', 'green', 'blue'} (Такой уже есть)

# colors.add('gray')
# print(colors)                       # {'red', 'green', 'blue','gray'}
# # Удаление элемента
# colors.remove('red')
# print(colors)                       # {'green', 'blue','gray'}
# # colors.remove('red')              # KeyError: 'red'
# colors.discard('red')               # ok (не вызывает ошибку)
# print(colors)                       # {'green', 'blue','gray'}
# # Очистить множество
# colors.clear() # { }
# print(colors) # set()

# a = {1, 2, 3, 5, 8}
# print(a)
# b = {2, 5, 8, 13, 21}
# print(b)
# # Копирование множества
# c = a.copy()                        # c = {1, 2, 3, 5, 8}
# print(c)
# # Объединение множеств
# u = a.union(b)                      # u = {1, 2, 3, 5, 8, 13, 21}
# print(u)
# # Пересечение множеств
# i = a.intersection(b)               # i = {8, 2, 5}
# print(i)
# # Разность множеств
# dl = a.difference(b)                # dl = {1, 3}
# dr = b.difference(a)                # dr = {13, 21}

# q = a.union(b).difference(a.intersection(b))
# print(q)                            # {1, 21, 3, 13}
# q1 = a\
#     .union(b)\
#         .difference(a.intersection(b))
# print(q1)

# a= {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})

# list_1 = [1,3,5,7]
# list_2 = list_1
# print(f'{list_1}\n{list_2}')    # [1, 3, 5, 7]
#                                 # [1, 3, 5, 7]
# list_1[1] = 123
# print(f'{list_1}\n{list_2}')    # [1, 123, 5, 7]
#                                 # [1, 123, 5, 7]
# list_2[3] = 333
# print(f'{list_1}\n{list_2}')    # [1, 123, 5, 333]
#                                 # [1, 123, 5, 333]

# list = [1, 3, 5, 7, 9]
# print(list)                         # [1, 3, 5, 7, 9]
# # Удаление элемента [1]
# list.pop(1)
# print(list)                         # [1, 5, 7, 9]
# # Удаление Последнего элемента 
# list.pop()
# print(list)                         # [1, 5, 7]
# # Вставка элемента [1]
# list.insert(1, 3)
# print(list)                         # [1, 3, 5, 7]
# # добавление элемента в конец списка
# list.append(9)
# print(list)                         # [1, 3, 5, 7, 9]

