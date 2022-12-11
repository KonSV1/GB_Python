import re
import funcs
import data_base
import view


def button_click():
    (first_number, second_number) = view.input_data()
    operation = view.input_operation()
    data_base.write_log(f'{first_number} {operation} {second_number}')
    in_data = data_base.read_log()
    expression = (re.findall(r'-|/|\+|\*|[\d]+', in_data))
    if expression[1] == '+':
        view.output_data(funcs.sum(int(expression[0]), int(expression[2])))
        data_base.write_res(funcs.sum(int(expression[0]), int(expression[2])))
    elif expression[1] == '-':
        view.output_data(funcs.dif(int(expression[0]), int(expression[2])))
        data_base.write_res(funcs.dif(int(expression[0]), int(expression[2])))
    elif expression[1] == '*':
        view.output_data(funcs.mult(int(expression[0]), int(expression[2])))
        data_base.write_res(funcs.mult(int(expression[0]), int(expression[2])))
    elif expression[1] == '/':
        view.output_data(funcs.div(int(expression[0]), int(expression[2])))
        data_base.write_res(funcs.div(int(expression[0]), int(expression[2])))
