from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, JobQueue

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello World")

async def keep_alive(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Função para enviar uma mensagem periódica e manter o bot ativo."""
    await context.bot.send_message(chat_id='-4195474080', text="Keep-alive message")

def main() -> None:
    application = Application.builder().token('6788247666:AAE_9h3yeE6uRHz__MnJs5UXBsbtR4pj1JA').build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    # Adiciona a tarefa de keep-alive para ser executada a cada 5 minutos
    jq = application.job_queue
    jq.run_repeating(keep_alive, interval=300, first=0)

    application.run_polling()

if __name__ == '__main__':
    main()
