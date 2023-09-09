import telebot
import requests
import json
from telebot import types

token = "6659756402:AAGwYhea35qBozf0nED94U3UVko0BARAyy4"

API_key = "f8a0fde2d802f8a84c8cac622c3ec957"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item = types.KeyboardButton("Weather")
    markup.add(item)
    bot.send_message(message.chat.id, "Привіт! Вибери сервіс :", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Weather")
def handle_button_click(message):
    bot.send_message(message.chat.id, "Введіть назву міста :")


@bot.message_handler(content_types=["text"])
def get_weather(message):
    city = message.text.strip().lower()
    kaka = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric"
    )
    json1 = json.loads(kaka.text)
    temp = json1["main"]["temp"]
    bot.send_message(message.chat.id, "Погода в  ", city, "{temp}")


bot.infinity_polling()
