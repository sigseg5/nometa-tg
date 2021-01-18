from os import remove, getenv
from telegram.ext import CallbackContext
from telegram.update import Update


def remove_original_doc_from_server(logger, update):
    logger.info("Preparing for original file deletion on server")
    try:
        remove("documents/image")
        update.message.reply_text("Original file successfully removed from server")
        logger.info("Original file successfully removed")
    except Exception:
        logger.error("Can't remove original file")
        update.message.reply_text("Error at removing original file from server")


def send_file(logger, update: Update, context: CallbackContext, mode):
    FAWKES_MODE = getenv("FAWKES_MODE")

    logger.info("Preparing for sending cloaked file\n")

    if mode == "cloaked":
        try:
            _ = context.bot.send_document(chat_id=update.effective_message.chat_id,
                                          document=open('documents/clean_image_{0}_cloaked.png'.format(FAWKES_MODE), 'rb'))
            logger.info("Cloaked file sending finished")
        except Exception as e:
            logger.error(e)
            logger.critical("EXCEPTION at cloaked file sender section")
            update.message.reply_text("Error at sending cloaked file")

    elif mode == "clean":
        try:
            _ = context.bot.send_document(chat_id=update.effective_message.chat_id,
                                          document=open('documents/clean_image.jpg', 'rb'))
            logger.info("Document without metadata sending finished")
            update.message.reply_text("Metadata removed from photo")
            logger.info("Document sending finished")
        except Exception as e:
            logger.error(e)
            logger.critical("EXCEPTION at file sender section for remove metadata")
            update.message.reply_text("Error at sending clean file")
