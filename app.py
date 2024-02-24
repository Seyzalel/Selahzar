import telebot
from telebot import types
import requests
import threading

# Direitos reservados 2024, Empresa Selahzar S.A.
__author__ = "Selahzar S.A."
__copyright__ = "2024 Selahzar S.A."
__license__ = "Private"
__version__ = "1.0"

# Token do bot
selahzar_telegram_bot_token = '6788247666:AAE_9h3yeE6uRHz__MnJs5UXBsbtR4pj1JA'
bot = telebot.TeleBot(selahzar_telegram_bot_token)

# Função para visitar o site
def visit_site():
    url = "https://selahzar-1.onrender.com/"
    headers = {"User-Agent": "KeepAliveAgent"}
    try:
        response = requests.get(url, headers=headers)
        print(f"Site visited with status code: {response.status_code}")
    except Exception as e:
        print(f"Failed to visit site: {e}")
    # Agendar a próxima visita
    threading.Timer(7, visit_site).start()

# Comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    instagram_button = types.InlineKeyboardButton("Instagram", url="https://instagram.com")
    markup.add(instagram_button)
    bot.send_message(message.chat.id, "Bem-vindo ao bot da Selahzar S.A.! Clique abaixo para nos visitar no Instagram.", reply_markup=markup)

# Iniciar a visita ao site
visit_site()

# Tentativa de manter o bot rodando e lidar com exceções
try:
    bot.infinity_polling()
except telebot.apihelper.ApiTelegramException as e:
    print(f"Erro detectado: {e}")