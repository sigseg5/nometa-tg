from os import remove


def remove_original_doc_from_server(logger, update):
    logger.info("Preparing for original file deletion on server")
    try:
        remove("documents/image")
        update.message.reply_text("Original file successfully removed from server")
        logger.info("Original file successfully removed")
    except Exception:
        logger.error("Can't remove original file")
        update.message.reply_text("Error at removing original file from server")
