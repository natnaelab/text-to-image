from telegram import Update
from telegram.ext import CallbackContext, MessageHandler, Filters


def start(update: Update, context: CallbackContext):
    text = """
👋 Welcome to the Text-to-Image Generator Bot! 👩‍💻🖼️

I'm here to help you transform your text into beautiful images! Simply type in your desired text, and I'll generate a unique image based on your input.

To get started, follow these steps:

1️⃣ Type your desired text by appending /img command in front.
2️⃣ Wait a moment while I create a custom image just for you.
3️⃣ Once the image is ready, I'll send it right back to you!

Type /help if you need more information about how to use this bot.

Enjoy exploring the power of words and images together! 🎉✨
"""
    update.message.reply_text(text)


start_handler = MessageHandler(Filters.command & Filters.regex('^/start'), start)
