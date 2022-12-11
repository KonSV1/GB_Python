def input_data():
    first_number = int(input('Введите первое число: '))
    second_number = int(input('Введите второе число: '))
    return first_number, second_number


def input_operation() -> str:
    operation = input('Введите операцию: ')
    return operation


def output_data(in_data: int):
    print(f'Результат равен: {in_data}')
