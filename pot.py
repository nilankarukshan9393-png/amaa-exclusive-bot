
import os
import time
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is missing!")

bot = telebot.TeleBot(TOKEN)

# මුලින් Public Channel එක තිබියදී ID එක ලබාගන්න
CHANNEL_ID = "@AmaaExclusive"

SHARE_LINK = (
    "https://t.me/share/url"
    "?url=https%3A%2F%2Ft.me%2FAmaaExclusive"
    "&text=Join%20Amaa%20Exclusive"
)


def start_keyboard():
    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton(
            "📤 Groups 3කට Share කරන්න",
            url=SHARE_LINK
        )
    )

    markup.add(
        InlineKeyboardButton(
            "✅ I Shared",
            callback_data="shared"
        )
    )

    return markup


def join_keyboard(link):
    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton(
            "🔓 Join Amaa Exclusive",
            url=link
        )
    )

    markup.add(
        InlineKeyboardButton(
            "✅ I Joined",
            callback_data="check_join"
        )
    )

    return markup


@bot.message_handler(commands=["getid"])
def get_channel_id(message):
    try:
        chat = bot.get_chat("@AmaaExclusive")
        bot.send_message(
            message.chat.id,
            f"Channel ID: {chat.id}"
        )
    except Exception as e:
        bot.send_message(
            message.chat.id,
            f"Error: {e}"
        )


@bot.message_handler(commands=["start"])
def start(message):

    text = (
        "🌟 ආයුබෝවන්!\n\n"
        "Amaa Exclusive වෙත සාදරයෙන් පිළිගනිමු. ❤️\n\n"
        "📢 පියවර 01:\n"
        "අපගේ Channel Link එක Groups 3කට Share කරන්න.\n\n"
        "🔓 පියවර 02:\n"
        "Share කළ පසු I Shared Button එක ඔබන්න.\n\n"
        "❤️ Amaa Exclusive සමඟ එකතු වෙන්න!"
    )

    bot.send_message(
        message.chat.id,
        text,
        reply_markup=start_keyboard()
    )


@bot.callback_query_handler(
    func=lambda call: call.data == "shared"
)
def shared(call):

    try:
        invite = bot.create_chat_invite_link(
            chat_id=CHANNEL_ID,
            member_limit=1,
            expire_date=int(time.time()) + 600
        )

        bot.answer_callback_query(
            call.id,
            "Invite Link Ready!"
        )

        bot.send_message(
            call.message.chat.id,
            "🎉 Unlock Link එක සූදානම්!\n\n"
            "පහත Button එකෙන් Channel එකට Join වෙන්න.",
            reply_markup=join_keyboard(invite.invite_link)
        )

    except Exception as e:
        print("Invite Error:", e)

        bot.answer_callback_query(
            call.id,
            "⚠️ Invite Link එක ලබාගන්න බැහැ.",
            show_alert=True
        )


@bot.callback_query_handler(
    func=lambda call: call.data == "check_join"
)
def check_join(call):

    try:
        member = bot.get_chat_member(
            CHANNEL_ID,
            call.from_user.id
        )

        joined = (
            member.status in ["member", "administrator", "creator"]
            or (
                member.status == "restricted"
                and getattr(member, "is_member", False)
            )
        )

        if joined:

            bot.answer_callback_query(
                call.id,
                "✅ Verification Successful!"
            )

            bot.send_message(
                call.message.chat.id,
                "🎉 ACCESS GRANTED!\n\n"
                "❤️ ඔයා දැන් Amaa Exclusive Member කෙනෙක්."
            )

        else:

            bot.answer_callback_query(
                call.id,
                "❌ මුලින් Channel එකට Join වෙන්න!",
                show_alert=True
            )

    except Exception as e:
        print("Verification Error:", e)

        bot.answer_callback_query(
            call.id,
            "⚠️ නැවත උත්සාහ කරන්න.",
            show_alert=True
        )


print("Amaa Exclusive Bot is running...")

bot.infinity_polling(skip_pending=True)


