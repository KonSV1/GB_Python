from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import time


def log(update: Update, context: ContextTypes):
    file  = open('Lection/Lection_5/db.csv','a', encoding='utf-8')
    file.write(f'{update.effective_user.first_name},{update.effective_user.id},{time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime())},{update.message.text}\n')
    file.close()