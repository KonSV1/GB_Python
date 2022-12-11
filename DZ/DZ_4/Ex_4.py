# Задание 4:
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.
import random
import os
    
    #return res

while (k := int(input('Задайте значение степени больше "0" --->'))) <= 0:
    print('Число не отвечает критериям ввода. Попробцй еще раз')
mch = []
while k >= 0:

    match k:
        case 1:
            a = random.randint(0, 100)
            mch.append(f'{a}*x + ')
            k-=1
        case 0:
            a = random.randint(0, 100)
            mch.append(f'{a} = 0')
            k-=1
        case _:
            a = random.randint(0, 100)
            mch.append(f'{a}*(x**{k}) + ')
            k-=1
    # if k >1:
    #     a = random.randint(0, 100)
    #     mch.append(f'{a}*(x**{k}) + ')
    #     k-=1
    # if k == 1:
    #     a = random.randint(0, 100)
    #     mch.append(f'{a}*x + ')
    #     k-=1
    # if k == 0:
    #     a = random.randint(0, 100)
    #     mch.append(f'{a} = 0')
    #     k-=1

path = 'Python/DZ_4/for_ex_4.txt'
with open(path, 'w') as data:
    data.write("".join(mch))