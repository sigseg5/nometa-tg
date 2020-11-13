#!/usr/bin/env python3

import logging
import os
import subprocess
import filetype

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
SUPPORTED_MIME_LIST = ("image/jpeg", "image/png")


def run(updater):
    logger.info("Starting polling")
    updater.start_polling()


def image_handler(update: Update, context: CallbackContext):
    logger.info("image_handler started")
    file = context.bot.getFile(update.message.photo[-1].file_id)
    logger.info("file_id: " + str(update.message.photo[-1].file_id))
    logger.info("File downloading started")
    file.download('images/image.jpg')
    logger.info("File downloading finished")

    try:
        logger.info("Goes into fawkes try-catch")
        run_protection = subprocess.call(["fawkes", "-d", "images", "--mode", FAWKES_MODE])
        logger.info(run_protection.decode('utf-8'))
        logger.info("fawkes try-catch finished")

    except Exception as e:
        logger.error(e)
        logger.critical("EXCEPTION at fawkes section")

    logger.info("Preparing for sending photo\n")
    ls_proc = subprocess.check_output(["ls", "images"])
    logger.info(ls_proc.decode('utf-8'))
    logger.info("\nStarting image sender")
    try:
        _ = context.bot.send_photo(chat_id=update.effective_message.chat_id, photo=open('images/image_{0}_cloaked.png'.format(FAWKES_MODE), 'rb'))
        logger.info("Photo sending finished")
    except Exception as e:
        logger.error(e)
        logger.critical("EXCEPTION at photo sender section")


def settings_handler(update: Update, context: CallbackContext):
    logger.info("settings_handler started")


def document_handler(update: Update, context: CallbackContext):
    # remove meta and apply fawkes
    logger.info("document_handler started")
    file = context.bot.getFile(update.message.document.file_id)
    file.download('images/image.jpg')
    logger.info("File successfully downloaded")

    kind = filetype.guess('images/image.jpg')
    if kind is None:
        logger.error('Cannot guess file type!')

        return

    logger.info('File MIME type: %s' % kind.mime)

    if kind.mime not in SUPPORTED_MIME_LIST:
        update.message.reply_text("{} not supported!".format(kind.mime))
        logger.info("Removing file...")
        try:
            os.remove("images/image.jpg")
        except Exception:
            logger.error("Can't remove file")
            return

        return
    else:
        logger.info("Sending document")
        try:
            _ = context.bot.send_document(chat_id=update.effective_message.chat_id, document=open('images/image.jpg', 'rb'))
            logger.info("Document sending finished")
        except Exception:
            logger.error("Can't send document")
            return


def video_handler(update: Update, context: CallbackContext):
    logger.info("video_handler started")
    update.message.reply_text("Videos not supported yet!")


def unsupported_handler(update: Update, context: CallbackContext):
    logger.info("Running unsupported_handler")
    update.message.reply_text("This action not supported")


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
