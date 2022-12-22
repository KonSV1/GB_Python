from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
import logging

import bot_command as bc

ENC = 'utf-8'
FORMAT_INFO = '%(asctime)s, %(module)s, %(funcName)s, %(name)s, --> %(message)s'

logging.basicConfig(format=FORMAT_INFO, filename='DZ/DZ_9/Ex_2/log.txt',
                    filemode='a', encoding=ENC, level=logging.INFO, datefmt='%m/%d/%Y %H:%M:%S')

path = 'token.config'  # файл с Токеном
d = open(path, 'r', encoding='utf-8')
KEY = d.readline()

app = ApplicationBuilder().token(KEY).build()
app.add_handler(CommandHandler("hi", bc.hi_comm))
app.add_handler(CommandHandler("time", bc.time_comm))
app.add_handler(CommandHandler("help", bc.help_comm))
app.add_handler(CommandHandler("helpCalc", bc.help_calc))
app.add_handler(CommandHandler("calc", bc.calc))
print('Server start')
app.run_polling()
