# -*- coding: UTF-8 -*-
# /usr/bin/env python
import os

# 项目的路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# 配置文件的路径
CONFIG_PATH = os.path.join(BASE_PATH, "doc", "config", "my.ini")

# 数据的路径
DATA_PATH = os.path.join(BASE_PATH, "doc", "data")

# 日志文件的路径
LOG_PATH = os.path.join(BASE_PATH, "doc", "log")

# 测试报告的路径
REPORT_PATH = os.path.join(BASE_PATH, "doc", "report")

# 测试用例的路径
TESTCASE_PATH = os.path.join(BASE_PATH, "test")

# 公共方法的路径
UTILS_PATH = os.path.join(BASE_PATH, "src", "utils")

# print(BASE_PATH)
# print(CONFIG_PATH)
# print(INPUT_DATA_PATH)
# print(OUTPUT_DATA_PATH)
# print(LOG_PATH)
# print(REPORT_PATH)
# print(TESTCASE_PATH)
# print(UTILS_PATH)
