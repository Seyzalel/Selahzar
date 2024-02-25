import telebot
from telebot import types
import time

# Substitua 'SEU_TOKEN_AQUI' pelo token do seu bot
TOKEN = '6788247666:AAE_9h3yeE6uRHz__MnJs5UXBsbtR4pj1JA'
bot = telebot.TeleBot(TOKEN)

# Handler para o comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Selahzar, Welcome To!")

# Função para enviar mensagem periodicamente (não recomendado para uso com o comando /start)
def send_periodic_message():
    while True:
        bot.send_message(-4195474080, "Mensagem periódica do bot")
        time.sleep(60)  # Espera 60 segundos antes de enviar a próxima mensagem

if __name__ == '__main__':
    # Começa a escutar mensagens
    bot.polling()

    # Para enviar mensagens periódicas, você precisaria de uma abordagem diferente,
    # pois bot.polling() é um loop de escuta que bloqueia a thread principal.
