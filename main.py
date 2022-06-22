from cgitb import text
from email import message
from typing import Text
from webbrowser import get
from flask import message_flashed
from telebot import types
from telebot import TeleBot
import requests
EURU = requests.get("https://free.currconv.com/api/v7/convert?q=EUR_RUB&compact=ultra&apiKey=626159f7b3598d14845d")
USRU = requests.get("https://free.currconv.com/api/v7/convert?q=USD_RUB&compact=ultra&apiKey=626159f7b3598d14845d")
CNRU = requests.get("https://free.currconv.com/api/v7/convert?q=CNY_RUB&compact=ultra&apiKey=626159f7b3598d14845d")

bot = TeleBot("5420849865:AAEKnic88WTs3cy1obUgZlI4i2EeKglNwic")


@bot.message_handler(commands=['start'])
def start(message):
  mess1 =  f'Привет, {message.from_user.first_name}! Чем могу помочь?'
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
  btn1 = types.KeyboardButton('Доллар = Рубль')
  btn2 = types.KeyboardButton('Евро = Рубль')
  btn3 = types.KeyboardButton('Юань = Рубль')

  markup.add(btn1, btn2, btn3)
  
  bot.send_message(message.chat.id, mess1, reply_markup=markup)

@bot.message_handler(content_types=['text'])
def dr(message):
  if message.text == 'Доллар = Рубль':
     bot.send_message(message.chat.id, USRU.content)
  elif message.text == 'Евро = Рубль':
     bot.send_message(message.chat.id, EURU.content)
  elif message.text == 'Юань = Рубль':
     bot.send_message(message.chat.id, CNRU.content)
  
  else:
    bot.send_message(message.chat.id, 'Error')

bot.polling(none_stop=True, interval=0)