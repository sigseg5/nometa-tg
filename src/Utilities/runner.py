from telegram.ext import Updater
import logging


def run(updater: Updater):
    logger = logging.getLogger()
    logger.info("Starting polling")
    updater.start_polling()
