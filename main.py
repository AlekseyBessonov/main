import traceback
import telebot
from config import currency, TOKEN
from extension import *




bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,
                 f"<Введите имя валюты, цену которой вы хотите узнать>\
<имя валюты, в которой надо узнать цену первой валюты>\
 <количество первой валюты>. Чтобы увидеть весь список доступных валют, введите /currency")
    print(message.text)


@bot.message_handler(commands=['currency'])
def Currency(message: telebot.types.Message):
    text = 'Вам доступны следующие валюты:'
    for key in currency.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def converter(message: telebot.types.Message):
    input_val = message.text.lower().split(' ')
    try:
        if len(input_val) != 3:
            raise ConversionExcepion(f"Много входных параметров! Для правильного ввода воспользуйтесь иструкцией /help")

        answer = CurrencyConverter.converter(input_val)
    except ConversionExcepion as e :
       bot.reply_to(message, f'Ошибка \n{e}')

    except BaseException as e:
        bot.reply_to(message, f'Неизвестная ошибка: \n{e}')


    else:
        bot.send_message(message.chat.id, answer)


bot.polling(timeout=10)
