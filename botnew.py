#!/usr/bin/env python

import telebot
import requests
name = '';
surname = '';
adress = '';
botle = '';

bot = telebot.TeleBot('989283902:AAG7bG9DCVPKvyWn3ljVZ0h-Vzr0csgazM8')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Привет', 'Пока')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('Как зовут?', 'Что можешь?')
keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3.row('Да', 'Нет')
keyboard4 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard4.row('Все верно', 'Исправить')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, петушара', reply_markup=keyboard2 )
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Уебывай, ихтиандр хуев')
    elif message.text.lower() == 'здравствуй':
        bot.send_message(message.chat.id, 'Ну здарова')
    elif message.text.lower() == 'здарова':
        bot.send_message(message.chat.id, 'Пизда у коровы')
    elif message.text.lower() == 'как дела?':
        bot.send_message(message.chat.id, 'Ахуенно, все работает')
    elif message.text.lower() == 'как зовут?':
        bot.send_message(message.chat.id, 'тебя ебать не должно, лучше закажи водичку' )
        bot.send_message(message.chat.id,'<a href="http://www.vlasovkluch.ru/">Заказать Власов Ключ</a>',
                 parse_mode="HTML")
        bot.send_message(message.chat.id, 'Будешь брать?',reply_markup=keyboard3 )
    elif message.text.lower() == 'что можешь?':
        bot.send_message(message.chat.id, 'Пока учусь, но учусь быстро!', reply_markup=keyboard1)
    elif message.text.lower() == 'да':
        bot.send_message(message.chat.id, 'Красава, мы ценим наших клиентов!' )
        bot.send_message(message.chat.id, 'Напишите ваше имя', start(message))


    elif message.text.lower() == 'нет':
        bot.send_message(message.chat.id, 'Подумай хорошо, кожаный ублюдок', reply_markup=keyboard3  )



@bot.message_handler(content_types=['text'])
def start(message):
        bot.send_message(message.chat.id, "Как тебя зовут?");
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name


def get_name(message): #получаем фамилию
    global name;
    name = message.text;
    bot.send_message(message.chat.id, 'Какая у тебя фамилия?');
    bot.register_next_step_handler(message, get_surname);

def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message(message.chat.id,'Адрес доставки?');
    bot.register_next_step_handler(message, get_adress);

def get_adress(message):
    global adress;
    adress = message.text;
    bot.send_message(message.chat.id,'Сколько бутылок?');
    bot.register_next_step_handler(message, get_botle);

def get_botle(message):
    global botle;
    botle = message.text;
    bot.send_message(message.chat.id, 'Адрес '+str(adress)+', тебя зовут '+name+' '+surname+', '+botle+' бутылки(ок) ?', reply_markup=keyboard4)

bot.polling(none_stop=True)
