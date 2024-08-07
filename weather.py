import telebot
import requests

TOKEN = 'Token'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'Напиши город, чтобы узнать погоду.')


def get_weather(city):
    url = f'http://wttr.in/{city}?format=3&lang=ru'
    response = requests.get(url)

    if response.status_code ==200:
        return response.text.strip()
    else:
        return 'Город не найден.'

@bot.message_handler(commands=['weather'])
def send_weather(message):
    try:
        city = message.text.split()[1]
        weather_info = get_weather(city)
        bot.reply_to(message,weather_info)
    except IndexError:
        bot.reply_to(message, 'Пожалуйста укажите город.')


bot.polling()