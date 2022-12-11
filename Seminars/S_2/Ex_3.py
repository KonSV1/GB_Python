#  Задача 3.
# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
# "Я люблю Phytom"
# "лю"
# 2


# Решение 1
# first_line = input("Введите текст: ")
# second_line = input("Введите искомое сочетание символов: ")
# print(first_line.count(second_line))


# Решение 2
first_line = "абракадабра"
second_line = "бра"
# first_line = input("Введите текст: ")
# second_line = input("Введите искомое сочетание символов: ")
count = 0
iter = 0
while iter < len(first_line):
    if second_line in first_line[0+iter: len(second_line)+iter]:
        count += 1
        iter += 1
    else:
        iter += 1
print(count)

# Решения других студентов
# cnt = 0
# while second_line in first_line:
#     first_line = first_line.replace(second_line, ' ', 1)
#     print(first_line)
#     cnt += 1
# print(cnt)

# res = first_line.split(second_line)
# print(res)
# print(len(res) - 1)