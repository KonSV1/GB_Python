


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
        case _:
            return 'неизвестная операция'
