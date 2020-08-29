import pyowm
import telebot
import datetime
import time
import eventlet
import requests
import logging
import schedule

owm = pyowm.OWM('', language = "ru")
bot = telebot.TeleBot("")

@bot.message_handler(content_types=['text'])

def send_echo(message):
  observation = owm.weather_at_place( message.text )
  w = observation.get_weather()
  temp = w.get_temperature('celsius')
  humidity = w.get_humidity()
  wind = w.get_wind()

  answer = "В городе " + message.text + " сейчас " + str(temp["temp"]) + "°C\n" \
           + "Максимальная температура: " + str(temp["temp_max"]) + "°C\n" \
           + "Минимальная температура: " + str(temp["temp_min"]) + "°C\n" \
           + "Влажность: " + str(humidity) + "%\n"
           


  bot.send_message(message.chat.id, answer)
  log(message)


def log(message):
  print("<!------!>")
  from datetime import datetime
  print(datetime.now())
  print("Сообщение от {0} {1} (id = {2}) \n {3}".format(message.from_user.first_name,
                                                        message.from_user.last_name,
                                                        str(message.from_user.id), message.text))





bot.infinity_polling()