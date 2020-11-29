import logging

from telegram.ext import CallbackContext
from telegram.update import Update


def settings_handler(update: Update, context: CallbackContext):
    logger = logging.getLogger()
    logger.info("settings_handler started")
