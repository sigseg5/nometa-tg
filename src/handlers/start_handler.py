from telegram.update import Update


def start_handler(update: Update):
    """
    This function sends a welcome message then user started a bot.
    :param update: Update from telegram.update
    """
    update.message.reply_text("This bot that provides an opportunity to automatically delete all metadata from photo "
                              "and apply fawkes face hiding tool to hide you face from face recognition apps in "
                              "social networks etc.\nNow you can send photo as photo or document.\nYou will get "
                              "message if tool can't find any faces.")
