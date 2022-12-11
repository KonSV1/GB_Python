def save_data(a, b, op):
    file = 'cash.txt'
    with open(file, 'w') as d:
        d.writelines(f'{a}\n')
        d.writelines(f'{b}\n')
        d.writelines(op)
    return file


def read_data(file: str):
    with open(file, 'r') as d:
        a = int(d.readline())
        b = int(d.readline())
        op = d.readline()
        return a, b, op
