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
selahzar_telegram_bot_token = 'YOUR_BOT_TOKEN_HERE'
bot = telebot.TeleBot(selahzar_telegram_bot_token)

# Função para visitar o site e mantê-lo ativo
def keep_bot_active():
    url = "https://selahzar-1.onrender.com/"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers)
        print(f"Site visited with status code: {response.status_code} at every 1 minute")
    except Exception as e:
        print(f"Failed to visit site: {e}")
    # Agendar a próxima verificação para 1 minuto depois
    threading.Timer(60, keep_bot_active).start()

# Comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    instagram_button = types.InlineKeyboardButton("Instagram", url="https://instagram.com")
    markup.add(instagram_button)
    bot.send_message(message.chat.id, "Bem-vindo ao bot da Selahzar S.A! Clique abaixo para nos visitar no Instagram. Selahzar!!!", reply_markup=markup)

# Iniciar a função de manter ativo
keep_bot_active()

# Tentativa de manter o bot rodando e lidar com exceções
try:
    bot.infinity_polling()
except telebot.apihelper.ApiTelegramException as e:
    print(f"Erro detectado: {e}")