# 2. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 1 2 3 4 5 7 8 9


li = '1 2 3 4 5 6 8 9 10 11 12 13 14'
li = list(map(int, (li.split())))
print(li)
i=0
while i < len(li)-1:
    if li[i] != li[i+1]-1:
        print(li[i]+1)
        break
    i+=1

