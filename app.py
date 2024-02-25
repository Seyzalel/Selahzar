from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello World")

def main() -> None:
    application = Application.builder().token('6788247666:AAE_9h3yeE6uRHz__MnJs5UXBsbtR4pj1JA').build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()

if __name__ == '__main__':
    main()
