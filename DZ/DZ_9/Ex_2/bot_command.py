from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import time
from spy import *


async def hi_comm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')

async def help_comm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hi - приветствие\n/time - узнать дату и время\
        \n/sum - посчитать сумму 2-х чисел ("/sum"_"число1"_"число2")')

async def time_comm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'{time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime())}')

async def sum_comm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = (update.message.text).split()
    x, y = int(msg[1]), int(msg[2]),
    await update.message.reply_text(f'{x} + {y} = {x+y}')
