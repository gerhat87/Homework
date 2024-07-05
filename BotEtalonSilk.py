import telebot
import time
import memcache
import requests

TOKEN = '6869186963:AAHv-mR6oafJTP5A-9LI0rMUAHvCBTJNQvg'
bot = telebot.TeleBot(TOKEN)

# Подключение к memcached
mc = memcache.Client(['127.0.0.1:11211'], debug=True)

def get_weather(city):
    # Формирование ключа кеша
    cache_key = f'weather_{city}'

    # Проверка наличия данных в кеше
    cached_data = mc.get(cache_key)

    if cached_data:
        # Возвращаем данные из кеша
        print(f'Using cached data for {city}')
        return cached_data

    # Запрос к API
    response = requests.get(f'https://api.example.com/weather?city={city}')
    weather_data = response.json()

    # Сохранение данных в кеше
    mc.set(cache_key, weather_data, 600)  # 10 минут ~ 600 секунд

    return weather_data

def start_message(message):
    bot.send_message(message.chat.id, "Привет! Меня зовут Юлия, я эксперт в области изготовления шёлковых изделий! Я приглашаю порадовать себя чем-то особенным!\n"
                                      "Давайте знакомиться! Как можно к Вам обращаться?")
    bot.register_next_step_handler(message, get_name)

def get_name(message):
    name = message.text
    bot.send_message(message.chat.id, f"Приятно познакомиться, {name}! Что Вас интересует? Выбирайте!")
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add("Мужская одежда", "Женская одежда", "Одеяла", "Подушки", "Наматрасники", "Постельное белье", "Аксессуары", "Пледы")
    bot.send_message(message.chat.id, "Выберите категорию", reply_markup=keyboard)
    bot.register_next_step_handler(message, get_category)

def get_category(message):
    bot.send_message(message.chat.id, "Используя сайт https://etalonsilk.ru/, уточните наименование, размеры, цвет и другие характеристики и напишите в чате Ваши предпочтения")
    bot.register_next_step_handler(message, get_preferences)

def get_preferences(message):
    bot.send_message(message.chat.id, "Вы хотите приехать в шоурум или получить консультацию от эксперта потелефону?")
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add("Приехать в шоурум", "Получить консультацию по телефону")
    bot.send_message(message.chat.id, "Выберите вариант", reply_markup=keyboard)
    bot.register_next_step_handler(message, get_choice)

def get_choice(message):
    if message.text == "Приехать в шоурум":
        bot.send_message(message.chat.id, "Мы находимся по адресу: м.Белорусская, ул. Малая Грузинская 54 оф. 715, с 10 до 21 часа в любой день будем рады Вам!\n"
                                          "Более подробная информация на сайте: https://etalonsilk.ru/")
        time.sleep(2)
        bot.send_message(message.chat.id, "В какой день и время Вам было бы удобно подъехать?")
        bot.register_next_step_handler(message, get_schedule)
    elif message.text == "Получить консультацию по телефону":
        bot.send_message(message.chat.id, "Ждем Вашего звонка по номеру телефона: +79161768947 (Юлия).\n"
                                          "Более подробная информация на сайте: https://etalonsilk.ru/")
    else:
        bot.send_message(message.chat.id, "Выберите один из предложенных вариантов")
        bot.register_next_step_handler(message, get_choice)

def get_schedule(message):
    bot.send_message(message.chat.id, "Отлично! В ближайшее время менеджер свяжется с Вами. Наш номер телефона:"
                                      " +79161768947")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    start_message(message)

bot.polling()