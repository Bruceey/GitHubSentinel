# import logging
# from rich.logging import RichHandler

# FORMAT = '%(message)s'
# logging.basicConfig(
#     level="NOTSET", format=FORMAT, handlers=[RichHandler(omit_repeated_times=False)]
# )

# log = logging.getLogger("rich")
# log.debug("Debug message")
# log.info("Hello, World!")
# log.warning("This is a warning message")
# log.error("This is an error message")
# log.critical("This is a critical message")


from loguru import logger
import sys
console_format = '<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level:<8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>'
logger.remove()
logger.add(sys.stdout, level="DEBUG", format=console_format, colorize=True)

def yangmi():
    logger.debug("That's it, beautiful and simple logging!")


yangmi()