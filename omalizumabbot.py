import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

# Данные о рекомендуемых дозах хранятся в data1 или data2 в зависимости от кратности введения
data1 = [
    # Введение требуется 1 раз в 2 недели
    {'ig_level': {'from': 30.0, 'to': 100.0}, 'weight': {'from': 20.0, 'to': 25.0}, 'dose': 75.0},
    {'ig_level': {'from': 30.0, 'to': 100.0}, 'weight': {'from': 25.0, 'to': 30.0}, 'dose': 75.0},
    {'ig_level': {'from': 30.0, 'to': 100.0}, 'weight': {'from': 30.0, 'to': 40.0}, 'dose': 75.0},
    {'ig_level': {'from': 30.0, 'to': 100.0}, 'weight': {'from': 40.0, 'to': 50.0}, 'dose': 150.0},
    {'ig_level': {'from': 30.0, 'to': 100.0}, 'weight': {'from': 50.0, 'to': 60.0}, 'dose': 150.0},
    {'ig_level': {'from': 30.0, 'to': 100.0}, 'weight': {'from': 60.0, 'to': 70.0}, 'dose': 150.0},
    {'ig_level': {'from': 30.0, 'to': 100.0}, 'weight': {'from': 70.0, 'to': 80.0}, 'dose': 150.0},
    {'ig_level': {'from': 30.0, 'to': 100.0}, 'weight': {'from': 80.0, 'to': 90.0}, 'dose': 150.0},
    {'ig_level': {'from': 30.0, 'to': 100.0}, 'weight': {'from': 90.0, 'to': 125.0}, 'dose': 300.0},
    {'ig_level': {'from': 30.0, 'to': 100.0}, 'weight': {'from': 125.0, 'to': 150.0}, 'dose': 300.0},

    {'ig_level': {'from': 100.0, 'to': 200.0}, 'weight': {'from': 20.0, 'to': 25.0}, 'dose': 150.0},
    {'ig_level': {'from': 100.0, 'to': 200.0}, 'weight': {'from': 25.0, 'to': 30.0}, 'dose': 150.0},
    {'ig_level': {'from': 100.0, 'to': 200.0}, 'weight': {'from': 30.0, 'to': 40.0}, 'dose': 150.0},
    {'ig_level': {'from': 100.0, 'to': 200.0}, 'weight': {'from': 40.0, 'to': 50.0}, 'dose': 300.0},
    {'ig_level': {'from': 100.0, 'to': 200.0}, 'weight': {'from': 50.0, 'to': 60.0}, 'dose': 300.0},
    {'ig_level': {'from': 100.0, 'to': 200.0}, 'weight': {'from': 60.0, 'to': 70.0}, 'dose': 300.0},
    {'ig_level': {'from': 100.0, 'to': 200.0}, 'weight': {'from': 70.0, 'to': 80.0}, 'dose': 300.0},
    {'ig_level': {'from': 100.0, 'to': 200.0}, 'weight': {'from': 80.0, 'to': 90.0}, 'dose': 300.0},
    {'ig_level': {'from': 100.0, 'to': 200.0}, 'weight': {'from': 90.0, 'to': 125.0}, 'dose': 450.0},
    {'ig_level': {'from': 100.0, 'to': 200.0}, 'weight': {'from': 125.0, 'to': 150.0}, 'dose': 600.0},

    {'ig_level': {'from': 200.0, 'to': 300.0}, 'weight': {'from': 20.0, 'to': 25.0}, 'dose': 150.0},
    {'ig_level': {'from': 200.0, 'to': 300.0}, 'weight': {'from': 25.0, 'to': 30.0}, 'dose': 150.0},
    {'ig_level': {'from': 200.0, 'to': 300.0}, 'weight': {'from': 30.0, 'to': 40.0}, 'dose': 225.0},
    {'ig_level': {'from': 200.0, 'to': 300.0}, 'weight': {'from': 40.0, 'to': 50.0}, 'dose': 300.0},
    {'ig_level': {'from': 200.0, 'to': 300.0}, 'weight': {'from': 50.0, 'to': 60.0}, 'dose': 300.0},
    {'ig_level': {'from': 200.0, 'to': 300.0}, 'weight': {'from': 60.0, 'to': 70.0}, 'dose': 450.0},
    {'ig_level': {'from': 200.0, 'to': 300.0}, 'weight': {'from': 70.0, 'to': 80.0}, 'dose': 450.0},
    {'ig_level': {'from': 200.0, 'to': 300.0}, 'weight': {'from': 80.0, 'to': 90.0}, 'dose': 450.0},
    {'ig_level': {'from': 200.0, 'to': 300.0}, 'weight': {'from': 90.0, 'to': 125.0}, 'dose': 600.0},

    {'ig_level': {'from': 300.0, 'to': 400.0}, 'weight': {'from': 20.0, 'to': 25.0}, 'dose': 225.0},
    {'ig_level': {'from': 300.0, 'to': 400.0}, 'weight': {'from': 25.0, 'to': 30.0}, 'dose': 225.0},
    {'ig_level': {'from': 300.0, 'to': 400.0}, 'weight': {'from': 30.0, 'to': 40.0}, 'dose': 300.0},
    {'ig_level': {'from': 300.0, 'to': 400.0}, 'weight': {'from': 40.0, 'to': 50.0}, 'dose': 450.0},
    {'ig_level': {'from': 300.0, 'to': 400.0}, 'weight': {'from': 50.0, 'to': 60.0}, 'dose': 450.0},
    {'ig_level': {'from': 300.0, 'to': 400.0}, 'weight': {'from': 60.0, 'to': 70.0}, 'dose': 450.0},
    {'ig_level': {'from': 300.0, 'to': 400.0}, 'weight': {'from': 70.0, 'to': 80.0}, 'dose': 600.0},
    {'ig_level': {'from': 300.0, 'to': 400.0}, 'weight': {'from': 80.0, 'to': 90.0}, 'dose': 600.0},

    {'ig_level': {'from': 400.0, 'to': 500.0}, 'weight': {'from': 20.0, 'to': 25.0}, 'dose': 225.0},
    {'ig_level': {'from': 400.0, 'to': 500.0}, 'weight': {'from': 25.0, 'to': 30.0}, 'dose': 300.0},
    {'ig_level': {'from': 400.0, 'to': 500.0}, 'weight': {'from': 30.0, 'to': 40.0}, 'dose': 450.0},
    {'ig_level': {'from': 400.0, 'to': 500.0}, 'weight': {'from': 40.0, 'to': 50.0}, 'dose': 450.0},
    {'ig_level': {'from': 400.0, 'to': 500.0}, 'weight': {'from': 50.0, 'to': 60.0}, 'dose': 600.0},
    {'ig_level': {'from': 400.0, 'to': 500.0}, 'weight': {'from': 60.0, 'to': 70.0}, 'dose': 600.0},

    {'ig_level': {'from': 500.0, 'to': 600.0}, 'weight': {'from': 20.0, 'to': 25.0}, 'dose': 300.0},
    {'ig_level': {'from': 500.0, 'to': 600.0}, 'weight': {'from': 25.0, 'to': 30.0}, 'dose': 300.0},
    {'ig_level': {'from': 500.0, 'to': 600.0}, 'weight': {'from': 30.0, 'to': 40.0}, 'dose': 450.0},
    {'ig_level': {'from': 500.0, 'to': 600.0}, 'weight': {'from': 40.0, 'to': 50.0}, 'dose': 600.0},
    {'ig_level': {'from': 500.0, 'to': 600.0}, 'weight': {'from': 50.0, 'to': 60.0}, 'dose': 600.0},

    {'ig_level': {'from': 600.0, 'to': 700.0}, 'weight': {'from': 20.0, 'to': 25.0}, 'dose': 300.0},
    {'ig_level': {'from': 600.0, 'to': 700.0}, 'weight': {'from': 30.0, 'to': 40.0}, 'dose': 450.0},
    {'ig_level': {'from': 600.0, 'to': 700.0}, 'weight': {'from': 40.0, 'to': 50.0}, 'dose': 600.0},

]

data2 = [
    # Введение требуется 1 раз в 2 недели
    {'ig_level': {'from': 30.0, 'to': 100.0}, 'weight': {'from': 125.0, 'to': 150.0}, 'dose': 225.0},

    {'ig_level': {'from': 100.0, 'to': 200.0}, 'weight': {'from': 150.0, 'to': 200.0}, 'dose': 375.0},

    {'ig_level': {'from': 200.0, 'to': 300.0}, 'weight': {'from': 125.0, 'to': 150.0}, 'dose': 375.0},
    {'ig_level': {'from': 200.0, 'to': 300.0}, 'weight': {'from': 150.0, 'to': 200.0}, 'dose': 525.0},

    {'ig_level': {'from': 300.0, 'to': 400.0}, 'weight': {'from': 90.0, 'to': 125.0}, 'dose': 450.0},
    {'ig_level': {'from': 300.0, 'to': 400.0}, 'weight': {'from': 125.0, 'to': 150.0}, 'dose': 525.0},

    {'ig_level': {'from': 400.0, 'to': 500.0}, 'weight': {'from': 70.0, 'to': 80.0}, 'dose': 375.0},
    {'ig_level': {'from': 400.0, 'to': 500.0}, 'weight': {'from': 80.0, 'to': 90.0}, 'dose': 375.0},
    {'ig_level': {'from': 400.0, 'to': 500.0}, 'weight': {'from': 90.0, 'to': 125.0}, 'dose': 525.0},
    {'ig_level': {'from': 400.0, 'to': 500.0}, 'weight': {'from': 125.0, 'to': 150.0}, 'dose': 600.0},

    {'ig_level': {'from': 500.0, 'to': 600.0}, 'weight': {'from': 60.0, 'to': 70.0}, 'dose': 375.0},
    {'ig_level': {'from': 500.0, 'to': 600.0}, 'weight': {'from': 70.0, 'to': 80.0}, 'dose': 450.0},
    {'ig_level': {'from': 500.0, 'to': 600.0}, 'weight': {'from': 80.0, 'to': 90.0}, 'dose': 450.0},
    {'ig_level': {'from': 500.0, 'to': 600.0}, 'weight': {'from': 90.0, 'to': 125.0}, 'dose': 600.0},

    {'ig_level': {'from': 600.0, 'to': 700.0}, 'weight': {'from': 25.0, 'to': 30.0}, 'dose': 225.0},
    {'ig_level': {'from': 600.0, 'to': 700.0}, 'weight': {'from': 50.0, 'to': 60.0}, 'dose': 375.0},
    {'ig_level': {'from': 600.0, 'to': 700.0}, 'weight': {'from': 60.0, 'to': 70.0}, 'dose': 450.0},
    {'ig_level': {'from': 600.0, 'to': 700.0}, 'weight': {'from': 70.0, 'to': 80.0}, 'dose': 450.0},
    {'ig_level': {'from': 600.0, 'to': 700.0}, 'weight': {'from': 80.0, 'to': 90.0}, 'dose': 525.0},

    {'ig_level': {'from': 700.0, 'to': 800.0}, 'weight': {'from': 20.0, 'to': 25.0}, 'dose': 225.0},
    {'ig_level': {'from': 700.0, 'to': 800.0}, 'weight': {'from': 25.0, 'to': 30.0}, 'dose': 225.0},
    {'ig_level': {'from': 700.0, 'to': 800.0}, 'weight': {'from': 30.0, 'to': 40.0}, 'dose': 300.0},
    {'ig_level': {'from': 700.0, 'to': 800.0}, 'weight': {'from': 40.0, 'to': 50.0}, 'dose': 375.0},
    {'ig_level': {'from': 700.0, 'to': 800.0}, 'weight': {'from': 50.0, 'to': 60.0}, 'dose': 450.0},
    {'ig_level': {'from': 700.0, 'to': 800.0}, 'weight': {'from': 60.0, 'to': 70.0}, 'dose': 450.0},
    {'ig_level': {'from': 700.0, 'to': 800.0}, 'weight': {'from': 70.0, 'to': 80.0}, 'dose': 525.0},
    {'ig_level': {'from': 700.0, 'to': 800.0}, 'weight': {'from': 80.0, 'to': 90.0}, 'dose': 600.0},

    {'ig_level': {'from': 800.0, 'to': 900.0}, 'weight': {'from': 20.0, 'to': 25.0}, 'dose': 225.0},
    {'ig_level': {'from': 800.0, 'to': 900.0}, 'weight': {'from': 25.0, 'to': 30.0}, 'dose': 225.0},
    {'ig_level': {'from': 800.0, 'to': 900.0}, 'weight': {'from': 30.0, 'to': 40.0}, 'dose': 300.0},
    {'ig_level': {'from': 800.0, 'to': 900.0}, 'weight': {'from': 40.0, 'to': 50.0}, 'dose': 375.0},
    {'ig_level': {'from': 800.0, 'to': 900.0}, 'weight': {'from': 50.0, 'to': 60.0}, 'dose': 450.0},
    {'ig_level': {'from': 800.0, 'to': 900.0}, 'weight': {'from': 60.0, 'to': 70.0}, 'dose': 525.0},
    {'ig_level': {'from': 800.0, 'to': 900.0}, 'weight': {'from': 70.0, 'to': 80.0}, 'dose': 600.0},

    {'ig_level': {'from': 900.0, 'to': 1000.0}, 'weight': {'from': 20.0, 'to': 25.0}, 'dose': 225.0},
    {'ig_level': {'from': 900.0, 'to': 1000.0}, 'weight': {'from': 25.0, 'to': 30.0}, 'dose': 300.0},
    {'ig_level': {'from': 900.0, 'to': 1000.0}, 'weight': {'from': 30.0, 'to': 40.0}, 'dose': 375.0},
    {'ig_level': {'from': 900.0, 'to': 1000.0}, 'weight': {'from': 40.0, 'to': 50.0}, 'dose': 450.0},
    {'ig_level': {'from': 900.0, 'to': 1000.0}, 'weight': {'from': 50.0, 'to': 60.0}, 'dose': 525.0},
    {'ig_level': {'from': 900.0, 'to': 1000.0}, 'weight': {'from': 60.0, 'to': 70.0}, 'dose': 600.0},

    {'ig_level': {'from': 1000.0, 'to': 1100.0}, 'weight': {'from': 20.0, 'to': 25.0}, 'dose': 225.0},
    {'ig_level': {'from': 1000.0, 'to': 1100.0}, 'weight': {'from': 25.0, 'to': 30.0}, 'dose': 300.0},
    {'ig_level': {'from': 1000.0, 'to': 1100.0}, 'weight': {'from': 30.0, 'to': 40.0}, 'dose': 375.0},
    {'ig_level': {'from': 1000.0, 'to': 1100.0}, 'weight': {'from': 40.0, 'to': 50.0}, 'dose': 450.0},
    {'ig_level': {'from': 1000.0, 'to': 1100.0}, 'weight': {'from': 50.0, 'to': 60.0}, 'dose': 600.0},

    {'ig_level': {'from': 1100.0, 'to': 1200.0}, 'weight': {'from': 20.0, 'to': 25.0}, 'dose': 300.0},
    {'ig_level': {'from': 1100.0, 'to': 1200.0}, 'weight': {'from': 25.0, 'to': 30.0}, 'dose': 300.0},
    {'ig_level': {'from': 1100.0, 'to': 1200.0}, 'weight': {'from': 30.0, 'to': 40.0}, 'dose': 450.0},
    {'ig_level': {'from': 1100.0, 'to': 1200.0}, 'weight': {'from': 40.0, 'to': 50.0}, 'dose': 525.0},
    {'ig_level': {'from': 1100.0, 'to': 1200.0}, 'weight': {'from': 50.0, 'to': 60.0}, 'dose': 600.0},

    {'ig_level': {'from': 1200.0, 'to': 1300.0}, 'weight': {'from': 20.0, 'to': 25.0}, 'dose': 300.0},
    {'ig_level': {'from': 1200.0, 'to': 1300.0}, 'weight': {'from': 25.0, 'to': 30.0}, 'dose': 375.0},
    {'ig_level': {'from': 1200.0, 'to': 1300.0}, 'weight': {'from': 30.0, 'to': 40.0}, 'dose': 450.0},
    {'ig_level': {'from': 1200.0, 'to': 1300.0}, 'weight': {'from': 40.0, 'to': 50.0}, 'dose': 525.0},

    {'ig_level': {'from': 1300.0, 'to': 1500.0}, 'weight': {'from': 20.0, 'to': 25.0}, 'dose': 300.0},
    {'ig_level': {'from': 1300.0, 'to': 1500.0}, 'weight': {'from': 25.0, 'to': 30.0}, 'dose': 375.0},
    {'ig_level': {'from': 1300.0, 'to': 1500.0}, 'weight': {'from': 30.0, 'to': 40.0}, 'dose': 525.0},
    {'ig_level': {'from': 1300.0, 'to': 1500.0}, 'weight': {'from': 40.0, 'to': 50.0}, 'dose': 600.0},

]

# Хранилище данных пользователей для расчёта
user_data = {}

#Тело бота
#Приветственное сообщение
@bot.message_handler(commands=['start'])
def welcome_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Новый расчёт")
    markup.add(item1)

    bot.send_message(
        message.chat.id,
        "Добро пожаловать!\nЭтот бот умеет рассчитывать дозу препарата омализумаб для лечения персистирующей атопической бронхиальной астмы у пациентов старше 6 лет.\nИнформация о дозах соответствует инструкциям, зарегистрированным в ГРЛС РФ.\nДля начала нажмите на кнопку: 'Новый расчёт'",
        parse_mode='html',
        reply_markup=markup
    )

#Сбор данный об уровне IgE и весе пациента от пользователя
@bot.message_handler(content_types=['text'])
def handle_text(message):
    chat_id = message.chat.id

    if message.chat.type == 'private':
        if message.text == 'Новый расчёт':
            bot.send_message(chat_id,
                             "Во-первых, укажите исходный уровень IgE (ME/ml) у пациента.\nНапример: 238 или 157.4")
            user_data[chat_id] = {'step': 'ig_level'}

        elif chat_id in user_data and user_data[chat_id].get('step') == 'ig_level':
            try:
                ig_level = float(message.text.replace(',', '.'))
                if ig_level < 30 or ig_level > 1500:
                    bot.send_message(chat_id, "При заданном уровне IgE применение омализумаба не предусмотрено.")
                    user_data.pop(chat_id, None)
                else:
                    user_data[chat_id]['ig_level'] = ig_level
                    user_data[chat_id]['step'] = 'weight'
                    bot.send_message(chat_id, "Во-вторых, укажите вес пациента в килограммах.\nНапример: 70 или 85.5")
            except ValueError:
                bot.send_message(chat_id, "Пожалуйста, введите значение уровня IgE в корректном формате, например: 238")

        elif chat_id in user_data and user_data[chat_id].get('step') == 'weight':
            try:
                weight = float(message.text.replace(',', '.'))
                if weight < 20 or weight > 200:
                    bot.send_message(chat_id,
                                     "При заданном уровне веса пациента применение омализумаба не предусмотрено.")
                    user_data.pop(chat_id, None)
                else:
                    user_data[chat_id]['weight'] = weight

                    # Функция поиска дозы препарата
                    def find_dose(ig_level, weight):
                        for item in data1:  # Сначала проверяем data1
                            ig_range = item['ig_level']
                            weight_range = item['weight']
                            if ig_range['from'] <= ig_level <= ig_range['to'] and weight_range['from'] <= weight <= \
                                    weight_range['to']:
                                return item['dose'], "Вводить подкожно 1 раз в 4 недели."

                        for item in data2:  # Если в data1 не найдено, проверяем data2
                            ig_range = item['ig_level']
                            weight_range = item['weight']
                            if ig_range['from'] <= ig_level <= ig_range['to'] and weight_range['from'] <= weight <= \
                                    weight_range['to']:
                                return item['dose'], "Вводить подкожно 1 раз в 2 недели."

                        return None, None  # Если не найдено ни в одном списке

                    #Отправка результатов поиска дозы пользователю
                    dose, frequency = find_dose(user_data[chat_id]['ig_level'], weight)

                    if dose:
                        bot.send_message(chat_id, f"Рекомендуемая доза омализумаба: {int(dose)} мг.")
                        if frequency:
                            bot.send_message(chat_id, frequency)
                    else:
                        bot.send_message(chat_id,
                                         "К сожалению, подходящей дозировки для указанных параметров не найдено.")

                    user_data.pop(chat_id, None)  # Очистка данных пользователя

            except ValueError:
                bot.send_message(chat_id, "Пожалуйста, введите значение веса в корректном формате, например: 70")

        else:
            bot.send_message(chat_id, 'Нажмите "Новый расчёт", чтобы начать заново.')


# Запуск бота
bot.polling(none_stop=True)
