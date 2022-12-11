# 3. Дан список чисел. Создайте список, в который попадают числа, 
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.
    
#     *Пример:* 
#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7] и т.д.


li = [1, 5, 2, 3, 4, 6, 1, 7]
my_li = [li[0]]

# for i in range(1, len(li)):
#     if my_li[-1] < li[i]:
#         my_li.append(li[i])
# print(my_li)

[my_li.append(li[i]) for i in range(1, len(li)) if my_li[-1] < li[i]]
print(li)
print(my_li)
