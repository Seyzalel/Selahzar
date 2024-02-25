from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackContext
import logging

# Insira o ID do seu grupo aqui
GROUP_CHAT_ID = -4195474080

# Token do bot fornecido pelo BotFather
TOKEN = "6788247666:AAE_9h3yeE6uRHz__MnJs5UXBsbtR4pj1JA"

# Configuração básica do logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello World, Selahzar!")

async def keep_alive(context: CallbackContext) -> None:
    """Função para enviar uma mensagem periódica e manter o bot ativo."""
    bot = context.bot
    await bot.send_message(chat_id=GROUP_CHAT_ID, text="Keep-alive message")

def main() -> None:
    # Cria uma instância do Application usando o token do bot
    application = Application.builder().token(TOKEN).build()

    # Adiciona o manipulador do comando /start
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    # Adiciona a tarefa de keep-alive para ser executada a cada 5 minutos
    application.job_queue.run_repeating(keep_alive, interval=30, first=0)

    # Inicia o bot
    application.run_polling()

if __name__ == '__main__':
    main()
