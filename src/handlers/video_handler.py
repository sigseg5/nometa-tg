import logging

from telegram.ext import CallbackContext
from telegram.update import Update


def video_handler(update: Update, context: CallbackContext):
    logger = logging.getLogger()
    logger.info("video_handler started")
    update.message.reply_text("Videos not supported yet!")