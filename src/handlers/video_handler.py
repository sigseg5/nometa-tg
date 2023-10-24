from logging import getLogger

from telegram.ext import CallbackContext
from telegram.update import Update

def video_handler(update: Update, context: CallbackContext):
    """
    This function is started if the bot receives video
    :param update: Update from telegram.update
    """
    logger = getLogger()
    logger.info("video_handler started")
    update.message.reply_text("Videos not supported yet!")
