
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
