# 1. Считать строку набора чисел из файла. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел. Результат запишите в исодный файл (minn maxx).

path = 'Python/S_4/Ex_1.txt'
data = open(path, 'r')              
li = data.read()                      
data.close()
li = li.split()
li = list(map(int, li))
x = max(li)
y = min(li)
print(x, y)
data = open(path, 'a')  
data.write(f'\nMax = {x}\n')
data.write(f'Min = {y}\n')
data.close()