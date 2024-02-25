from telegram.ext import Updater, CommandHandler

# Função para responder ao comando /start
def start(update, context):
    # Enviar a mensagem "Hello World!"
    update.message.reply_text('Hello World!')

def main():
    # Inicializar o updater com o token do seu bot
    updater = Updater("INSIRA_SEU_TOKEN_AQUI", use_context=True)

    # Obter o despachante para registrar os manipuladores
    dp = updater.dispatcher

    # Adicionar um manipulador para o comando /start
    dp.add_handler(CommandHandler("start", start))

    # Iniciar o bot
    updater.start_polling()

    # Manter o bot em execução até que Ctrl + C seja pressionado
    updater.idle()

if __name__ == '__main__':
    main()
