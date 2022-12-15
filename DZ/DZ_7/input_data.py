

def input_data():
    x = []
    x.append(str(input('\nВведите Фамилию --> ')))
    x.append(str(input('\nВведите Имя --> ')))
    x.append(str(input('\nВведите Отчество --> ')))
    x.append(str(input('\nВведите номер телефона --> ')))
    x.append(str(input('\nДобавте описание --> ')))
    print(x)
    return (x)


def serch_contact(r):
    if r == 1:
        x = str(input('\nВведите Фамилию --> '))
    if r == 2:
        x = str(input('\nВведите номер телефона --> '))
    return x


def serch_for_del():
    x = input('Введите данные (Фамилию или Имя или Номер телефона) для поиска и  удаления контакта --> ')
    return x

