def input_data():
    a = input('введите число: ')
    return a


def input_operation():
    op = input('+ - сумма\n- - разность\n* - произведение\n/ - деление\n** или ^ - возведение в степень\n\
nr - вычисление корня\nвведите операцию: ')
    return op

def output_res(res, op):
    match op:
        case '+':
            print(f"sum = {res}")
        case '-':
            print(f"diff = {res}")
        case '*':
            print(f"mult = {res}")
        case '/':
            print(f"div = {res}")
        case '**' | '^':
            print(f"deg = {res}")
        case 'nr':
           print(f"nr = {res}")
        case _:
            print(res)
