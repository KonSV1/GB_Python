import os
import csv
import json
import logging


ENC = 'utf-8'
data_csv = 'DZ/DZ_8/phonebook.csv'
data_json = 'DZ/DZ_8/phonebook.json'
data_xml = 'DZ/DZ_8/phonebook.xml'


def new_contact(cont):
    with open(data_csv, 'a', encoding=ENC) as d:
        d.writelines(f'{cont[0]},')
        d.writelines(f'{cont[1]},')
        d.writelines(f'{cont[2]},')
        d.writelines(f'{cont[3]},')
        d.writelines(f'{cont[4]}\n')
    return cont


def serch_cont(name):
    print('Фамилия'.center(20).title(), '!'.center(1), 'Имя'.center(20).title(),
          '!'.center(1), 'Отчество'.center(20).title(), '!'.center(1),
          '№ телефона'.center(23).title(), '!'.center(1), 'Описание\n'.center(35).title())
    logging.info(f'/Поиск --> {name}')
    with open(data_csv, 'r', encoding=ENC) as d:
        j = 0
        k = 0
        while True:
            cont = d.readline()
            if not cont:
                if j == 0:
                    print('\n\033[31m{}\033[0m'.format(
                        f'\n"{name}" в справочнике не найден'))
                    logging.info(f'{name} --> не найден')
                break
            if name in cont:
                cont = cont.split(',')
                cont = list(map(str, cont))
                print(cont[0].center(20).title(), '!'.center(1), cont[1].center(20).title(),
                      '!'.center(1), cont[2].center(20).title(), '!'.center(1),
                      cont[3].center(23).title(), '!'.center(1), cont[4].center(35).title())
                j += 1
                k += 1
                logging.info(f'Найден --> {cont}')
        logging.info(f'Поиск --> ok. Найдено {k}')


def print_phonebook():
    with open(data_csv, 'r', encoding=ENC) as d:
        while True:
            cont = d.readline()
            if not cont:
                break
            cont = cont.split(',')
            cont = list(map(str, cont))
            print((cont[0].center(20)).title(), '!'.center(1), (cont[1].center(20)).title(), '!'.center(1), cont[2].center(20).title(), '!'.center(1),
                  cont[3].center(23).title(), '!'.center(1), cont[4].center(35).title())


def del_cont(ob):
    logging.info(f'/Поиск для удаления --> {ob}')
    list_cont = []
    with open(data_csv, 'r', encoding=ENC) as d:
        while True:
            cont = d.readline()
            if not cont:
                break
            list_cont.append(cont)
    j = 0
    while j < len(list_cont):
        if (ob).lower() in list_cont[j]:
            print('\n\033[33m{}\033[0m'.format(list_cont[j].title()))
            print('\033[31m{}\033[0m'.format('Удалить контакт?'))
            x = int(input('\n1 - Удалить\n2 - Пропустить\n--> '))
            if x == 1:
                print('\033[31m{}\033[0m'.format(
                    f'{list_cont[j].title()} Удален'))
                logging.info((f'Найден -->{list_cont[j].title()} --> Удален'))
                list_cont.pop(j)
            else:
                logging.info(
                    (f'Найден -->{list_cont[j].title()} --> Удаление отменено'))
                j += 1
        else:
            j += 1
    d = open(data_csv, 'w', encoding=ENC, newline='\n')
    for i in list_cont:
        d.write(f'{i}')
    d.close()


def file_del():
    print('\n\033[31m{}\033[0m'.format(
        '\nУдалить справочник?:\n1 - Удалить\n2 - Не удалять--> '))
    while (r := int(input())) < 1 or r > 2:
        print('\n\033[31m{}\033[0m'.format('Неверно выбран режим работы'))
    if r == 1:
        os.remove(data_csv)
        print('Справочник удален')
        logging.info(f'{data_csv} --> Удален')
    else:
        print('Удаление отменено')
        logging.info('Удаление отменено')
   


def csv_to_json():
    json_arr = []
    with open(data_csv, 'r', newline='\n', encoding=ENC) as d:
        csv_list = csv.DictReader(d)
        for i in csv_list:
            json_arr.append(i)
    with open(data_json, 'w', encoding=ENC) as j:
        json_list = json.dumps(json_arr, indent=4)
        j.write(json_list)


def json_to_csv():
    with open(data_json, 'r', encoding=ENC) as jf:
        data = json.load(jf)
        data_file = open(data_csv, 'w', encoding=ENC, newline='\n')
        csv_writer = csv.writer(data_file)
        count = 0
        for emp in data:
            if count == 0:
                header = emp.keys()
                csv_writer.writerow(header)
                count += 1
            csv_writer.writerow(emp.values())
        data_file.close()



def convert_row(i):
    return """<phonebook>
	<фамилия>%s</фамилия>
    <имя>%s</имя>
    <отчество>%s</отчество>
    <телефон>%s</телефон>
    <описание>%s</описание>
    </phonebook>""" % (i[0], i[1] ,i[2] , i[3], i[4])

def csv_to_xml():
    xml_arr = []
    with open(data_csv, 'r', newline='\n', encoding=ENC) as d:
        csv_list = csv.reader(d)
        for i in csv_list:
            xml_arr.append(i)
    # print(xml_arr[1:2])
    with open(data_xml, 'w', encoding=ENC) as f:
        f.write('\n'.join([convert_row(i) for i in xml_arr[1:]]))

