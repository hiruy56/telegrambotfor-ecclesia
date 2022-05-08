import os
import telebot


API_KEY = os.getenv("5350511309:AAGT4OaAMSO1aEFhRGN1ZWKmAPz73HPOJR8")
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['pricing'])
def price(message):
  bot.send_message(message.chat.id, "first floor price per month:xxxDollars(xxxBirr) Current(www)\nfirst floor 2 price per month xxxDollars(xxxbirr) Current(www)\nSecond floor price per month xxxDollars(xxxBirr)")
  
@bot.message_handler(commands=['about'])
def about(message):
  bot.send_message(message.chat.id, "Luxurious Fully Furnished Apartment for rent We would like to introduce to you our Brand New Luxurious FullyFurnished Apartment  located at BISRATE GEBRIEL Area, AddisAbaba,Ethiopia . This NEW Luxurious apartment is a western-contemporary style residential property. The wholesale building is provided with a high level of Finishing such as Decorative Gypsum Works and lighting. The whole building is provided with a high level of amenities and. facilities. Description\n-CCTV camera\n-Free WIFI zone whole building\n-Water Storage\n-Backup Generator\n-Reception Area\n-Price range 1500$ to 2500$ dollars")
                   
@bot.message_handler(commands=['phone'])
def phone(message):
  bot.send_message(message.chat.id, "+251911241355")
  
@bot.message_handler(commands=['location'])
def location(message):
  bot.send_message(message.chat.id, "https://maps.app.goo.gl/P4Vm6HPqGHy1poSp6 or BISRATE GEBRIEL Area, AddisAbaba,Ethiopia ")

pic = 'https://github.com/TelegramBots/book/raw/master/src/docs/photo-ara.jpg'

#@bot.message_handler(commands=['Galery'])
#def galery(ecclesia):
  #bot.sendPhoto(ecclesia, photo=open('test.jpg', 'rb'))

bot.polling()
