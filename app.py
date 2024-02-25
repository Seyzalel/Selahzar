# Importando as bibliotecas necessárias
import telebot
from telebot import types, apihelper

# Direitos reservados 2024, Empresa Selahzar S.A.
__author__ = "Selahzar S.A."
__copyright__ = "2024 Selahzar S.A."
__license__ = "Private"
__version__ = "1.0"

# Token do bot
selahzar_telegram_bot_token = 'YOUR_BOT_TOKEN_HERE'
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

# Tentativa de manter o bot rodando e lidar com exceções
try:
    bot.infinity_polling()
except apihelper.ApiTelegramException as e:
    print(f"Erro detectado: {e}")
    # Lógica adicional para lidar com o erro ou reiniciar o bot pode ser adicionada aqui.