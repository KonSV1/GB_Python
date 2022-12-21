# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной идексах.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12
__name__ = 'main'
import Fun_2 as f
import logging

ENC = 'utf-8'
FORMAT_INFO = '%(asctime)s, %(name)s, --> %(message)s'
# FORMAT_DEBUG = '%(asctime)s, %(module)s, %(filename)s, %(funcName)s, %(name)s, --> %(message)s'

logging.basicConfig(format=FORMAT_INFO, filename='DZ/DZ_6/log_info.txt',
                    filemode='a', encoding=ENC, level=logging.INFO, datefmt='%m/%d/%Y %H:%M:%S')
# logging.basicConfig(format=FORMAT_DEBUG, filename='DZ/DZ_6/log_debug.txt',
#                     filemode='a', encoding=ENC, level=logging.DEBUG, datefmt='%m/%d/%Y %H:%M:%S')

print('\nСоздадим список состоящий из целых чисел от 1 до 100')
n = int(input('Введите количество элементов в списке: '))
num = f.new_list(n)
print(
    f'\n{num} -> на нечетных индексах: {f.sum_nech(num)[0]} ответ: {f.sum_nech(num)[1]}\n')


logging.info(
    f'{num} -> на нечетных индексах: {f.sum_nech(num)[0]} ответ: {f.sum_nech(num)[1]}')
