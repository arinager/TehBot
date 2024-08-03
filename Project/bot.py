from config import *
from telebot import TeleBot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telebot import types
import sqlite3 
from config import DATABASE



bot = TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """
Привет!👋
Я - бот - тех.поддержка! Появились вопросы? Возможно, это один из них!😃 
Пропиши команду info, чтобы увидеть список самых частозадаваемых вопросов🤖
""")
    
@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id,
"""
✨Вот вопросы, которые задают нам чаще всего:

○ Как оформить заказ?
○ Как узнать статус моего заказа?
○ Как отменить заказ?
○ Что делать, если товар пришел поврежденным?
○ Как связаться с вашей технической поддержкой?
○ Как узнать информацию о доставке?
""")
    

@bot.message_handler(func=lambda message: True)
def echo_message(message):

    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("SELECT * FROM qa WHERE questions = ?",(message.text,))
    result = cur.fetchall()
    if result: 
        bot.reply_to(message, result[0][1])
    else:
        bot.send_message(message.chat.id, """Похоже, что такого вопроса нету в списке🙁
Ознакомьтесь со списком всех частозадаваемых вопросов через команду info📋""")

bot.infinity_polling()