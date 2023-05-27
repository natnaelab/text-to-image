from telegram import Update
from telegram.ext import CallbackContext, MessageHandler, Filters


def help(update: Update, context: CallbackContext):
    update.message.reply_text('help')


help_handler = MessageHandler(Filters.command & Filters.regex('^/start'), help)
