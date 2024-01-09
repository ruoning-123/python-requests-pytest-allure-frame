import time

import pytest
import requests
from src.utils.config_data import ConfigMethod as cm
from src.utils.common import CT
from src.utils.yaml_data import get_money_manager_content as mm
from src.utils.get_mariadb_sql import get_sql_data


class MoneyManager(CT):
    def add_money_manager(self, name, accloud_wtech__manager_overview__c):
        url = cm().read_config("REQUEST", "dev_domain") + mm()[
            'add_money_manager']['url']
        res = requests.request(method="post", url=url, json={'name': name,
                                                             'accloud_wtech__manager_overview__c': accloud_wtech__manager_overview__c},
                               headers=self.headers)
        assert dict(res.json())["code"] == 200

    def update_money_manager(self, sfid, name, accloud_wtech__manager_overview__c):
        sfidt = get_sql_data("select sfid from development.t_wtech_money_manager where name ='{}'".format(name))[0]
        url = cm().read_config("REQUEST", "dev_domain") + \
              mm()['update_money_manager']['url'] + sfidt
        res = requests.request(method="patch", url=url, json={
            "sfid": sfid,
            "name": name,
            "accloud_wtech__manager_overview__c": accloud_wtech__manager_overview__c,
            "accloud_wtech__city__c": "",
            "accloud_wtech__phone__c": "",
            "accloud_wtech__state__c": "",
            "accloud_wtech__street__c": "",
            "accloud_wtech__zipcode__c": "",
            "accloud_wtech__fax__c": ""
        },
                               headers=self.headers)
        assert dict(res.json())["code"] == 200

    def get_money_manager_by_name(self, name):
        url = cm().read_config("REQUEST", "dev_domain") + \
              mm()[
                  'get_money_manager_by_name']['url'] + name
        res = requests.request(method="get", url=url, headers=self.headers)
        assert dict(res.json())["code"] == 200

    def get_money_manager_by_sfid(self, sfid):
        url = cm().read_config("REQUEST", "dev_domain") + \
              mm()[
                  'get_money_manager_by_sfid']['url'] + sfid
        res = requests.request(method="get", url=url, headers=self.headers)
        assert dict(res.json())["code"] == 200

    def delete_money_manager_by_sfid(self, sfid):
        url = cm().read_config("REQUEST", "dev_domain") + \
              mm()[
                  'delete_money_manager_by_sfid']['url'] + sfid
        res = requests.request(method="delete", url=url, headers=self.headers)
        time.sleep(3)
        assert dict(res.json())["code"] == 200









