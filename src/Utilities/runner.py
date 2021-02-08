from logging import getLogger

from telegram.ext import Updater


def run(updater: Updater):
    """
    Function to start the bot
    :param updater: Updater from telegram.ext
    """
    logger = getLogger()
    logger.info("Starting polling")
    updater.start_polling()
