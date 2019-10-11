#!/usr/bin/env python

import telebot
name = '';
surname = '';
adress = '';
botle = '';

bot = telebot.TeleBot('989283902:AAG7bG9DCVPKvyWn3ljVZ0h-Vzr0csgazM8')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Хочу сделать заказ', 'Узнать о продукции')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('Есть тара', 'Нет тары')
keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3.row('Да', 'Нет')
keyboard4 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard4.row('Все верно', 'Исправить')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в компанию "Власов ключ"', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'хочу сделать заказ':
        bot.send_message(message.chat.id, 'У вас есть сменная тара?', reply_markup=keyboard2 )

    elif message.text.lower() == 'есть тара':
        start(message);
    elif message.text.lower() == 'все верно':
        bot.send_message(message.chat.id, 'Спасибо что пользуетесь нашим сервисом, Ваш заказ прибудет точно по расписанию!')
        start_message(message);
    elif message.text.lower() == 'исправить':
        start(message);
    elif message.text.lower() == 'узнать о продукции':
        bot.send_message(message.chat.id, 'Добро пожаловать на наш сайт, там вы найдете ответы на все интересующие вас вопросы' )
        bot.send_message(message.chat.id,'<a href="http://www.vlasovkluch.ru/">Заказать Власов Ключ</a>',
                 parse_mode="HTML")
        bot.send_message(message.chat.id, 'Готовы сделать заказ?',reply_markup=keyboard3 )
    elif message.text.lower() == 'что можешь?':
        bot.send_message(message.chat.id, 'Пока учусь, но учусь быстро!', reply_markup=keyboard1)
    elif message.text.lower() == 'да':
        start(message);


    elif message.text.lower() == 'нет':
        bot.send_message(message.chat.id, 'Всегда рады видеть Вас, удачи!', reply_markup=keyboard1  )



@bot.message_handler(content_types=['text'])
def start(message):
        bot.send_message(message.chat.id, "Как Вас зовут?");
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name


def get_name(message): #получаем фамилию
    global name;
    name = message.text;
    bot.send_message(message.chat.id, 'На какой день вы хотите заказать доставку?');
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
    bot.send_message(message.chat.id,''+name+', вы подтверждаете заказ на '+botle+' бутылки(ок), '+str(surname)+' по адресу '+str(adress)+'?', reply_markup=keyboard4)

bot.polling(none_stop=True, interval=0)
