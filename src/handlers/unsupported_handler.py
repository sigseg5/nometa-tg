from logging import getLogger

from telegram.update import Update


def unsupported_handler(update: Update):
    """
    This function is started if the bot receives one of the unsupported actions
    :param update: Update from telegram.update
    """
    logger = getLogger()
    logger.info("Running unsupported_handler")
    update.message.reply_text("This action not supported")
