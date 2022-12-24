rom aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import sqlite3
import openpyxl
import datetime
import aioschedule
import asyncio

bot = Bot(token='5463908802:AAE4DwiZErxX_9gg2kKQFUV3adFeccMNtuk')
dp = Dispatcher(bot)

connection = sqlite3.connect('Users.db')
cur = connection.cursor()

wb = openpyxl.load_workbook('schedule.xlsx')
sheets = wb.sheetnames
sheet = wb[sheets[0]]
fixed_schedule = False