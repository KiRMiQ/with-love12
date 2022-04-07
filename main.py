# Импортируем необходимые классы.
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, updater
import time
from random import randint
from glob import glob
from random import choice
import telebot123

bot = telebot123.bot()

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id


TOKEN = '5108975731:AAH-YdBkL16a9MIAL1YPwt7VDn0bx289qBA'
updater = Updater(token=TOKEN)
timeset = time.asctime()
img = open('img/1.jpg')
love_description = {
    1: 'а я по прежнему люблю тебя',
    2: 'и наша любовь всё ещё не закончилась)',
    3: 'но я бы тебя сейчас поцеловал'
}

love_picture = {
    1: ''
}


def love(update, context):
    update.message.reply_text(f"На часах {time.asctime().split()[3]}, {love_description[randint(1, 3)]}")


def love_pic(bot, context):
    bot.send_photo(chat_id=user_id, open('/путь/к/картинке.jpg', 'rb'));


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("love", love))
    dp.add_handler(CommandHandler("love_pic", love_pic))
    updater.start_polling()
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
