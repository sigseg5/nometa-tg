#!/usr/bin/env python3

from logging import getLogger, basicConfig, INFO
from os import getenv

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from src.Utilities.runner import run
from src.handlers.document_handler import document_handler
from src.handlers.image_handler import image_handler
from src.handlers.setting_handler import settings_handler
from src.handlers.unsupported_handler import unsupported_handler
from src.handlers.video_handler import video_handler
from src.handlers.start_handler import start_handler

basicConfig(level=INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = getLogger()

APP_VER = "0.1.0"

TOKEN = getenv("TOKEN")

# Will be used for settings manager
# META_DELETION = getenv("META_DELETION")
# FAWKES_APPLY = getenv("FAWKES_APPLY")


if __name__ == '__main__':
    logger.info("Starting bot, version {}".format(APP_VER))
    updater = Updater(token=TOKEN, use_context=True)

    # Handlers for supported actions
    updater.dispatcher.add_handler(CommandHandler("set", settings_handler))
    updater.dispatcher.add_handler(CommandHandler("start", start_handler))
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
    updater.dispatcher.add_handler(MessageHandler(Filters.chat_type.private, unsupported_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.status_update, unsupported_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.contact, unsupported_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.user(), unsupported_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.group, unsupported_handler))

    run(updater)
