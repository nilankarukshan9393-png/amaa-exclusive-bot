import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "YOUR_BOT_TOKEN"

bot = telebot.TeleBot(TOKEN)

CHANNEL_LINK = "https://t.me/AmaaExclusive"

@bot.message_handler(commands=['start'])
def start(message):
    text = (
        "🌟 ආයුබෝවන්!\n\n"
        "Amaa Exclusive වෙත සාදරයෙන් පිළිගනිමු. ❤️\n\n"
        "📢 පියවර 01:\n"
        "අපගේ Channel Link එක Groups 5කට Share කරන්න.\n\n"
        "🔓 පියවර 02:\n"
        "Share කිරීමෙන් පසු පහත Button එක ඔබන්න."
    )

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(
        "📢 Channel Link Share කරන්න",
        url="https://t.me/share/url?url=https%3A%2F%2Ft.me%2FAmaaExclusive"
    ))
    markup.add(InlineKeyboardButton(
        "🔓 Channel එකට යන්න",
        url=CHANNEL_LINK
    ))

    bot.send_message(message.chat.id, text, reply_markup=markup)

bot.infinity_polling()
