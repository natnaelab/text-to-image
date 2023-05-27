from telegram import Update
from telegram.ext import CallbackContext, MessageHandler, Filters, DispatcherHandlerStop


def img(update: Update, context: CallbackContext):
    txt = update.message.text.split(" ")

    if len(txt) <= 1:
        update.message.reply_text("Invalid prompt")
        raise DispatcherHandlerStop
    
    prompt = txt[1]

    update.message.reply_text('generating ' + prompt)


img_handler = MessageHandler(Filters.command & Filters.regex('^/img'), img)
