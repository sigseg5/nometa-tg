from telegram.ext import Updater
from logging import getLogger


def run(updater: Updater):
    logger = getLogger()
    logger.info("Starting polling")
    updater.start_polling()
