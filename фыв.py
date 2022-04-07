import telebot

from random import randint, choice
import time

TOKEN = '5108975731:AAH-YdBkL16a9MIAL1YPwt7VDn0bx289qBA'
bot = telebot.TeleBot(TOKEN)

love_description = {
    1: 'а я по прежнему люблю тебя',
    2: 'и наша любовь всё ещё не закончилась)',
    3: 'но я бы тебя сейчас поцеловал'
}

love_picture = {
    1: 'Самые счастливые',
    2: 'И в мыслях у каждого из нас "вечность и ещё чуть-чуть"',
    3: 'Всегда будем друг рядом с другом'
}

love_ignor = {
    1: 'Я чуть-чуть занят, но обязательно тебе отвечу солнышко',
    2: 'Ни с кем другим я не нахожусь, мне нужна тольно ты, скоро буду)',
    3: 'Твой дурачёк наверное забыл включить уведомления на телефоне, не переживай, скоро ответит'
}


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет любимая, этот робот будет заменять меня, пока я остутствую <3")
    bot.send_message(message.chat.id, "Доступные для тебя команды:")
    bot.send_message(message.chat.id, "Напоминание / Фото / Игнорщик / Послушать")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Напоминание":
        bot.send_message(message.from_user.id,
                         f"На часах {time.asctime().split()[3]}, {love_description[randint(1, 3)]}")
    elif message.text == "Фото":
        bot.send_photo(message.from_user.id, open(f'img/{randint(1, 4)}.jpg', 'rb'))
        bot.send_message(message.from_user.id, {love_picture[randint(1, 3)]})
    elif message.text == "Игнорщик":
        bot.send_message(message.from_user.id, {love_ignor[randint(1, 3)]})
    elif message.text == "Послушать":
        bot.send_audio(message.from_user.id, open(f'audio/{randint(1, 1)}.mp3', 'rb'))
    else:
        bot.send_message(message.from_user.id, 'я такого не умею!!!!!')


bot.polling(none_stop=True, interval=0)
