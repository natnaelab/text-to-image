from telegram import Update
from telegram.ext import CallbackContext, DispatcherHandlerStop
from bot.models import User
from django.utils import timezone


def middleware_handler(update: Update, context: CallbackContext):
    msg_text = ""
    try: msg_text = update.message and update.message.text
    except: raise DispatcherHandlerStop
    user = update.effective_user

    if update.message and not update.message.chat.type == "private":
        raise DispatcherHandlerStop

    db_user: User = User.objects.filter(tid=user.id).first()

    if user.is_bot or (db_user and db_user.is_banned):
        raise DispatcherHandlerStop

    if db_user:
        if update.message:
            if not db_user.is_active:
                db_user.is_active = True
            
            db_user.message_count += 1
            db_user.last_message_at = timezone.now()
            db_user.save()

    else:
        if not msg_text or not msg_text.startswith('/start'):
            update.message.reply_text('start with /start command!')
            raise DispatcherHandlerStop
        else:
            User(tid=user.id).save()
