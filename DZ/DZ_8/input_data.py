

def input_data():
    x = []
    x.append(str(input('\nВведите Фамилию --> ').strip()).lower())
    x.append(str(input('\nВведите Имя --> ').strip().lower()))
    x.append(str(input('\nВведите Отчество --> ').strip().lower()))
    x.append(str(input('\nВведите номер телефона --> ').strip().lower()))
    x.append(str(input('\nДобавте описание --> ').strip().lower()))
    print(x)
    return (x)


def serch_contact(r):
    if r == 1:
        x = str(input('\nВведите Фамилию --> ').strip().lower())
    if r == 2:
        x = str(input('\nВведите номер телефона --> '))
    return x


def serch_for_del():
    x = input(('Введите данные (Фамилию или Имя или Номер телефона) для поиска и  удаления контакта --> ').strip().lower())
    return x

