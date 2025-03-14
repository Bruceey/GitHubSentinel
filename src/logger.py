# src/logger.py

from loguru import logger
import sys

# 定义统一的日志格式字符串
format = '{time:YYYY-MM-DD HH:mm:ss} | {level:<8} | {name}:{function}:{line} - {message}'

# 配置 Loguru，移除默认的日志配置
logger.remove()

# 使用统一的日志格式配置标准输出和标准错误输出，支持彩色显示
logger.add(sys.stdout, level="DEBUG", format=format, colorize=True)
logger.add(sys.stderr, level="ERROR", format=format, colorize=True)

# 同样使用统一的格式配置日志文件输出，设置文件大小为1MB自动轮换
logger.add("logs/app.log", rotation="1 MB", level="DEBUG", format=format)

# 为logger设置别名，方便在其他模块中导入和使用
LOG = logger

# 将LOG变量公开，允许其他模块通过from logger import LOG来使用它
__all__ = ["LOG"]


# import logging
# from logging.handlers import RotatingFileHandler
# import sys


# class Logger:
#     def __init__(self, log_level="DEBUG"):
#         self.logger = logging.getLogger()
#         self.logger.setLevel(log_level)
#         self.formatter = logging.Formatter(
#             fmt="%(asctime)s %(levelname)-8s %(filename)s:%(lineno)d - %(message)s",
#             datefmt="%Y-%m-%d %H:%M:%S"
#             )
#         consoleHandler = logging.StreamHandler(sys.stdout)
#         consoleHandler.setFormatter(self.formatter)
#         self.logger.addHandler(consoleHandler)

#     def add(self, log_file_path, maxBytes=1048576, level="DEBUG", backupCount=999):
#         # 生成一个包含fileHandler新的logger对象，maxBytes默认为1MB
#         fileHandler = RotatingFileHandler(
#             filename=log_file_path,
#             maxBytes=maxBytes,        # 1MiB触发轮转
#             backupCount=backupCount   # 保留备份文件999个
#         )



# FORMAT = '%(asctime)s %(levelname)-8s %(filename)s:%(lineno)d - %(message)s'
# datefmt = "[%Y-%m-%d %H:%M:%S]"
# formatter = logging.Formatter(FORMAT, datefmt=datefmt)

# consoleHandler = logging.StreamHandler()
# consoleHandler.setFormatter(formatter)

# fileHandler = RotatingFileHandler(
#     filename="logs/app.log",
#     maxBytes=1024 * 1024,    # 1MiB触发轮转
#     backupCount=999          # 保留备份文件999个
# )
# fileHandler.setFormatter(formatter)

# LOG = logging.getLogger()
# LOG.setLevel(logging.DEBUG)
# LOG.addHandler(consoleHandler)
# LOG.addHandler(fileHandler)


# logging.debug("这是一条debug信息")
# logging.info("这是一条info信息")
# logging.warning("这是一条warning信息")
# logging.error("这是一条error信息")
# logging.critical("这是一条critical信息")

