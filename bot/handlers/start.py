from telegram import Update
from telegram.ext import CallbackContext, MessageHandler, Filters


def start(update: Update, context: CallbackContext):
    update.message.reply_text('hello')


start_handler = MessageHandler(Filters.command & Filters.regex('^/start'), start)
