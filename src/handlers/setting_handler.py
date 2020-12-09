from logging import getLogger

from telegram.ext import CallbackContext
from telegram.update import Update


def settings_handler(update: Update, context: CallbackContext):
    # TODO: implement settings manager: change mode for metadata deletion, fawkes apply, fawkes mode
    logger = getLogger()
    logger.info("settings_handler started")
