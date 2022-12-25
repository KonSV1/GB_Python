from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import sqlite3
import datetime
import aioschedule
import asyncio
import logging
import sqlite3 as sl
from openpyxl import load_workbook
import data_control as dc

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
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Телефонный справочник', 'Калькулятор']
    keyboard.add(*buttons)
    await message.answer('Что запустить?', reply_markup=keyboard)

@dp.message_handler(text='Телефонный справочник')
async def start(message: types.Message):
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
    mes = message.text
    logging.info(mes)
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
            if mes in cont:
                cont = cont.split(',')
                cont = list(map(str, cont))
                await bot.send_message(chat_id=message.chat.id, text=(f'{cont[5]} {cont[0]}\nТел.(внутренний) - {cont[6]}\nТел.(город) - {cont[7]}\
                \nТел.(сот) - {cont[8]}\nE-mail - {cont[9]}'))
    csv.close()

print('Server  starting')
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
