# От 0 до 2


# n = 0
# match n:
#     case 0|1:
#         print(f'1  - {n}')
#     case 2|3:
#         print(f'2  - {n}')
#     case 4:
#         print(f'3  - {n}')
#     case _:
#         print(f'Erorr {n}')

def f(seg):
    new_list = []
    while seg:
        match seg:
            case [x, y, z, *tail] if x == y == z:
                new_list.extend(['3', x])
            case [x, y, *tail] if x == y:
                new_list.extend(['2', x])
            case [x, *tail]:
                new_list.extend(['1', x])
        seg = tail
    return new_list
    
seg = ['0']
for _ in range(15):
    seg = f(seg)
    print(''.join(seg))