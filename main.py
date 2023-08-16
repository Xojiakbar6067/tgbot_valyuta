import telebot
import buttons as bt
from telebot.types import ReplyKeyboardRemove as remove
usd_count=12110.21
eur_count=13217.87
rub_count=124.71

#регистрация бота
bot=telebot.TeleBot('6420185233:AAHPwX7kkN5fqLUJwVc6ys3fD4v_9JZcras')

#пропишем алгоритм
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, "приветывую в нашем боте", reply_markup=bt.choice_buttons())

@bot.message_handler(content_types=['text'])
def text_message(message):
    if message.text=='Курс валюты':
        bot.send_message(message.from_user.id, 'курс доллара \nкурс йевро \nкурс рубля', reply_markup=bt.button1())
        bot.register_next_step_handler(message, tranzak)
    else:
        bot.send_message(message.from_user.id, 'я вас не понял')
def tranzak(message):
    if message.text=='USD':
        bot.send_message(message.from_user.id, f'сегодняшный курс доллара {usd_count}, сколко USD хотите менят?', reply_markup=remove())
        bot.register_next_step_handler(message, usd)
    elif message.text=='EUR':
        bot.send_message(message.from_user.id, f'сегодняшный курс евро {eur_count}, сколко USD хотите менят?', reply_markup=remove())
        bot.register_next_step_handler(message, eur)
    elif message.text=='RUB':
        bot.send_message(message.from_user.id, f'сугодняшный курс рубля {rub_count}, сколко USD хотите менят?', reply_markup=remove())
        bot.register_next_step_handler(message, rub)
    else:
        pass

def usd(message):
    amount=int(message.text)
    change=amount*usd_count
    bot.send_message(message.from_user.id, change, reply_markup=bt.choice_buttons())
    bot.register_next_step_handler(message, text_message)
def eur(message):
    amount=int(message.text)
    change=amount*eur_count
    bot.send_message(message.from_user.id, change, reply_markup=bt.choice_buttons())
    bot.register_next_step_handler(message, text_message)
def rub(message):
    amount=int(message.text)
    change=amount*rub_count
    bot.send_message(message.from_user.id, change, reply_markup=bt.choice_buttons())
    bot.register_next_step_handler(message, text_message)
#запуск бота
bot.polling(non_stop=True)