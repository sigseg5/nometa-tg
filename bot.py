#!/usr/bin/env python3

import logging
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from src.Utilities.runner import run
from src.handlers.document_handler import document_handler
from src.handlers.image_handler import image_handler
from src.handlers.setting_handler import settings_handler
from src.handlers.unsupported_handler import unsupported_handler
from src.handlers.video_handler import video_handler

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

APP_VER = "0.0.1"

TOKEN = os.getenv("TOKEN")
META_DELETION = os.getenv("META_DELETION")
FAWKES_APPLY = os.getenv("FAWKES_APPLY")


if __name__ == '__main__':
    logger.info("Starting bot")
    updater = Updater(token=TOKEN, use_context=True)

    updater.dispatcher.add_handler(CommandHandler("set", settings_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.photo, image_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.document, document_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.video, video_handler))

    # Handlers for unsupported actions
    updater.dispatcher.add_handler(MessageHandler(Filters.sticker, unsupported_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.location, unsupported_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.video, unsupported_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.audio, unsupported_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.command, unsupported_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.forwarded, unsupported_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.voice, unsupported_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.private, unsupported_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.status_update, unsupported_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.contact, unsupported_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.user, unsupported_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.group, unsupported_handler))

    run(updater)
