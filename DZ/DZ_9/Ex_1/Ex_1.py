# Задание 3:
# Создайте и зпустите программу для игры в ""Крестики-нолики"" в виртуальном окружении.

import random

line1 = ['¹','²','³']
line2 = ['⁴','⁵','⁶']
line3 = ['⁷','⁸','⁹']
print(f'\nИграем в "Крестики-нолики"')
print(*line1,sep='\t|\t')
print(*line2,sep='\t|\t')
print(*line3,sep='\t|\t')
g1, g2 = 'Игрок А', 'Игрок Б'
h = int(random.randint(0, 1))
if h == 0:
    print(f'\nПервый ход делает "{g1}"')
    i = 0
else:
    print(f'\nПервый ход делает "{g2}"')
    i = 1
count = 0
while i < 10:
    if i % 2 == 0:
        while (k := int(input(f'\n\n"{g1}" выберете цифру, чтобы поставить "X" на это место  '))) > 9:
                print('Неверно. Попробуй еще раз.\n')
        if k > 6: line3[k-10] = 'X'
        elif k > 3: line2[k-7] = 'X'
        else: line1[k-1] = 'X'
        if (line1[0] == line1[1] == line1[2] == 'X') or\
            (line2[0] == line2[1] == line2[2] == 'X') or\
                (line3[0] == line3[1] ==line3[2] =='X') or\
                    (line1[0] == line2[0] == line3[0] == 'X') or\
                        (line1[1] == line2[1] == line3[1] == 'X') or\
                            (line1[2] == line2[2] == line3[2] == 'X') or\
                                (line1[0] == line2[1] == line3[3] == 'X') or\
                                    (line1[2] == line2[1] == line3[0] == 'X'):
                                    print(*line1,sep='\t|\t')
                                    print(*line2,sep='\t|\t')
                                    print(*line3,sep='\t|\t')
                                    print('\n\nИгра окончена. Выиграл "Игрок А". Поздравляем!\n\n')
                                    break
        i +=1
        count +=1
    else:
        while (k := int(input(f'\n\n"{g2}" выберете цифру, чтобы поставить "O" на это место    '))) > 9:
                print('Неверно. Попробуй еще раз.\n')
        if k > 6: line3[k-10] = 'O'
        elif k > 3: line2[k-7] = 'O'
        else: line1[k-1] = 'O'
        if (line1[0] == line1[1] == line1[2] == 'O') or\
            (line2[0] == line2[1] == line2[2] == 'O') or\
                (line3[0] == line3[1] ==line3[2] =='O') or\
                    (line1[0] == line2[0] == line3[0] == 'O') or\
                        (line1[1] == line2[1] == line3[1] == 'O') or\
                            (line1[2] == line2[2] == line3[2] == 'O') or\
                                (line1[0] == line2[1] == line3[3] == 'O') or\
                                    (line1[2] == line2[1] == line3[0] == 'O'):
                                        print(*line1,sep='\t|\t')
                                        print(*line2,sep='\t|\t')
                                        print(*line3,sep='\t|\t')
                                        print('\n\nИгра окончена. Выиграл "Игрок Б". Поздравляем!\n\n')
                                        break
        i +=1
        count +=1
    print(*line1,sep='\t|\t')
    print(*line2,sep='\t|\t')
    print(*line3,sep='\t|\t')
