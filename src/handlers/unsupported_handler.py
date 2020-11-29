import logging

from telegram.ext import CallbackContext
from telegram.update import Update


def unsupported_handler(update: Update, context: CallbackContext):
    logger = logging.getLogger()
    logger.info("Running unsupported_handler")
    update.message.reply_text("This action not supported")