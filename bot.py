import telebot
import random
import time

TOKEN ="8510465911:AAGGYvP37lfTWPvf_AbBTFBFgwHuJQbULwA"

bot = telebot.TeleBot(TOKEN)

pairs = [
    "EURUSD-OTC",
    "GBPUSD-OTC",
    "USDJPY-OTC",
    "AUDUSD-OTC",
    "EURJPY-OTC"
]

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "🤖 أهلا! بوت إشارات Pocket Option OTC جاهز.\n\n"
        "استعملي /signal للحصول على إشارة."
    )

@bot.message_handler(commands=["signal"])
def signal(message):
    pair = random.choice(pairs)
    direction = random.choice(["CALL ⬆️", "PUT ⬇️"])

    text = (
        "🛰 POCKET OPTION [M1]\n\n"
        f"💷 {pair}\n"
        "💎 1 min\n"
        f"🔔 {direction}\n\n"
        "⚠️ إشارة تجريبية وليست ضمانًا للربح."
    )

    bot.send_message(message.chat.id, text)

bot.infinity_polling()
