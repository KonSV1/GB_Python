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
    await message.answer('Что запустить?', reply_markup=keyboard)


@dp.message_handler(text='Телефонный справочник')
async def start(message: types.Message):
    logging.info(message.text)
    global subjects
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
    await bot.send_message(chat_id=message.chat.id,text='Режим калькулятора', reply_markup=keyboard)
    mes = []
    @dp.message_handler(text=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','.','+','-', '/', '*','del', '(', ')', '='])
    async def s(message: types.Message):
        if message.text != '=':
            if message.text != 'del':
                mes.append(message.text)
            else:
                for _ in range(0,1):
                    mes.pop()
                    await message.answer(text=(''.join(mes)))
        else:
            await message.answer(text=(''.join(mes)))
            res = eval(''.join(mes))
            await message.answer(text=res)
            logging.info(f'{mes} = {res}')
            mes.clear()










     
        # await message.answer(text=st)




    await message.answer(text='Простой калькулятор', reply_markup=keyboard)

print('Server  starting')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
