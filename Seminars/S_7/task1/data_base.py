def write_log(log: str):
    with open('text.txt', 'w') as data:
        data.write(log)


def read_log():
    with open('text.txt', 'r') as data:
        return data.read()


def write_res(log: int):
    with open('text.txt', 'a') as data:
        data.write(f'\nresult: {log}')
