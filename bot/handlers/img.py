from telegram import Update
from telegram.ext import CallbackContext, MessageHandler, Filters, DispatcherHandlerStop
from proxy_scraper import proxyScraper, proxyChecker


def img(update: Update, context: CallbackContext):
    txt = update.message.text.split(" ")

    if len(txt) <= 1:
        update.message.reply_text("No prompt found")
        raise DispatcherHandlerStop
    
    prompt = txt[1]
    
    proxyScraper.scrape()
    proxyChecker.check()

    proxies = open("proxies.txt", 'r')
    
    if len(proxies.readlines()) == 0:        
        update.message.reply_text('unfortunately no proxies found...')
    else:        
        update.message.reply_text('found ' + len(proxies.readlines()) + ' proxies...')
        update.message.reply_text('generating ' + prompt)


img_handler = MessageHandler(Filters.command & Filters.regex('^/img'), img)
