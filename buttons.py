from telebot import types

def choice_buttons():
    #создаем пространство для кнопок
    kb=types.ReplyKeyboardMarkup(resize_keyboard=True)
    #создаем сами кнопкие
    tranzak=types.KeyboardButton('Курс валюты')
    #добавит кнопки в пронстранству
    kb.add(tranzak)
    return kb
def button1():
    kb=types.ReplyKeyboardMarkup(resize_keyboard=True)
    dollar=types.KeyboardButton('USD')
    evro=types.KeyboardButton('EUR')
    rubl=types.KeyboardButton('RUB')
    kb.add(dollar, evro, rubl)
    return kb