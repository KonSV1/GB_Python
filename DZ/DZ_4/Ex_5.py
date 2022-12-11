# Задание 5:
# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов (складываются числа, у которых "х" в одинаковых степенях).
# Пример того, что будет в итогвом файле: 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0

import Fun as f

path1 = 'Python/DZ_4/for_ex_5_1.txt'
path2 = 'Python/DZ_4/for_ex_5_2.txt'
path3 = 'Python/DZ_4/for_ex_5_3.txt'
with open(path1, 'r') as data:
    for l1 in data:
        data.read()
with open(path2, 'r') as data:
    for l2 in data:
        data.read()
print(l1)  
print(l2)       
# l1 = f.clear(l1)  # контрольный вывод в консоль
# l2 = f.clear(l2)  # контрольный вывод в консоль
el = (-4)
while el > (-len(l1)):
    l1.pop(el)
    el -= 1
el = (-4)
while el > (-len(l2)):
    l2.pop(el)
    el -= 1
# print(l1)   # контрольный вывод в консоль
# print(l2)   # контрольный вывод в консоль
l3 = []
el = 0
if len(l1) < len(l2):
    i = 0
    s =len(l2) - len(l1)
    while i < s:
        l1.insert(0, 0)
        i+=1
    while el < len(l1):
        l3.append(int(l1[el]) + int(l2[el]))
        el+=1
else:
    i = 0
    s =len(l1) - len(l2)
    while i < s:
        l2.insert(0, 0)
        i+=1
    while el < len(l1):
        l3.append(int(l1[el]) + int(l2[el]))
        el+=1
# print(l3)       # контрольный вывод в консоль
# print("".join(f.prin_res(l3, len(l3)))) # контрольный вывод в консоль
with open(path3, 'w') as data:
    data.write("".join(f.prin_res(l3, len(l3))))    # Запись в файл