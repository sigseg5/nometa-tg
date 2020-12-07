from logging import getLogger
from os import remove, getenv, path
from subprocess import call

from telegram.ext import CallbackContext
from telegram.update import Update
from src.Utilities.cmd_logger import result_of

FAWKES_MODE = getenv("FAWKES_MODE")


def image_handler(update: Update, context: CallbackContext):
    logger = getLogger()
    logger.info("image_handler started")
    file = context.bot.getFile(update.message.photo[-1].file_id)
    logger.info("Photo downloading started")
    file.download('images/image.jpg')
    logger.info("Photo downloading finished")
    update.message.reply_text("Photo successfully downloaded")
    is_faces_found = False

    try:
        logger.info("Goes into fawkes section")
        update.message.reply_text("Applying face hider tools, wait...")
        _ = call(["fawkes", "-d", "images", "--mode", FAWKES_MODE])
        if path.exists('images/image_{0}_cloaked.png'.format(FAWKES_MODE)):
            is_faces_found = True
`
        logger.info("Does faces founded?: {}".format(is_faces_found))
        logger.info("fawkes try-catch finished")

    except Exception as e:
        logger.error(e)
        logger.critical("EXCEPTION at fawkes section")
        update.message.reply_text("Error at hiding faces")

    logger.info("Preparing for sending photo\n")
    logger.info("\nStarting image sender")
    try:
        _ = context.bot.send_photo(chat_id=update.effective_message.chat_id,
                                   photo=open('images/image_{0}_cloaked.png'.format(FAWKES_MODE), 'rb'))
        logger.info("Photo sending finished")
    except Exception as e:
        logger.error(e)
        logger.critical("EXCEPTION at photo sender section")
        update.message.reply_text("Error at sending photo")

    logger.info("Preparing for original photo deletion on server")
    try:
        remove("images/image.jpg")
        update.message.reply_text("Original photo successfully removed from server")
        logger.info("Original photo successfully removed")
    except Exception:
        logger.error("Can't remove original image")
        update.message.reply_text("Error at removing original photo from server")

    logger.info("Preparing for cloaked photo deletion on server")
    try:
        remove("images/image_{0}_cloaked.png".format(FAWKES_MODE))
        update.message.reply_text("Cloaked photo successfully removed from server")
        logger.info("Cloaked photo successfully removed")
    except Exception:
        logger.error("Can't remove cloaked image")
        update.message.reply_text("Error at removing cloaked photo from server")
