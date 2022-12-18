def print_phonebook():
    with open(data_csv, 'r', encoding=ENC) as d:
        while True:
            cont = d.readline()
            if not cont:
                break
            cont = cont.split(',')
            cont = list(map(str, cont))
            print((cont[0].center(20)).title(), '!'.center(1), (cont[1].center(20)).title(), '!'.center(1), cont[2].center(20).title(), '!'.center(1),\
                 cont[3].center(23).title(), '!'.center(1), cont[4].center(35).title())

# print_phonebook()

def res_operation(cont,x):
    match (x):
        case 1:
            print('\n\033[32m{}\033[0m'.format(f'Контакт "{cont[0]} {cont[4]}" успешно добавлен\n'))
        case 2:
