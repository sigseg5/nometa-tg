import logging
import os
import subprocess

from telegram.ext import CallbackContext
from telegram.update import Update
from src.Utilities.cmd_logger import result_of

FAWKES_MODE = os.getenv("FAWKES_MODE")


# FIXME: Exception 'int' object has no attribute 'decode'
# FIXME: Remove file_id hash
# FIXME: fawkes apply for 2 images ??

def image_handler(update: Update, context: CallbackContext):
    logger = logging.getLogger()
    logger.info("image_handler started")
    file = context.bot.getFile(update.message.photo[-1].file_id)
    logger.info("file_id: " + str(update.message.photo[-1].file_id))
    logger.info("File downloading started")
    file.download('images/image.jpg')
    logger.info("File downloading finished")

    try:
        logger.info("Goes into fawkes try-catch")
        run_protection = subprocess.call(["fawkes", "-d", "images", "--mode", FAWKES_MODE])
        logger.info(run_protection)
        logger.info("fawkes try-catch finished")

    except Exception as e:
        logger.error(e)
        logger.critical("EXCEPTION at fawkes section")

    logger.info("Preparing for sending photo\n")
    logger.info(result_of("ls images"))
    logger.info("\nStarting image sender")
    try:
        _ = context.bot.send_photo(chat_id=update.effective_message.chat_id,
                                   photo=open('images/image_{0}_cloaked.png'.format(FAWKES_MODE), 'rb'))
        logger.info("Photo sending finished")
    except Exception as e:
        logger.error(e)
        logger.critical("EXCEPTION at photo sender section")
# TODO: Add photo deletion
