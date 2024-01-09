# -*- coding: UTF-8 -*-
# /usr/bin/env python
import logging
from src.route.paths import LOG_PATH

# 编程的方式记录日志

# 记录器
logger1 = logging.getLogger("logger1")
logger1.setLevel(logging.DEBUG)

# 处理器
# 1.标准输出
sh1 = logging.StreamHandler()

sh1.setLevel(logging.DEBUG)

# 2.文件输出
# 没有设置输出级别，将用logger1的输出级别(并且输出级别在设置的时候级别不能比Logger的低!!!)，设置了就使用自己的输出级别
fh1 = logging.FileHandler(filename="{}/my.log".format(LOG_PATH), mode='a',encoding='utf-8')

# 格式器
fmt1 = logging.Formatter(fmt="%(asctime)s - %(levelname)-8s - %(filename)-8s : %(lineno)3s line - %(message)s"
                         , datefmt="%Y/%m/%d %H:%M:%S")

fmt2 = logging.Formatter(fmt="%(asctime)s - %(levelname)-8s - %(filename)-8s : %(lineno)3s line - %(message)s"
                         , datefmt="%Y/%m/%d %H:%M:%S")

# 给处理器设置格式
sh1.setFormatter(fmt1)
fh1.setFormatter(fmt2)

# 记录器设置处理器
logger1.addHandler(sh1)
logger1.addHandler(fh1)


# 打印日志代码
def log_debug(msg):
    logger1.debug(msg)


def log_info(msg):
    logger1.info(msg)


def log_warning(msg):
    logger1.warning(msg)


def log_error(msg):
    logger1.error(msg)


def log_critical(msg):
    logger1.critical(msg)
