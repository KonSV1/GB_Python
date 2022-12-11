# Задание 1:
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

str = 'Преданы забвению герои Зибабве.'
a = str.split()
res = list(filter(lambda i: not 'абв' in i, a))
print(str)
print (a)
print(' '.join(res))
#print (*res)               # тот же результат, что и в строке 9