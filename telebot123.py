import telebot

from random import randint
import time

TOKEN = '5108975731:AAH-YdBkL16a9MIAL1YPwt7VDn0bx289qBA'
bot = telebot.TeleBot(TOKEN)

emo = {
    1: '❤️', 2: '💋', 3: '🥰', 4: '😘', 5: '😍', 6: '️☺️', 7: '😊', 8: '😻', 9: '👀',
    10: '👩‍❤️‍💋‍👨', 11: '⭐️', 12: '✨', 13: '💫', 14: '🍓', 15: '🌄', 16: '🧡', 17: '💛', 18: '💚', 19: '💙',
    20: '💜', 21: '🖤', 22: '🤍', 23: '🤎', 24: '❤️‍🔥', 25: '❣️', 26: '💕', 27: '💞', 28: '💓', 29: '💗',
    30: '💖', 31: '💘️', 32: '💝', 33: '🔞'
}

love_description = {
    1: f'а я по прежнему люблю тебя{emo[randint(1, 33)]}️',
    2: f'и наша любовь всё ещё не закончилась){emo[randint(1, 33)]}',
    3: f'но я бы тебя сейчас поцеловал{emo[randint(1, 33)]}',
    4: f'в это мгновение мы как-то были вместе, однако оно не последнее{emo[randint(1, 33)]}',
    5: f'а в тебя начинают стрелять: пиу-пиу-пиу, обстрел из поцелуйчиков поразил тебя{emo[randint(1, 33)]}',
    6: f'однако это не имеет значения, моё сердце занято тобой в любое время суток{emo[randint(1, 33)]}',
    7: f'и даже в эту секунду у нас есть с тобой общее счастливое воспоминание{emo[randint(1, 33)]}',
    8: f'а твоя улыбка готова хоть сейчас сразить меня с ног{emo[randint(1, 33)]}',
    9: f'но мне бы сейчас не помешал твой прекрасный поцелуй{emo[randint(1, 33)]}',
    10: f'но для нас время слишком ничтожно, ведь когда мы рядом, оно летит слишком незментно{emo[randint(1, 33)]}'
}

love_picture = {
    1: f'Самые счастливые{emo[randint(1, 33)]}',
    2: f'И в мыслях у каждого из нас "вечность и ещё чуть-чуть"{emo[randint(1, 33)]}',
    3: f'Всегда будем друг рядом с другом{emo[randint(1, 33)]}',
    4: f'А ведь мы могли и не встретиться… И блуждали бы по миру две одинокие половинки{emo[randint(1, 33)]}',
    5: f'Твои объятия — мое любимое место на земле!{emo[randint(1, 33)]}',
    6: f'Каждая история любви прекрасна, но наша — самая лучшая{emo[randint(1, 33)]}',
    7: f'Твоя улыбка не способна изменить мир, но она изменила меня{emo[randint(1, 33)]}',
    8: f'Кто знал, что этот момент станет одним из моих самых любимых?{emo[randint(1, 33)]}',
    9: f'Мы здесь такие же милые, как и всегда{emo[randint(1, 33)]}',
    10: f'Мне нравится пересматривать прошлое, но будущее — это то, что меня больше всего радует вместе с тобой{emo[randint(1, 33)]}',
    11: f'Первый наш поцелуй забыть просто невозможно{emo[randint(1, 33)]}',
    12: f'Вся моя скромность постепенно тухла при виде тебя{emo[randint(1, 33)]}',
    13: f'Ты мой счастливый лотерейный билет{emo[randint(1, 33)]}',
    14: f'Мгновения, которые хочется запомнить на всю жизнь{emo[randint(1, 33)]}',
    15: f'Мое сердечко твое навсегда!{emo[randint(1, 33)]}',
    16: f'Понятия не имею, как я умудрился найти любовь всей жизни{emo[randint(1, 33)]}',
    17: f'Я меняюсь, ты меняешься, но наша любовь остаётся{emo[randint(1, 33)]}'
}

love_ignor = {
    1: 'Он просил передать: "Я чуть-чуть занят, но обязательно тебе отвечу солнышко"',
    2: 'Я пожалуй просто процитирую его: "Ни с кем другим я не нахожусь, мне нужна тольно ты, скоро буду)"',
    3: 'Твой дурачёк наверное забыл включить уведомления на телефоне, не переживай, скоро ответит',
    4: 'Ух ты глупый робот я.... Я забыл передать его сообщение: "Прости, что не отвечаю,'
       ' я обязательно скоро исправлюсь пупсик"',
    5: 'Если честно, я без понятния почему этот паренёк тебе не может ответить,'
       ' но я ему доверяю, так что не переживай, скоро он будет перед тобой извиняться',
    6: 'Мда, он местами похож на эгоиста, но не обращай сильно на это внимания, он всё равно тебя любит',
    7: 'Он до сих пор не ответил? Боже да он с этими играми надоест любому... но ты обязательно дождешься!)',
    8: 'Я хоть и робот, но понимаю, что тебе не нужны эти абьюзивные отношения',
    9: 'Может он просто дал храпу и забыл тебе написать? Я не уверяю, но вполне вероятно',
    10: 'Вообще он меня создал, поэтому я попробую оправдать его и сказать, что он не специально,'
        ' так что не грусти, скоро он осознает, что оставил тебя одну',
    11: 'Да, я согласен, давай сойдёмся на том, что он охренел',
    12: 'У него залагало реально, сейчас обязательно ответит.',
    13: 'Я не уверен, но вполне возможно, что он расслабляется, так что подожди 2 минутки',
    14: 'Каждый раз когда ты это спрашиваешь, я его защищаю, а я устал между прочим....',
    15: 'Есть вероятность, что он разговаривает с мамой или она его отвлекает, скоро он будет на метсе',
    16: 'Он греет себе еду наверное, он жрёт немеренно, так что сейчас принесёт тарелочку с едой за компьютер и ответит'
}

skazka1 = telebot.types.KeyboardButton("Рапунцель")
skazka2 = telebot.types.KeyboardButton("Кот в сапогах")
skazka3 = telebot.types.KeyboardButton("Маша и медведь")
skazka4 = telebot.types.KeyboardButton("Волк и семеро козлят")
skazka5 = telebot.types.KeyboardButton("Маленькие человечки")
skazka6 = telebot.types.KeyboardButton("Золотая рыбка")
skazka7 = telebot.types.KeyboardButton("Спящая красавица")
skazka8 = telebot.types.KeyboardButton("Король-лягушонок")
skazka9 = telebot.types.KeyboardButton("Лесная старуха")
skazka10 = telebot.types.KeyboardButton("Сивка-бурка")


@bot.message_handler(commands=['начало'])
def start_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("Напоминание")
    btn2 = telebot.types.KeyboardButton("Мы")
    btn3 = telebot.types.KeyboardButton("Игнорщик")
    btn4 = telebot.types.KeyboardButton("Сказки ч.1")
    btn5 = telebot.types.KeyboardButton("Сказки ч.2")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, text="Это мои функции👀", reply_markup=markup)


@bot.message_handler(commands=['text'])
def returned(message):
    btn1 = telebot.types.KeyboardButton("Напоминание")
    btn2 = telebot.types.KeyboardButton("Мы")
    btn3 = telebot.types.KeyboardButton("Игнорщик")
    btn4 = telebot.types.KeyboardButton("Сказки ч.1")
    btn5 = telebot.types.KeyboardButton("Сказки ч.2")
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, text='Возвращаюсь к функциям👀', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Напоминание":
        bot.send_message(message.from_user.id,
                         f"На часах {time.asctime().split()[3]}, {love_description[randint(1, 10)]}")
    elif message.text == "Мы":
        bot.send_photo(message.from_user.id, open(f'img/{randint(1, 27)}.jpg', 'rb'))
        bot.send_message(message.from_user.id, {love_picture[randint(1, 17)]})
    elif message.text == "Игнорщик":
        bot.send_message(message.from_user.id, {love_ignor[randint(1, 16)]})
    elif message.text == "Сказки ч.1":
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(skazka1, skazka2, skazka3, skazka4, skazka5, skazka6)
        bot.send_message(message.chat.id, text="Сказки на выбор☺️", reply_markup=markup)
    elif message.text == "Сказки ч.2":
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(skazka7, skazka8, skazka9, skazka10)
        bot.send_message(message.chat.id, text="Сказки на выбор☺️", reply_markup=markup)
    elif message.text == "Рапунцель":
        bot.send_audio(message.from_user.id, open('audio/skazka/Рапунцель.mp3', 'rb'))
        returned(message)
        bot.se
    elif message.text == "Кот в сапогах":
        bot.send_audio(message.from_user.id, open('audio/skazka/Кот в сапогах.mp3', 'rb'))
        returned(message)
    elif message.text == "Маша и медведь":
        bot.send_audio(message.from_user.id, open('audio/skazka/Маша и Медведь.mp3', 'rb'))
        returned(message)
    elif message.text == "Волк и семеро козлят":
        bot.send_audio(message.from_user.id, open('audio/skazka/Волк и семеро козлят.mp3', 'rb'))
        returned(message)
    elif message.text == "Маленькие человечки":
        bot.send_audio(message.from_user.id, open('audio/skazka/Маленькие человечки.mp3', 'rb'))
        returned(message)
    elif message.text == "Золотая рыбка":
        bot.send_audio(message.from_user.id, open('audio/skazka/Золотая рыбка.mp3', 'rb'))
        returned(message)
    elif message.text == "Спящая красавица":
        bot.send_audio(message.from_user.id, open('audio/skazka/Спящая красавица.mp3', 'rb'))
        returned(message)
    elif message.text == "Король-лягушонок":
        bot.send_audio(message.from_user.id, open('audio/skazka/Король-лягушонок.mp3', 'rb'))
        returned(message)
    elif message.text == "Лесная старуха":
        bot.send_audio(message.from_user.id, open('audio/skazka/Лесная старуха.mp3', 'rb'))
        returned(message)
    elif message.text == "Сивка-бурка":
        bot.send_audio(message.from_user.id, open('audio/skazka/Сивка-бурка.mp3', 'rb'))
        returned(message)
    else:
        bot.send_message(message.from_user.id, 'Ванечка не ожидал, что будут просить такое😱😨🤔')


bot.polling(none_stop=True, interval=0)
