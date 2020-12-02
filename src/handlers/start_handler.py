from logging import getLogger
from telegram.ext import CallbackContext
from telegram.update import Update


def start_handler(update: Update, context: CallbackContext):
    logger = getLogger()
    logger.info("User {} started bot".format(update.effective_user["id"]))
    update.message.reply_text("Hello from bot")
