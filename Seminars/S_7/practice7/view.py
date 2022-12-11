#ввод 2-х чисел

def input_float_namber() -> list:
    
    count = 0
    
    human_answer_namber = []
    
    while True:
        
        human_answer_string = input(f"Введите число: ")
    
        try:
            namber = float(human_answer_string)
        except ValueError:
            print("Повторите ввод")
            continue
        else:
            human_answer_namber.append(namber)
            count +=1
            if count == 2: break
        
    return human_answer_namber

#ввод знака

def input_float_znak() -> list:

    human_answer_znak = []

    while True:
        
        kortej_znakov = ("+", "-", "/", "*")

        human_answer_string = input(f"Введите знака: ")
        
        if kortej_znakov.count(human_answer_string) == 1:
            
            human_answer_znak.append(human_answer_string)
            return human_answer_znak
        else:
            print("Повторите ввод")
            continue 


def view_data(data, title):
    print(f'{title} = {data}')