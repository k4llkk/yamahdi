import random
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot('6387632922:AAFHZLAxufgGRByVOxpb2FEhJNhhwcKakj8')

game_active = False
number = None
max_attempts = 3
attempts = 0

@bot.message_handler(commands=['start'])
def start(message):
    global game_active, attempts
    game_active = False
    attempts = 0

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("ابدأ اللعبة", callback_data="start_game"))
    bot.send_message(message.chat.id, 'اهلاً حياك الله! اضغط على الزر لبدء اللعبة.', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "start_game")
def start_game(call):
    global game_active, number, attempts
    if not game_active:
        number = random.randint(1, 10)
        bot.send_message(call.message.chat.id, 'اختر أي رقم من 1 إلى 10 🌚 ')
        game_active = True
        attempts = 0
    else:
        bot.send_message(call.message.chat.id, 'اللعبة قيد التشغيل، يرجى انتهاء الجولة الحالية أولاً.')

@bot.message_handler(func=lambda message: game_active)
def handle_guess(message):
    global game_active, number, attempts
    try:
        guess = int(message.text)
        attempts += 1

        if guess == number:
            bot.send_message(message.chat.id, "مُبارك فزتها بفخر 🥳")
            won = "https://t.me/VIPABH/2"

            bot.send_video(message.chat.id, won)
            game_active = False
        elif attempts >= max_attempts:
            bot.send_message(message.chat.id, f"للأسف، لقد نفدت محاولاتك. الرقم الصحيح هو {number}.🌚",)
            lose = "https://t.me/VIPABH/23"
            bot.send_video(message.chat.id, lose)

            game_active = False
        else:


            bot.send_message(message.chat.id, f"جرب مرة لخ، الرقم غلط💔باقي لك {abs(attempts - max_attempts)} فرص")


    except ValueError:
        bot.send_message(message.chat.id, "يرجى إدخال رقم صحيح")

bot.polling()
