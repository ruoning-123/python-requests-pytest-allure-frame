# -*- coding: UTF-8 -*-
# /usr/bin/env python
import os
from src.route import paths
import yaml


# 获取文件内容，包括input_data和output_data的文件路径内容
def get_yaml_data(*yaml_file):
    path = os.path.join(paths.DATA_PATH, *yaml_file)
    file = open(path, 'r', encoding='utf-8')
    file_data = file.read()
    content = yaml.load(file_data, Loader=yaml.FullLoader)
    return dict(content)


# amp的yaml文件内容
# 获取money manager的yaml文件内容
def get_money_manager_content():
    return get_yaml_data('amp_api', 'amp_accloud_api', 'money_manager.yaml')


# 获取separate account的yaml文件内容
def get_separate_account_content():
    return get_yaml_data('amp_api', 'amp_accloud_api', 'separate_account.yaml')


# 获取separate account的yaml文件内容
def get_cascading_update_content():
    return get_yaml_data('amp_api', 'amp_accloud_api', 'cascading_update.yaml')


def get_product_detail_content():
    return get_yaml_data('amp_api', 'amp_accloud_api', 'product_detail.yaml')


if __name__ == '__main__':
    print(get_money_manager_content())
