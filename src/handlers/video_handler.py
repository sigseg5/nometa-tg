from logging import getLogger
from logging import getLogger

from telegram.ext import CallbackContext
from telegram.update import Update


def video_handler(update: Update, context: CallbackContext):
    # TODO: may be add fawkes style tool for video processing
    logger = getLogger()
    logger.info("video_handler started")
    update.message.reply_text("Videos not supported yet!")
