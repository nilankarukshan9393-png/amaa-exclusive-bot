
import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is missing!")

bot = telebot.TeleBot(TOKEN)

CHANNEL_USERNAME = "@AmaaExclusive"
CHANNEL_LINK = "https://t.me/AmaaExclusive"


def join_keyboard():
    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton(
            "📢 Join Channel",
            url=CHANNEL_LINK
        )
    )

    markup.add(
        InlineKeyboardButton(
            "✅ I Joined",
            callback_data="check_join"
        )
    )

    return markup


@bot.message_handler(commands=["start"])
def start(message):
    text = (
        "🌟 Amaa Exclusive වෙත සාදරයෙන් පිළිගනිමු!\n\n"
        "🔐 ඉදිරියට යාමට අපගේ Channel එකට Join වෙන්න.\n\n"
        "1️⃣ පහත Join Channel Button එක ඔබන්න.\n"
        "2️⃣ Channel එකට Join වෙන්න.\n"
        "3️⃣ නැවත Bot එකට ඇවිත් I Joined ඔබන්න.\n\n"
        "❤️ Thank You!"
    )

    bot.send_message(
        message.chat.id,
        text,
        reply_markup=join_keyboard()
    )


@bot.callback_query_handler(func=lambda call: call.data == "check_join")
def check_join(call):
    user_id = call.from_user.id

    try:
        member = bot.get_chat_member(
            CHANNEL_USERNAME,
            user_id
        )

        if member.status in ["member", "administrator", "creator"]:
            bot.answer_callback_query(
                call.id,
                "✅ Join Verified!"
            )

            bot.send_message(
                call.message.chat.id,
                "🎉 Join Verification Successful!\n\n"
                "❤️ ඔයා Amaa Exclusive Member කෙනෙක්.\n"
                "Access Granted!"
            )

        else:
            bot.answer_callback_query(
                call.id,
                "❌ තවම Channel එකට Join වෙලා නැහැ!",
                show_alert=True
            )

    except Exception:
        bot.answer_callback_query(
            call.id,
            "⚠️ Check කරන්න බැහැ. පසුව නැවත උත්සාහ කරන්න.",
            show_alert=True
        )


print("Amaa Exclusive Bot is running...")

bot.infinity_polling(skip_pending=True)
