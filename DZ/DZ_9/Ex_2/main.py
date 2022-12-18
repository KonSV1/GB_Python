from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_command as bc
import os

app = ApplicationBuilder().token("5918521840:AAGcuyAaSAr_jSxvRMlQH1DmOuC3ii4L7as").build()

app.add_handler(CommandHandler("hi", bc.hi_comm))
app.add_handler(CommandHandler("time", bc.time_comm))
app.add_handler(CommandHandler("help", bc.help_comm))
app.add_handler(CommandHandler("sum", bc.sum_comm))
print('Server start')
app.run_polling()
