from logging import getLogger
from os import remove, getenv, path
from subprocess import call

from filetype import filetype
from telegram.ext import CallbackContext
from telegram.update import Update

from src.Utilities.metadata_worker import delete_metadata
from src.Utilities.cmd_logger import result_of

SUPPORTED_MIME_LIST = "image/jpeg"
FAWKES_MODE = getenv("FAWKES_MODE")


def document_handler(update: Update, context: CallbackContext):
    """
        This function has multiple scope of responsibility:
        1. Downloading a document as '.jpg', generally this is best solution for compatibility;
        2. Guessing a file type. If type isn't supported file removes from server;
        3. Checking is this file type supported by application. If type isn't supported file removes from server;
        4. Removing metadata from document via calling 'metadata_worker.py';
        2. Applying face hiding tool;
        3. Sending cloaked and metadata-free file;
        4. Removing original, metadata-free, and cloaked files from server.
        Yep, this function definitely should be refactored...
        """
    logger = getLogger()
    is_faces_found = False

    logger.info("document_handler started")
    file = context.bot.getFile(update.message.document.file_id)
    file.download('documents/image.jpg')

    logger.info("Guessing file type")
    kind = filetype.guess('documents/image.jpg')
    if kind is None:
        logger.error('Cannot guess file type!')
        update.message.reply_text("Cannot guess file type. This file type not supported")

        try:
            logger.info("Preparing for file deletion from server (kind guess)")
            remove("documents/image.jpg")
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
            remove("documents/image.jpg")
            update.message.reply_text("File successfully removed from server")
        except Exception:
            logger.error("Can't remove file")
            update.message.reply_text("Error at removing file from server")
        return
    else:
        logger.info("Metadata removing started")
        delete_metadata("documents/image.jpg")
        logger.info("Metadata was successfully deleted")
        update.message.reply_text("Metadata was successfully deleted")

        logger.info("Preparing for original file deletion on server")
        try:
            remove("documents/image.jpg")
            update.message.reply_text("Original file successfully removed from server")
            logger.info("Original file successfully removed")
        except Exception:
            logger.error("Can't remove original file")
            update.message.reply_text("Error at removing original file from server")

        try:
            logger.info("Goes into fawkes section")
            update.message.reply_text("Applying face hider tools, wait...")
            _ = call(["fawkes", "-d", "documents", "--mode", FAWKES_MODE])
            logger.info(result_of("ls documents"))
            if path.exists('documents/clean_image_{0}_cloaked.png'.format(FAWKES_MODE)):
                is_faces_found = True

            logger.info("Does faces found?: {}".format(is_faces_found))
            logger.info("fawkes try-catch finished")

        except Exception as e:
            logger.error(e)
            logger.critical("EXCEPTION at fawkes section")
            update.message.reply_text("Error at hiding faces")

        if is_faces_found:
            logger.info("Preparing for sending cloaked file\n")
            try:
                _ = context.bot.send_document(chat_id=update.effective_message.chat_id,
                                              document=open('documents/clean_image_{0}_cloaked.png'.format(FAWKES_MODE),
                                                            'rb'))
                logger.info("Cloaked file sending finished")
            except Exception as e:
                logger.error(e)
                logger.critical("EXCEPTION at cloaked file sender section")
                update.message.reply_text("Error at sending cloaked file")

            logger.info("Preparing for clean file deletion on server")
            try:
                remove("documents/clean_image.jpg")
                update.message.reply_text("Clean version of file successfully removed from server")
                logger.info("Clean version of file successfully removed")
            except Exception:
                logger.error("Can't remove clean version of file")
                update.message.reply_text("Error at removing clean version of file from server")

            logger.info("Preparing for cloaked photo deletion on server")
            try:
                remove("documents/clean_image_{0}_cloaked.png".format(FAWKES_MODE))
                update.message.reply_text("Cloaked file successfully removed from server")
                logger.info("Cloaked file successfully removed")
            except Exception:
                logger.error("Can't remove cloaked file")
                update.message.reply_text("Error at removing cloaked file from server")
        else:
            logger.info("No faces found")
            update.message.reply_text("Can't find any faces")
            logger.info("Preparing for sending photo without metadata")
            try:
                _ = context.bot.send_document(chat_id=update.effective_message.chat_id,
                                              document=open('documents/clean_image.jpg', 'rb'))
                logger.info("Document without metadata sending finished")
                update.message.reply_text("Metadata removed from photo")
                logger.info("Photo sending finished")
            except Exception as e:
                logger.error(e)
                logger.critical("EXCEPTION at file sender section for remove metadata")
                update.message.reply_text("Error at sending file")

            try:
                remove("documents/clean_image.jpg")
                update.message.reply_text("File without metadata successfully removed from server")
                logger.info("File without metadata successfully removed")
            except Exception:
                logger.error("Can't remove file without metadata")
                update.message.reply_text("Error at removing file without metadata from server")
