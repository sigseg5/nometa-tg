from logging import getLogger

from telegram.ext import CallbackContext
from telegram.update import Update

def settings_handler(update: Update, context: CallbackContext):
    """
    This function is started if the bot receives settings command (not used yet)
    """
    logger = getLogger()
    logger.info("settings_handler started")
