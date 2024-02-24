import telebot

TOKEN = '6788247666:AAE_9h3yeE6uRHz__MnJs5UXBsbtR4pj1JA'  # Substitua YOUR_TOKEN_HERE pelo token fornecido pelo BotFather
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    username = message.from_user.username
    bot.reply_to(message, f"Hello, @{username}")

bot.polling()