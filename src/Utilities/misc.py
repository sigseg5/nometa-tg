from os import remove, getenv

from telegram.ext import CallbackContext
from telegram.update import Update

FAWKES_MODE = getenv("FAWKES_MODE")


def remove_original_doc_from_server(logger, update: Update):
    """
    Function for removing original file that sent by user with name "image" without extension
    :param logger: Logger from logging package
    :param update: Update from telegram.update package
    """
    logger.info("Preparing for original file deletion on server")
    try:
        remove("documents/image")
        update.message.reply_text("Original file successfully removed from server")
        logger.info("Original file successfully removed")
    except Exception as e:
        logger.error("Can't remove original file")
        logger.error(e.args)
        update.message.reply_text("Error at removing original file from server")


def send_file(logger, update: Update, context: CallbackContext, mode):
    """
    Function for sending file after applied Fawkes or metadata deletion tool, you can specify mode by last param.
    :param logger: Logger from logging package
    :param update: Update from telegram.update package
    :param context:
    CallbackContext from telegram.ext package
    :param mode: String value of mode for func. You can use `cloaked` and `clean` value.
    `cloaked` for  send file after applied Fawkes tool with filename="clean_image_{0}_cloaked.png",
    where {0} is FAWKES_MODE;
    `clean` for send file after metadata deletion with name "clean_image.jpg" .
    """

    logger.info("Preparing for sending cloaked file")

    if mode == "cloaked":
        try:
            _ = context.bot.send_document(chat_id=update.effective_message.chat_id,
                                          document=open("documents/clean_image_cloaked.png", "rb"))
            logger.info("Cloaked file sending finished")
        except Exception as e:
            logger.error("EXCEPTION at cloaked file sender section")
            logger.error(e.args)
            update.message.reply_text("Error at sending cloaked file")

    elif mode == "clean":
        try:
            _ = context.bot.send_document(chat_id=update.effective_message.chat_id,
                                          document=open("documents/clean_image.jpg",
                                                        "rb"))
            logger.info("Document without metadata sending finished")
            update.message.reply_text("Metadata removed from photo")
            logger.info("Document sending finished")
        except Exception as e:
            logger.error("EXCEPTION at file sender section for remove metadata")
            logger.error(e.args)
            update.message.reply_text("Error at sending clean file")
