from logging import getLogger


def settings_handler():
    """
    This function is started if the bot receives settings command (not used yet)
    """
    logger = getLogger()
    logger.info("settings_handler started")
