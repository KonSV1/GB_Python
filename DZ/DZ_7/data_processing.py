import os
import input_data as ind



ENC = 'utf-8'
# data = 'Python/DZ/DZ_7/phonebook.txt'
data_csv = 'Python/DZ/DZ_7/phonebook.csv'


def new_contact(cont):
    with open(data_csv, 'a', encoding=ENC) as d:
        d.writelines(f'{cont[0]},')
        d.writelines(f'{cont[1]},')
        d.writelines(f'{cont[2]},')
        d.writelines(f'{cont[3]},')
        d.writelines(f'{cont[4]}; \n')
    print('\n\033[32m{}\033[0m'.format(f'Контакт "{cont[0]} {cont[4]}" успешно добавлен\n'))

# new_contact(ind.input_data())

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

print_phonebook()

# def print_phonebook():  # Можно вывести весь справочник таким способом, но мне не нравится формат вывода
#     with open(data, 'r', newline='\n', encoding=ENC) as d:
#         for el in d:
#             print(el.strip())


def serch_cont(r, name):
    with open(data_csv, 'r', encoding=ENC) as d:
        j=0
        while True:
            cont = d.readline()
            if not cont:
                if j == 0:
                    print('\n\033[31m{}\033[0m'.format(f'\n"{name}" в справочнике не найден'))
                break
            cont = cont.split(',')
            cont = list(map(str, cont))
            if r == 1:
                if cont[0] == name:
                    print('')
                    print(*cont, sep='\t')
                    j+=1
            if r == 2:
                if cont[3] == name:
                    print('')
                    print(*cont, sep='\t')
                    j+=1


# def txt_csv():
#     c = open(data_csv, 'w', encoding=ENC, newline='\n')
#     c.writelines('Фамилия,Имя,Отчество,Телефон,Описание;\n')
#     with open(data, 'r', newline='\n', encoding=ENC) as d:
#         while True:
#             cont = d.readline()
#             if not cont:
#                 break
#             cont = cont.split(',')
#             cont = list(map(str, cont))
#             c.writelines(f'{cont[0]},')
#             c.writelines(f'{cont[1]},')
#             c.writelines(f'{cont[2]},')
#             c.writelines(f'{cont[3]},')
#             c.writelines(f'{cont[4]}')
#     c.close()
#     print(f'\nЭкспорт справвочника завершен. CSV файл находится: {data_csv}\n')


def file_del():
    os.remove(data_csv)
    print('\n\033[31m{}\033[0m'.format('Телефонный справочник удален'))


# def csv_txt():
#     d = open(data, 'w', encoding=ENC, newline='\n')
#     with open(data_csv, 'r', encoding=ENC) as c:
#         i = 0
#         while True:
#             while i < 1:
#                 c.readline()
#                 i += 1
#             cont = c.readline()
#             if not cont:
#                 break
#             cont = cont.split(',')
#             cont = list(map(str, cont))

#             d.writelines(f'{cont[0]},')
#             d.writelines(f'{cont[1]},')
#             d.writelines(f'{cont[2]},')
#             d.writelines(f'{cont[3]},')
#             d.writelines(f'{cont[4]}')
#     d.close()
#     print(f'\nИмпорт справвочника завершен.\n')


def del_cont(ob):
    list_cont = []
    with open(data, 'r', encoding=ENC) as d:
        for el in d:
            el = el.replace('\n', '')
            list_cont.append(el)
        j = 0
        while j < len(list_cont):
            if ob in list_cont[j]:
                print('\n\033[31m{}\033[0m'.format(list_cont[j]))
                print('\033[31m{}\033[0m'.format('Удалить контакт?'))
                x = int(input('\n1 - Удалить\n2 - Пропустить\n--> '))
                if x == 1:
                    print('\033[31m{}\033[0m'.format(f'{list_cont[j]} Удален'))
                    list_cont.pop(j)
                else:
                    j+=1
            else:
                j+=1
        d = open(data, 'w', encoding=ENC)
        for i in list_cont:
            d.write(f'{i}\n')
        d.close()
    print('\nПоиск контактов для удаления завершен.\nВыбранные вами контакты удалены.')



