from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
import asyncio
import logging
from openpyxl import load_workbook


ENC = 'utf-8'
FORMAT_INFO = '%(asctime)s, %(module)s, %(funcName)s, %(name)s, --> %(message)s'

logging.basicConfig(format=FORMAT_INFO, filename='project_1/log.txt',
                    filemode='a', encoding=ENC, level=logging.INFO, datefmt='%m/%d/%Y %H:%M:%S')
path = 'project_1/token_bot.config'  # файл с Токеном
d = open(path, 'r', encoding=ENC)
key = d.readline()
bot = Bot(token=key)
dp = Dispatcher(bot)
f_csv = 'project_1/phonebook_ooo.csv'
wb = load_workbook('project_1/phonebook_ooo.xlsx')
sheets = wb.sheetnames
sheet = wb[sheets[0]]


@dp.message_handler(commands='start')
@dp.message_handler(text='Главная')
async def cmd_start(message: types.Message):
    logging.info(message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Телефонный справочник', 'Калькулятор']
    keyboard.add(*buttons)
    Game = types.KeyboardButton('Игра в монетки')
    keyboard.row(Game)
    await bot.send_message(chat_id=message.chat.id, text='Что запустить?', reply_markup=keyboard)


@dp.message_handler(text='Телефонный справочник')
async def start(message: types.Message):
    logging.info(message.text)
    home = types.KeyboardButton('Главная')
    management = types.KeyboardButton('Руководство')
    administration = types.KeyboardButton('Аппарат при руководстве')
    department_1 = types.KeyboardButton('Отдел 1')
    department_2 = types.KeyboardButton('Отдел 2')
    department_3 = types.KeyboardButton('Отдел 3')
    department_4 = types.KeyboardButton('Отдел 4')
    department_5 = types.KeyboardButton('Отдел 5')
    department_6 = types.KeyboardButton('Отдел 6')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(home).row(management, administration).row(department_1, department_2, department_3)\
            .row(department_4, department_5, department_6)
    await bot.send_message(chat_id=message.chat.id, text='Запускаю телефонный справочник\
    \nДля просмотра служебных телефонов работников ООО "Рога и копыта"\
    нажмите на иконку интересующего вас подразделения', reply_markup=keyboard)


@dp.message_handler(text=['Руководство', 'Аппарат при руководстве', 'Отдел 1',
                          'Отдел 2', 'Отдел 3', 'Отдел 4', 'Отдел 5', 'Отдел 6'])
async def select(message: types.Message):
    logging.info(message.text)
    data = sheet.rows
    csv = open(f_csv, 'w', encoding=ENC)
    for row in data:
        l = list(row)
        for i in range(len(l)):
            if i == len(l) - 1:
                csv.write(str(l[i].value)+'\n')
            else:
                csv.write(str(l[i].value) + ',')
    csv.close()
    with open('project_1/phonebook_ooo.csv', 'r', encoding=ENC) as d:
        while True:
            cont = d.readline()
            if not cont:
                break
            if message.text in cont:
                cont = cont.split(',')
                cont = list(map(str, cont))
                await bot.send_message(chat_id=message.chat.id, text=(f'{cont[5]} {cont[0]}\nТел.(внутренний) - {cont[6]}\nТел.(город) - {cont[7]}\
                \nТел.(сот) - {cont[8]}\nE-mail - {cont[9]}'))
    csv.close()


@dp.message_handler(text='Калькулятор')
async def inp(message: types.Message):
    logging.info(message.text)
    zer = types.KeyboardButton('0')
    one = types.KeyboardButton('1')
    two = types.KeyboardButton('2')
    three = types.KeyboardButton('3')
    four = types.KeyboardButton('4')
    five = types.KeyboardButton('5')
    six = types.KeyboardButton('6')
    seven = types.KeyboardButton('7')
    eight = types.KeyboardButton('8')
    nine = types.KeyboardButton('9')
    home = types.KeyboardButton('Главная')
    mult = types.KeyboardButton('*')
    div = types.KeyboardButton('/')
    summ = types.KeyboardButton('+')
    diff = types.KeyboardButton('-')
    res = types.KeyboardButton('=')
    sep = types.KeyboardButton('.')
    a = types.KeyboardButton('(')
    b = types.KeyboardButton(')')
    delit = types.KeyboardButton('del')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(seven, eight, nine, mult, home).row(four, five, six, div, delit).row(one, two, three, diff, summ)\
            .row(zer, a, b, sep, res)
    await bot.send_message(chat_id=message.chat.id, text='Режим калькулятора', reply_markup=keyboard)
    mes = []

    @dp.message_handler(text=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '+', '-', '/', '*', 'del', '(', ')', '='])
    async def s(message: types.Message):
        if message.text != '=':
            if message.text != 'del':
                mes.append(message.text)
            else:
                for _ in range(0, 1):
                    mes.pop()
                    await bot.send_message(chat_id=message.chat.id, text=(''.join(mes)))
        else:
            await message.answer(text=(''.join(mes)))
            res = eval(''.join(mes))
            await bot.send_message(chat_id=message.chat.id, text=res)
            logging.info(f'{mes} = {res}')
            mes.clear()


@dp.message_handler(text='Игра в монетки')
async def note(message: types.Message):
    await message.answer(text='Предлагаю сыграть в игру на доверие. Правила игры просты:\nЕсть некий автомат в \
который два игрока по очереди могут опустить (Доверие) \
или не опускать (Обман) монетку.\n- Если оба игрока доверяют друг другу (оба опустили в автомат по монетке) то каждый из них\
получает в награду по 2 монеты.\n- Если оба игрока обманули друг друга (ни кто из обоих игроков не опустил в автомат монетку),\
то ни один из игроков награды не получает.\n- Если один из игроков обманывает, а второй доверяет, то обманщик получает в\
награду три монеты, доверившийся игрок награды не получает.\
\nИгра состоит из нескольких раундов по 10 ходов. Побеждает тот игрок, у которго по окончении игры больше монет.')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ['три', 'пять', 'десять', 'Главная']
    keyboard.add(*buttons)
    await bot.send_message(chat_id=message.chat.id, text='Выберете количество раундов', reply_markup=keyboard)
    m = 0
    @dp.message_handler(text=['три', 'пять', 'десять'])
    async def game(message: types.Message):
        logging.info(message.text)
        if message.text == 'три':
            m = 3
        if message.text == 'пять':
            m = 5
        if message.text == 'десять':
            m = 10
        await bot.send_message(chat_id=message.chat.id, text=(f'\nВыбрана игра из {m} раундов'))
        trust = types.KeyboardButton('Опустить монетку')
        cheat = types.KeyboardButton('Обмануть')
        home = types.KeyboardButton('Главная')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row(trust, cheat, home)
        await bot.send_message(chat_id=message.chat.id, text='Начнем', reply_markup=keyboard)
        opp = 1
        arr_pl = []
        arr_opp = []
        roun, s_pl, s_opp = 0, 0, 0
        rez_pl, rez_opp = 0, 0,
        logging.info(message.text)
        while roun < m:
            j = 0
            while j < 10:
                @dp.message_handler(text=['Опустить монетку', 'Обмануть'])
                async def game_start(message: types.Message,):
                    logging.info(message.text)
                    if message.text == 'Опустить монетку':
                        z_pl = 1
                    else:
                        z_pl = 0
                    arr_pl.append(z_pl)
                    logging.info(z_pl)
                    logging.info( arr_pl)
                    await bot.send_message(chat_id=message.chat.id, text=(f'\nРаунд {roun+1}, ход {len(arr_pl)}'))
                    nonlocal rez_pl
                    nonlocal rez_opp
                    match (opp):
                        case 1:  # Наивный
                            arr_opp.append(1)
                            if arr_pl[j] == 1:
                                rez_pl = rez_pl + 2
                                rez_opp = rez_opp + 2
                                arr_pl.append(1)
                                j +=1
                                await bot.send_message(chat_id=message.chat.id, text=(
                                        'Поздравляем, вы доверяете друг другу. Каждый игрок получает в награду по 2 монеты.'))
                                await bot.send_message(chat_id=message.chat.id, text=(
                                        f'Счет составляет: У вас {rez_pl} монет, у второго игрока {rez_opp} монет'))
                            else:
                                rez_pl = rez_pl + 3
                                j +=1
                                await bot.send_message(chat_id=message.chat.id, text=(
                                        'Вам удалось обмануть другого игрока. Вы получаете в награду 3 монеты, другой игрок ничего не получает.'))
                                await bot.send_message(chat_id=message.chat.id, text=(
                                        f'Счет составляет: У вас {rez_pl} монет, у второго игрока {rez_pl} монет'))
                        case 2:  # Обманщик
                            if arr_pl[j] == 1:
                                rez_opp = rez_opp + 3
                                print('\033[31m{}\033[0m'.format(
                                    'Сожалеем Вас обманули. Вы не получаете награды, другой игрок получает в награду 3 монеты.'))
                                print(
                                    f'Счет составляет: У вас {rez_pl} монет, у второго игрока {rez_opp} монет')
                                arr_opp.append(0)
                                j += 1
                            else:
                                print('\033[33m{}\033[0m'.format(
                                    'Вы не доверяете друг другу, ни кто из вас не получает награды.'))
                                print(
                                    f'Cчет составляет: У вас {rez_pl} монет, у второго игрока {rez_opp} монет')
                                arr_opp.append(0)
                                j += 1
                        case 3:  # Подражатель
                            if j == 0:
                                if arr_pl[j] == 1:
                                    rez_pl = rez_pl + 2
                                    rez_opp = rez_opp + 2
                                    print('\033[32m{}\033[0m'.format(
                                        'Поздравляем, вы доверяете друг другу. Каждый игрок получает в награду по 2 монеты.'))
                                    print(
                                        f'Счет составляет: У вас {rez_pl} монет, у второго игрока {rez_opp} монет')
                                    arr_opp.append(1)
                                    j += 1
                                else:
                                    rez_pl = rez_pl + 3
                                    print('\033[35m{}\033[0m'.format(
                                        'Вам удалось обмануть другого игрока. Вы получаете в награду 3 монеты, другой игрок ничего не получает.'))
                                    print(
                                        f'Счет составляет: У вас {rez_pl} монет, у второго игрока {rez_opp} монет')
                                    arr_opp.append(1)
                                    j += 1
                            else:
                                if arr_pl[j] == 1 and arr_pl[j-1] == 1:
                                    rez_pl = rez_pl + 2
                                    rez_opp = rez_opp + 2
                                    print('\033[32m{}\033[0m'.format(
                                        'Поздравляем, вы доверяете друг другу. Каждый игрок получает в награду по 2 монеты.'))
                                    print(
                                        f'Счет составляет: У вас {rez_pl} монет, у второго игрока {rez_opp} монет')
                                    arr_opp.append(1)
                                    j += 1
                                elif arr_pl[j] == 1 and arr_pl[j-1] == 0:
                                    rez_opp = rez_opp + 3
                                    print('\033[31m{}\033[0m'.format(
                                        'Сожалеем Вас обманули. Вы не получаете награды, другой игрок получает в награду 3 монеты.'))
                                    print(
                                        f'Счет составляет: У вас {rez_pl} монет, у второго игрока {rez_opp} монет')
                                    arr_opp.append(0)
                                    j += 1
                                elif arr_pl[j] == 0 and arr_pl[j-1] == 1:
                                    rez_pl = rez_pl + 3
                                    print('\033[35m{}\033[0m'.format(
                                        'Вам удалось обмануть другого игрока. Вы получаете в награду 3 монеты, другой игрок ничего не получает.'))
                                    print(
                                        f'Счет составляет: У вас {rez_pl} монет, у второго игрока {rez_opp} монет')
                                    arr_opp.append(1)
                                    j += 1
                                elif arr_pl[j] == 0 and arr_pl[j-1] == 0:
                                    print('\033[33m{}\033[0m'.format(
                                        'Вы не доверяете друг другу, ни кто из вас не получает награды.'))
                                    print(
                                        f'Cчет составляет: У вас {rez_pl} монет, у второго игрока {rez_opp} монет')
                                    arr_opp.append(0)
                                    j += 1
                        case 4:  # Злопамятный
                            if arr_pl[j] == 1 and 0 not in arr_pl:
                                rez_pl = rez_pl + 2
                                rez_opp = rez_opp + 2
                                print('\033[32m{}\033[0m'.format(
                                    'Поздравляем, вы доверяете друг другу. Каждый игрок получает в награду по 2 монеты.'))
                                print(
                                    f'Счет составляет: У вас {rez_pl} монет, у второго игрока {rez_opp} монет')
                                arr_opp.append(1)
                                j += 1
                            elif arr_pl[j] == 0 and sum(arr_pl) == len(arr_pl)-1:
                                rez_pl = rez_pl + 3
                                print('\033[35m{}\033[0m'.format(
                                    'Вам удалось обмануть другого игрока. Вы получаете в награду 3 монеты, другой игрок ничего не получает.'))
                                print(
                                    f'Счет составляет: У вас {rez_pl} монет, у второго игрока {rez_opp} монет')
                                arr_opp.append(1)
                                j += 1
                            elif arr_pl[j] == 1 and sum(arr_pl) < len(arr_pl):
                                rez_opp = rez_opp + 3
                                print('\033[31m{}\033[0m'.format(
                                    'Сожалеем Вас обманули. Вы не получаете награды, другой игрок получает в награду 3 монеты.'))
                                print(
                                    f'Счет составляет: У вас {rez_pl} монет, у второго игрока {rez_opp} монет')
                                arr_opp.append(0)
                                j += 1
                            elif arr_pl[j] == 0 and sum(arr_pl) < len(arr_pl) - 1:
                                print('\033[33m{}\033[0m'.format(
                                    'Вы не доверяете друг другу, ни кто из вас не получает награды.'))
                                print(
                                    f'Cчет составляет: У вас {rez_pl} монет, у второго игрока {rez_opp} монет')
                                arr_opp.append(0)
                                j += 1
                        case 5:  # Детектив
                            match(j):
                                case 0:
                                    if arr_pl[j] == 0:
                                        rez_pl = rez_pl + 3
                                        print('\033[35m{}\033[0m'.format(
                                            'Вам удалось обмануть другого игрока. Вы получаете в награду 3 монеты, другой игрок ничего не получает.'))
                                        print(
                                            f'Счет составляет: У вас {rez_pl} монет, у второго игрока {rez_opp} монет')
                                        arr_opp.append(1)
                                        j += 1
                                    else:
                                        rez_pl = rez_pl + 2
                                        rez_opp = rez_opp + 2
                                        print('\033[32m{}\033[0m'.format(
                                            'Поздравляем, вы доверяете друг другу. Каждый игрок получает в награду по 2 монеты.'))
                                        print(
                                            f'Счет составляет: У вас {rez_pl} монет, у второго игрока {rez_opp} монет')
                                        arr_opp.append(1)
                                        j += 1
                                case 1:
                                    if arr_pl[j] == 0:
                                        print('\033[33m{}\033[0m'.format(
                                            'Вы не доверяете друг другу, ни кто из вас не получает награды.'))
                                        arr_opp.append(0)
                                        j += 1
                                    else:
                                        rez_opp = rez_opp + 3
                                        print('\033[31m{}\033[0m'.format(
                                            'Сожалеем Вас обманули. Вы не получаете награды, другой игрок получает в награду 3 монеты.'))
                                        print(
                                            f'Счет составляет: У вас {rez_pl} монет, у второго игрока {rez_opp} монет')
                                        arr_opp.append(0)
                                        j += 1
                                case 2:
                                    if arr_pl[j] == 0:
                                        rez_pl = rez_pl + 3
                                        print('\033[35m{}\033[0m'.format(
                                            'Вам удалось обмануть другого игрока. Вы получаете в награду 3 монеты, другой игрок ничего не получает.'))
                                        print(
                                            f'Счет составляет: У вас {rez_pl} монет, у второго игрока {rez_opp} монет')
                                        arr_opp.append(1)
                                        j += 1
                                    else:
                                        rez_pl = rez_pl + 2
                                        rez_opp = rez_opp + 2
                                        print('\033[32m{}\033[0m'.format(
                                            'Поздравляем, вы доверяете друг другу. Каждый игрок получает в награду по 2 монеты.'))
                                        print(
                                            f'Счет составляет: У вас {rez_pl} монет, у второго игрока {rez_opp} монет')
                                        arr_opp.append(1)
                                        j += 1
                                case 3:
                                    if arr_pl[j] == 0:
                                        rez_pl = rez_pl + 3
                                        print('\033[35m{}\033[0m'.format(
                                            'Вам удалось обмануть другого игрока. Вы получаете в награду 3 монеты, другой игрок ничего не получает.'))
                                        print(
                                            f'Счет составляет: У вас {rez_pl} монет, у второго игрока {rez_opp} монет')
                                        arr_opp.append(1)
                                        j += 1
                                    else:
                                        rez_pl = rez_pl + 2
                                        rez_opp = rez_opp + 2
                                        print('\033[32m{}\033[0m'.format(
                                            'Поздравляем, вы доверяете друг другу. Каждый игрок получает в награду по 2 монеты.'))
                                        print(
                                            f'Счет составляет: У вас {rez_pl} монет, у второго игрока {rez_opp} монет')
                                        arr_opp.append(1)
                                        j += 1
                                case _:
                                    if arr_pl[2] == 0:
                                        if arr_pl[j] == 1 and arr_pl[j-1] == 1:
                                            rez_pl = rez_pl + 2
                                            rez_opp = rez_opp + 2
                                            print('\033[32m{}\033[0m'.format(
                                                'Поздравляем, вы доверяете друг другу. Каждый игрок получает в награду по 2 монеты.'))
                                            print(
                                                f'Счет составляет: У вас {rez_pl} монет, у второго игрока {rez_opp} монет')
                                            arr_opp.append(1)
                                            j += 1
                                        elif arr_pl[j] == 1 and arr_pl[j-1] == 0:
                                            rez_opp = rez_opp + 3
                                            print('\033[31m{}\033[0m'.format(
                                                'Сожалеем Вас обманули. Вы не получаете награды, другой игрок получает в награду 3 монеты.'))
                                            print(
                                                f'Счет составляет: У вас {rez_pl} монет, у второго игрока {rez_opp} монет')
                                            arr_opp.append(0)
                                            j += 1
                                        elif arr_pl[j] == 0 and arr_pl[j-1] == 1:
                                            rez_pl = rez_pl + 3
                                            print('\033[35m{}\033[0m'.format(
                                                'Вам удалось обмануть другого игрока. Вы получаете в награду 3 монеты, другой игрок ничего не получает.'))
                                            print(
                                                f'Счет составляет: У вас {rez_pl} монет, у второго игрока {rez_opp} монет')
                                            arr_opp.append(1)
                                            j += 1
                                        elif arr_pl[j] == 0 and arr_pl[j-1] == 0:
                                            print('\033[33m{}\033[0m'.format(
                                                'Вы не доверяете друг другу, ни кто из вас не получает награды.'))
                                            print(
                                                f'Cчет составляет: У вас {rez_pl} монет, у второго игрока {rez_opp} монет')
                                            arr_opp.append(0)
                                            j += 1
                                    else:
                                        if arr_pl[j] == 1:
                                            rez_opp = rez_opp + 3
                                            print('\033[31m{}\033[0m'.format(
                                                'Сожалеем Вас обманули. Вы не получаете награды, другой игрок получает в награду 3 монеты.'))
                                            print(
                                                f'Счет составляет: У вас {rez_pl} монет, у второго игрока {rez_opp} монет')
                                            arr_opp.append(0)
                                            j += 1
                                        else:
                                            print('\033[33m{}\033[0m'.format(
                                                'Вы не доверяете друг другу, ни кто из вас не получает награды.'))
                                            print(
                                                f'Cчет составляет: У вас {rez_pl} монет, у второго игрока {rez_opp} монет')
                                            arr_opp.append(0)
                                            j += 1
                    s_pl = s_pl + rez_pl
                    s_opp = s_opp + rez_opp
                    roun += 1
                    await(f'---------------\nРезультаты раунда {roun+1}:\
            \nКоличество Ваших монет - {rez_pl} \nКоличество монет у другого игрока - {rez_opp}\
            \nКоличество монет по результатам {roun+1} раундов: У вас {s_pl}, у другого игрока {s_opp}\n---------------')
                    logging.info(
                    f'{opp} 1-Наивный, 2-Обманщик, 3-Подражатель, 4-Злопамятный, 5- Детектив')
                    logging.info(f'Ходы игрока\t\t{arr_pl}, очки игрока {rez_pl}')
                    logging.info(
                    f'Ходы соперника\t{arr_opp}, очки соперника {rez_opp}')
                    arr_pl.clear()
                    arr_opp.clear()
                
            await(f'\nРезультаты игры:\
                    \nКоличество Ваших монет - {s_pl} \nКоличество монет у другого игрока - {s_opp}')
            if s_pl > s_opp:
                await('Поздравляем, вы выиграли')
            if s_pl < s_opp:
                await('Сожалеем Вы проиграли.')
            if s_pl == s_opp:
                await('"Победила Дружба"')


print('Server  starting')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
