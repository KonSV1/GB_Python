import os



ENC = 'utf-8'
data_csv = 'DZ/DZ_8/phonebook.csv'
data_json = 'DZ/DZ_8/phonebook.json'


def print_menu(x):
    for i in x:
        print(x[i])

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

def print_mode(x):
    match (x):
        case 1:
            print('Создание нового контакта')
        case 2:
            print('Поиск контакта')
        case 3:
            print('Просмотр всего справочника')
        case 4:
            os.system('cls')
            print('\n\033[31m{}\033[0m'.format('Удаление контакта, восстановление данных будет невозможно'))
        case 5:
            os.system('cls')
            print('\n\033[31m{}\033[0m'.format('Удаление справочника, восстановление данных будет невозможно'))
        case 6:
            print('Конвертация справочника в формат JSON')
        case 7:
            print('Импорт справочника из формата JSON')
            




def res_operation(cont, x):
    match (x):
        case 1:
            print('\n\033[32m{}\033[0m'.format(f'Контакт "{cont[0].title()}, {cont[4].title()}" успешно добавлен\n'))
        case 2:
            print('\nПоиск контактов завершен')
        case 3:
            print('\nПросмотр справочника завершен\n')
        case 4:
            print('\nПоиск контактов для удаления завершен.\nВыбранные вами контакты удалены.')
        case 5:
            print('\n\033[31m{}\033[0m'.format('Телефонный справочник удален'))
        case 6:
            print(f'\nЭкспорт справочника завершен. Json файл находится: {data_json}\n')
        case 7:
            print(f'\nИмпорт справочника завершен.\n')
