# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['213213', 'dsf653', 'dsf', 'fdh76']
# num = 3
# Вывод: '213213', 'dsf653'

def find_num(list: list, num):
    for i in range(len(list)):
        if num in list[i]:
            print(list[i])

lst = ['213213', 'dsf653', 'dsf', 'fdh76']
num = input("Write number: ")

find_num(lst, num)


# Привести к функции
# def find_num(list: list, num: int) -> list:
#     for el in range(len(a)):
#         if num in a[el]:
#             print(a[el])


# a = ['213213', 'dsf653', 'dsf', 'fdh76']
# num = input('Введите исходное число')
# find_num(a, 3)


# def Input_list(n=int(input('введите колличество элементов: '))):
#     my_list = []
#     while n > 0:
#         my_list.append(input('введите элементы'))
#         n -= 1
#     print('\n')
#     return my_list


# def Found_in_list(list: list, n=input('введите искомое число: ')):
#     for el in list:
#         if n in el:
#             print(el)


# Found_in_list(Input_list())\
