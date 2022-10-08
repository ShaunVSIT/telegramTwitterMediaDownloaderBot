import constants as keys
from telegram.ext import *

print("Bot Started")


def start_command(update, context):
    update.message.reply_text('Please enter Tweet URL containing video')


def handle_message(update, context):
    text = str(update.message.text)


def error(update, context):
    print(f"Update {update} caused error {context.error})")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    # dp.add_handler(CommandHandler("help", help_command))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
