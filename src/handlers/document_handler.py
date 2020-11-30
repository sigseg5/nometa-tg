from logging import getLogger
from os import remove
from filetype import filetype
from telegram.ext import CallbackContext
from telegram.update import Update

SUPPORTED_MIME_LIST = ("image/jpeg", "image/png")


def document_handler(update: Update, context: CallbackContext):
    logger = getLogger()
    logger.info("document_handler started")
    file = context.bot.getFile(update.message.document.file_id)
    logger.info("File downloading started")
    file.download('images/image.jpg')
    logger.info("File successfully downloaded")

    logger.info("Guessing file type")
    kind = filetype.guess('images/image.jpg')
    if kind is None:
        logger.error('Cannot guess file type!')
        update.message.reply_text("Cannot guess file type. This file type not supported")

        try:
            logger.info("Preparing for file deletion from server (kind guess)")
            remove("images/image.jpg")
            update.message.reply_text("File successfully removed from server")
        except Exception:
            logger.error("Can't remove file (kind guess)")
            update.message.reply_text("Error at removing file from server")

        return

    logger.info('File MIME type: %s' % kind.mime)

    if kind.mime not in SUPPORTED_MIME_LIST:
        update.message.reply_text("{} not supported!".format(kind.mime))
        logger.info("Removing file...")
        try:
            remove("images/image.jpg")
            update.message.reply_text("File successfully removed from server")
        except Exception:
            logger.error("Can't remove file")
            update.message.reply_text("Error at removing file from server")
        return
    else:
        # TODO: Remove metadata and apply fawkes
        logger.info("Sending document")
        try:
            _ = context.bot.send_document(chat_id=update.effective_message.chat_id, document=open('images/image.jpg', 'rb'))
            logger.info("Document sending finished")
        except Exception:
            logger.error("Can't send document")
            return
