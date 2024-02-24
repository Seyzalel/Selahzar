import telebot
from telebot import types

# Direitos reservados 2024, Empresa Selahzar S.A.
__author__ = "Selahzar S.A."
__copyright__ = "2024 Selahzar S.A."
__license__ = "Private"
__version__ = "1.0"

# Token do bot
selahzar_telegram_bot_token = '6788247666:AAE_9h3yeE6uRHz__MnJs5UXBsbtR4pj1JA'
bot = telebot.TeleBot(selahzar_telegram_bot_token)

# Comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Criando o botão
    markup = types.InlineKeyboardMarkup()
    instagram_button = types.InlineKeyboardButton("Instagram", url="https://instagram.com")
    markup.add(instagram_button)

    # Enviando a mensagem com o botão
    bot.send_message(message.chat.id, "Bem-vindo ao bot da Selahzar S.A.! Clique abaixo para nos visitar no Instagram.", reply_markup=markup)

# Mantém o bot rodando
bot.infinity_polling()