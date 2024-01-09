# -*- coding: UTF-8 -*-
# /usr/bin/env python
import sys
import configparser
from src.route import paths


class ConfigMethod:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(paths.CONFIG_PATH, encoding="utf-8")

    # 读取my.ini文件，返回参数
    def read_config(self, section, key):
        return self.config[section][key]

    # 读取my.ini写入配置文件
    def write_config(self, section, key, msg):
        self.config.set(section, key, msg)
        self.config.write(open(paths.CONFIG_PATH, 'w'))
        return


if __name__ == '__main__':
    cm = ConfigMethod()
    print(cm.read_config("REQUEST", "token"))
