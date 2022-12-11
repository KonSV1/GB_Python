import model_oper
import view

def button_click():
    all_value = view.input_float_namber()
    znak = view.input_float_znak()
    result = model_oper.do_it(all_value[0], all_value[1], znak[0])
    view.view_data(result, "resul")