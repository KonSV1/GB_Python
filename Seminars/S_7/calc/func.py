import math


def calc(a, b, op):
    match op:
        case '+':
            return a+b
        case '-':
            return a-b
        case '*':
            return a*b
        case '/':
            try:
                return round(a/b, 2)
            except ZeroDivisionError:
                print('на ноль делить нельзя')
        case '**' | '^':
            return a**b
        case 'nr':
            return round(math.pow(a,1/b), 2)
        case _:
            return 'неизвестная операция'
