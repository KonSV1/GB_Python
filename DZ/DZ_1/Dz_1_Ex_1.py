# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

print('Введите день недели в числовом формате.')
print('Где: Понеделльник - 1, а воскресенье - 7.')
a = int(input())
if (a == 7 or a == 6): print(f'\n- {a} -> Да')
else: print(f'\n- {a} -> Нет')
