import logging

def input_data():
    x = []
    x.append(str(input('\nВведите Фамилию --> ').strip()).lower())
    x.append(str(input('\nВведите Имя --> ').strip().lower()))
    x.append(str(input('\nВведите Отчество --> ').strip().lower()))
    x.append(str(input('\nВведите номер телефона --> ').strip().lower()))
    x.append(str(input('\nДобавте описание --> ').strip().lower()))
    logging.debug(x)
    return (x)


def serch_contact():
    x = str(input('\nВведите любые данные для поиска--> ').strip().lower())
    logging.debug(x)
    return x


def serch_for_del():
    x = input(('Введите данные для поиска и удаления контакта --> ').strip().lower())
    logging.debug(x)
    return x

