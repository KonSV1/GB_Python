from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import time
import logging


async def hi_comm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info(f'Запрос --> {update.message.text}')
    logging.info(f'Ответ --> Привет {update.effective_user.first_name}')
    await update.message.reply_text(f'Привет {update.effective_user.first_name}')


async def help_comm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info(f'Запрос --> {update.message.text}')
    logging.info(f'Ответ --> /hi - приветствие\n/time - узнать дату и время\
        \n/calc - калькулятор для 2-х чисел')
    await update.message.reply_text(f'/hi - приветствие\n/time - узнать дату и время\
        \n/calc - калькулятор для 2-х чисел. Для получения справки по функции калькулятора наберите\n/helpCalc')


async def help_calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info(f'Запрос --> {update.message.text}')
    logging.info(f'Ответ --> helpCalc (msg)')
    await update.message.reply_text(f'Для проведения вычислений передайте строку вида:\
        \n/calc (число-1) (число-2) (символ оперрации)\nn+ - сумма\n- - разность\n* - произведение\n/ - деление')

async def time_comm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info(f'Запрос --> {update.message.text}')
    logging.info(
        f'Ответ --> {time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime())}')
    await update.message.reply_text(f'{time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime())}')


async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info(f'Запрос --> {update.message.text}')
    msg = (update.message.text).replace(",", ".")
    msg = msg.split()
    x, y, op = float(msg[1]), float(msg[2]), msg[3]
    match op:
        case '+':
            res = round(x + y, 2)
            logging.info(f'{x} {op} {y} = {res}')
        case '-':
            res = round(x - y, 2)
            logging.info(f'{x} {op} {y} = {res}')
        case '*':
            res = round(x * y, 2)
            logging.info(f'{x} {op} {y} = {res}')
        case '/':
            try:
                res = round(x / y, 2)
                logging.info(f'{x} {op} {y} = {res}')
            except ZeroDivisionError:
                res = 'на ноль делить нельзя'
                logging.info(f'{x} {op} {y} = {res}')
        case _:
            res = 'неизвестная операция'
            logging.info(f'{x} {op} {y} = {res}')
    await update.message.reply_text(f'{x} {op} {y} = {res}')
