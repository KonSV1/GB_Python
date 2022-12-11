# Задание 4:
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


import Fun as f

my_data = 'qqqqyyeee'
print(my_data)
cod = str(f.rle_code(my_data))
print(f.rle_code(my_data))
print(f.rle_decod(cod))
