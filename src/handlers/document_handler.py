from logging import getLogger
from os import remove, getenv, path
from subprocess import call

from filetype import filetype
from telegram.ext import CallbackContext
from telegram.update import Update

from src.Utilities.metadata_worker import delete_metadata
from src.Utilities.metadata_worker import delete_metadata_from_png
from src.Utilities.cmd_logger import result_of
from src.Utilities.misc import remove_original_doc_from_server
from src.Utilities.misc import send_file

SUPPORTED_MIME_LIST = ("image/jpeg", "image/png")
FAWKES_MODE = getenv("FAWKES_MODE")


def document_handler(update: Update, context: CallbackContext):
    """
        This function has multiple scope of responsibility:
        1. Downloading a document without extension;
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
    file.download("documents/image")

    logger.info("Guessing file type")
    kind = filetype.guess("documents/image")
    if kind is None:
        logger.error("Cannot guess file type!")
        update.message.reply_text("Cannot guess file type. This file type not supported")

        try:
            logger.info("Preparing for file deletion from server (kind guess)")
            remove("documents/image")
            update.message.reply_text("File successfully removed from server")
        except Exception as e:
            logger.error("Can't remove file (kind guess)")
            logger.error(e.args)
            update.message.reply_text("Error at removing file from server")
        return

    logger.info("File MIME type: %s", kind.mime)

    if kind.mime not in SUPPORTED_MIME_LIST:
        update.message.reply_text("{} not supported!".format(kind.mime))
        logger.info("Removing file...")
        try:
            remove("documents/image")
            update.message.reply_text("File successfully removed from server")
        except Exception as e:
            logger.error("Can't remove file")
            logger.error(e.args)
            update.message.reply_text("Error at removing file from server")
        return
    else:
        logger.info("Metadata removing started")
        if kind.mime == "image/png":
            try:
                delete_metadata_from_png("documents/image")
                logger.info("Metadata was successfully deleted")
            except Exception as e:
                logger.error("Metadata wasn't deleted")
                logger.error(e.args)
                remove_original_doc_from_server(logger, update)
                update.message.reply_text("Error at removing metadata from PNG file\nFile removed from server")

            remove_original_doc_from_server(logger, update)

            try:
                logger.info("Goes into fawkes section")
                update.message.reply_text("Applying face hider tools, wait...")
                _ = call(["fawkes", "-d", "documents", "--mode", FAWKES_MODE])
                logger.info(result_of("ls documents"))
                if path.exists("documents/clean_image_cloaked.png"):
                    is_faces_found = True

                logger.info("Does faces found?: %s", is_faces_found)
                logger.info("fawkes try-catch finished")

            except Exception as e:
                logger.error("EXCEPTION at fawkes section")
                logger.error(e.args)
                update.message.reply_text("Error at hiding faces")

            if is_faces_found:
                logger.info("Preparing for sending cloaked file")

                send_file(logger, update, context, "cloaked")

                logger.info("Preparing for clean file deletion on server")
                try:
                    remove("documents/clean_image.png")
                    update.message.reply_text("Clean version of file successfully removed from server")
                    logger.info("Clean version of file successfully removed")
                except Exception as e:
                    logger.error("Can't remove clean version of file")
                    logger.error(e.args)
                    update.message.reply_text("Error at removing clean version of file from server")

                logger.info("Preparing for cloaked photo deletion on server")
                try:
                    remove("documents/clean_image_cloaked.png")
                    update.message.reply_text("Cloaked file successfully removed from server")
                    logger.info("Cloaked file successfully removed")
                except Exception as e:
                    logger.error("Can't remove cloaked file")
                    logger.error(e.args)
                    update.message.reply_text("Error at removing cloaked file from server")
            else:
                logger.info("No faces found")
                update.message.reply_text("Can't find any faces")
                logger.info("Preparing for sending photo without metadata")

                send_file(logger, update, context, "clean")

                try:
                    remove("documents/clean_image.png")
                    update.message.reply_text("File without metadata successfully removed from server")
                    logger.info("File without metadata successfully removed")
                except Exception as e:
                    logger.error("Can't remove file without metadata")
                    logger.error(e.args)
                    update.message.reply_text("Error at removing file without metadata from server")

        else:
            delete_metadata("documents/image")
            logger.info("Metadata was successfully deleted")
            update.message.reply_text("Metadata was successfully deleted")

            remove_original_doc_from_server(logger, update)

            try:
                logger.info("Goes into fawkes section")
                update.message.reply_text("Applying face hider tools, wait...")
                _ = call(["fawkes", "-d", "documents", "--mode", FAWKES_MODE])
                logger.info(result_of("ls documents"))
                if path.exists("documents/clean_image_cloaked.png"):
                    is_faces_found = True

                logger.info("Does faces found?: %s", is_faces_found)
                logger.info("fawkes try-catch finished")

            except Exception as e:
                logger.error("EXCEPTION at fawkes section")
                logger.error(e.args)
                update.message.reply_text("Error at hiding faces")

            if is_faces_found:
                logger.info("Preparing for sending cloaked file")

                send_file(logger, update, context, "cloaked")

                logger.info("Preparing for clean file deletion on server")
                try:
                    remove("documents/clean_image.jpg")
                    update.message.reply_text("Clean version of file successfully removed from server")
                    logger.info("Clean version of file successfully removed")
                except Exception as e:
                    logger.error("Can't remove clean version of file")
                    logger.error(e.args)
                    update.message.reply_text("Error at removing clean version of file from server")

                logger.info("Preparing for cloaked photo deletion on server")
                try:
                    remove("documents/clean_image_cloaked.png")
                    update.message.reply_text("Cloaked file successfully removed from server")
                    logger.info("Cloaked file successfully removed")
                except Exception as e:
                    logger.error("Can't remove cloaked file")
                    logger.error(e.args)
                    update.message.reply_text("Error at removing cloaked file from server")
            else:
                logger.info("No faces found")
                update.message.reply_text("Can't find any faces")
                logger.info("Preparing for sending photo without metadata")

                send_file(logger, update, context, "clean")

                try:
                    remove("documents/clean_image.jpg")
                    update.message.reply_text("File without metadata successfully removed from server")
                    logger.info("File without metadata successfully removed")
                except Exception as e:
                    logger.error("Can't remove file without metadata")
                    logger.error(e.args)
                    update.message.reply_text("Error at removing file without metadata from server")
