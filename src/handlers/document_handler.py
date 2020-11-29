import logging
import os
import subprocess

from filetype import filetype
from telegram.ext import CallbackContext
from telegram.update import Update

SUPPORTED_MIME_LIST = ("image/jpeg", "image/png")


def document_handler(update: Update, context: CallbackContext):
    logger = logging.getLogger()
    logger.info(subprocess.check_output("pwd").decode('utf-8'))
    logger.info(subprocess.check_output(["ls", "-lah"]).decode('utf-8'))
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
