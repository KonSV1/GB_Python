import view as v
import data_base as b
import func as f


def click_button():
    num_1 = v.input_data()
    num_2 = v.input_data()
    op = v.input_operation()
    file = b.save_data(num_1, num_2, op)
    num_1, num_2, op = b.read_data(file)
    res = f.calc(num_1, num_2, op)
    v.output_res(res, op)
