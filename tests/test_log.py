import logging
from rich.logging import RichHandler

FORMAT = '%(message)s'
logging.basicConfig(
    level="NOTSET", format=FORMAT, handlers=[RichHandler(omit_repeated_times=False)]
)

log = logging.getLogger("rich")
log.debug("Debug message")
log.info("Hello, World!")
log.warning("This is a warning message")
log.error("This is an error message")
log.critical("This is a critical message")