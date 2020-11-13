#!/usr/bin/env python3

import logging
import os
from telegram import *
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

NOMETA_VER = "0.0.1"

TOKEN = os.getenv("TOKEN")
META_DELETION = os.getenv("META_DELETION")
FAWKES_APPLY = os.getenv("FAWKES_APPLY")
FAWKES_MODE = os.getenv("FAWKES_MODE")


def run(updater):
    logger.info("Starting polling")
    updater.start_polling()


def image_handler(update: Update, context: CallbackContext):
    logger.info("Starting image_handler")
    file = context.bot.getFile(update.message.photo[-1].file_id)
    print("file_id: " + str(update.message.photo[-1].file_id))
    file.download('./image.jpg')


if __name__ == '__main__':
    logger.info("Starting bot")
    updater = Updater(token=TOKEN, use_context=True)

    updater.dispatcher.add_handler(CommandHandler("start", start_handler))
    updater.dispatcher.add_handler(CommandHandler("random", random_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.photo, image_handler))

    run(updater)
