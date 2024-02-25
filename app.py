import telebot
import time

# Token do seu bot
TOKEN = '6788247666:AAE_9h3yeE6uRHz__MnJs5UXBsbtR4pj1JA'

# Criação do objeto bot
bot = telebot.TeleBot(TOKEN)

# Função para enviar mensagem no grupo a cada 5 segundos
def enviar_mensagem():
    while True:
        try:
            # Substitua o ID do grupo (-4195474080) pelo ID do grupo que deseja enviar a mensagem
            bot.send_message(-4195474080, "Sua mensagem aqui")
            print("Mensagem enviada com sucesso")
        except Exception as e:
            print(f"Erro ao enviar mensagem: {e}")
        time.sleep(1)

# Iniciar o envio de mensagens
enviar_mensagem()
