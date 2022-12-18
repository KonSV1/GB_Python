from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_command as bc
import os

path = 'token.config'
d = open(path, 'r', encoding='utf-8')
KEY = d.readline()
app = ApplicationBuilder().token(KEY).build()

app.add_handler(CommandHandler("hi", bc.hi_comm))
app.add_handler(CommandHandler("time", bc.time_comm))
app.add_handler(CommandHandler("help", bc.help_comm))
app.add_handler(CommandHandler("sum", bc.sum_comm))
print('Server start')
app.run_polling()
