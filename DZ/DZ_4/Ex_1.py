# Задание 1:
# Вычислить число Пи c заданной точностью d
# Пример: - при d = 0.001, π = 3.141
# Ввод: 0.01
#     Вывод: 3.14
#     Ввод: 0.001
#     Вывод: 3.141

import math
gr = float(input('Введите точность вывода значения 𝜋. Точность ввести в формате 0,0..01: \n'))
i = 0
while gr != 1:
    i +=1
    gr = gr * 10
    print(i)
p = (math.pi)
print(round(p, i))