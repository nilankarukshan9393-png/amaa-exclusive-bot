

import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is missing!")

bot = telebot.TeleBot(TOKEN)

CHANNEL_USERNAME = "@AmaaExclusive"
CHANNEL_LINK = "https://t.me/AmaaExclusive"

SHARE_LINK = (
    "https://t.me/share/url"
    "?url=https%3A%2F%2Ft.me%2FAmaaExclusive"
    "&text=Amaa%20Exclusive%20Channel"
)


def main_keyboard():
    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton(
            "📤 Groups 3කට Share කරන්න",
            url=SHARE_LINK
        )
    )

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
        "🌟 ආයුබෝවන්!\n\n"
        "Amaa Exclusive වෙත සාදරයෙන් පිළිගනිමු. ❤️\n\n"
        "📢 පියවර 01:\n"
        "අපගේ Channel Link එක Groups 3කට Share කරන්න.\n\n"
        "🔓 පියවර 02:\n"
        "පහත Button එක ඔබලා Channel එකට Join වෙන්න.\n\n"
        "✅ පියවර 03:\n"
        "Join වූ පසු I Joined Button එක ඔබන්න.\n\n"
        "❤️ Amaa Exclusive සමඟ එකතු වෙන්න!"
    )

    bot.send_message(
        message.chat.id,
        text,
        reply_markup=main_keyboard()
    )


@bot.callback_query_handler(
    func=lambda call: call.data == "check_join"
)
def check_join(call):

    user_id = call.from_user.id

    try:
        member = bot.get_chat_member(
            CHANNEL_USERNAME,
            user_id
        )

        if member.status in [
            "member",
            "administrator",
            "creator"
        ]:

            bot.answer_callback_query(
                call.id,
                "✅ Join Verified!"
            )

            bot.send_message(
                call.message.chat.id,
                "🎉 Verification Successful!\n\n"
                "❤️ ඔයා Amaa Exclusive Member කෙනෙක්.\n\n"
                "🔓 Access Granted!"
            )

        else:

            bot.answer_callback_query(
                call.id,
                "❌ මුලින් Channel එකට Join වෙන්න!",
                show_alert=True
            )

    except Exception as error:

        print("Verification Error:", error)

        bot.answer_callback_query(
            call.id,
            "⚠️ නැවත උත්සාහ කරන්න.",
            show_alert=True
        )


print("Amaa Exclusive Bot is running...")

bot.infinity_polling(skip_pending=True)
