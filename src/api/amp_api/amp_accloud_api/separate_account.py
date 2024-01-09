import requests
from src.utils.config_data import ConfigMethod as cm
from src.utils.common import CT
from src.utils.yaml_data import get_separate_account_content as sa
import time

class SeparateAccount(CT):
    def add_separate_account_sma(self, accloud_wtech__category__c, accloud_wtech__custodians__c,
                                 accloud_wtech__mmanager__c,
                                 accloud_wtech__modelname__c, accloud_wtech__position__c, accloud_wtech__risklevel__c,
                                 accloud_wtech__type__c):
        url = cm().read_config("REQUEST", "dev_domain") + sa()[
            'add_separate_account_sma']['url']
        res = requests.request(method="post", url=url, json={
            "accloud_wtech__category__c": accloud_wtech__category__c,
            "accloud_wtech__custodians__c": accloud_wtech__custodians__c,
            "accloud_wtech__mmanager__c": accloud_wtech__mmanager__c,
            "accloud_wtech__modelname__c": accloud_wtech__modelname__c,
            "accloud_wtech__position__c": accloud_wtech__position__c,
            "accloud_wtech__risklevel__c": accloud_wtech__risklevel__c,
            "accloud_wtech__type__c": accloud_wtech__type__c
        },
                               headers=self.headers)
        assert dict(res.json())["code"] == 200

    def update_separate_account_sma(self, accloud_wtech__category__c, accloud_wtech__custodians__c,
                                    accloud_wtech__mmanager__c,
                                    accloud_wtech__modelname__c, accloud_wtech__position__c,
                                    accloud_wtech__risklevel__c,
                                    accloud_wtech__type__c, sma_sfid):
        url = cm().read_config("REQUEST", "dev_domain") + sa()[
            'update_separate_account_sma']['url'] + sma_sfid
        res = requests.request(method="patch", url=url, json={
            "accloud_wtech__category__c": accloud_wtech__category__c,
            "accloud_wtech__custodians__c": accloud_wtech__custodians__c,
            "accloud_wtech__mmanager__c": accloud_wtech__mmanager__c,
            "accloud_wtech__modelname__c": accloud_wtech__modelname__c,
            "accloud_wtech__position__c": accloud_wtech__position__c,
            "accloud_wtech__risklevel__c": accloud_wtech__risklevel__c,
            "accloud_wtech__type__c": accloud_wtech__type__c,
            "sfid": sma_sfid
        },
                               headers=self.headers)
        assert dict(res.json())["code"] == 200

    def add_separate_account_model(self, accloud_wtech__custodians__c, accloud_wtech__mmanager__c,
                                   accloud_wtech__modelname__c, accloud_wtech__position__c, accloud_wtech__risklevel__c,
                                   accloud_wtech__type__c):
        url = cm().read_config("REQUEST", "dev_domain") + sa()[
            'add_separate_account_model']['url']
        res = requests.request(method="post", url=url, json={
            "accloud_wtech__custodians__c": accloud_wtech__custodians__c,
            "accloud_wtech__mmanager__c": accloud_wtech__mmanager__c,
            "accloud_wtech__modelname__c": accloud_wtech__modelname__c,
            "accloud_wtech__position__c": accloud_wtech__position__c,
            "accloud_wtech__risklevel__c": accloud_wtech__risklevel__c,
            "accloud_wtech__type__c": accloud_wtech__type__c
        },
                               headers=self.headers)
        assert dict(res.json())["code"] == 200

    def add_separate_account_strategy(self, accloud_wtech__custodians__c, accloud_wtech__mmanager__c,
                                      accloud_wtech__modelname__c, accloud_wtech__position__c,
                                      accloud_wtech__risklevel__c,
                                      accloud_wtech__type__c):
        url = cm().read_config("REQUEST", "dev_domain") + sa()[
            'add_separate_account_strategy']['url']
        res = requests.request(method="post", url=url, json={
            "accloud_wtech__custodians__c": accloud_wtech__custodians__c,
            "accloud_wtech__mmanager__c": accloud_wtech__mmanager__c,
            "accloud_wtech__modelname__c": accloud_wtech__modelname__c,
            "accloud_wtech__position__c": accloud_wtech__position__c,
            "accloud_wtech__risklevel__c": accloud_wtech__risklevel__c,
            "accloud_wtech__type__c": accloud_wtech__type__c
        },
                               headers=self.headers)
        assert dict(res.json())["code"] == 200

    def get_separate_account_no_select(self):
        url = cm().read_config("REQUEST", "dev_domain") + \
              sa()[
                  'get_separate_account_no_select']['url']
        res = requests.request(method="get", url=url, headers=self.headers)
        assert dict(res.json())["code"] == 200

    def get_separate_account_by_name(self, name):
        url = cm().read_config("REQUEST", "dev_domain") + \
              sa()[
                  'get_separate_account_by_name']['url'] + name
        res = requests.request(method="get", url=url, headers=self.headers)
        assert dict(res.json())["code"] == 200

    def get_separate_account_by_money_manager_sfid(self, sfid):
        url = cm().read_config("REQUEST", "dev_domain") + \
              sa()['get_separate_account_by_money_manager_sfid']['url'] + sfid
        res = requests.request(method="get", url=url, headers=self.headers)
        time.sleep(3)
        assert dict(res.json())["code"] == 200

    def get_separate_account_by_sfid(self, sfid):
        url = cm().read_config("REQUEST", "dev_domain") + \
              sa()['get_separate_account_by_sfid']['url'] + sfid
        res = requests.request(method="get", url=url, headers=self.headers)
        assert dict(res.json())["code"] == 200

    def get_security_by_name(self, security_name):
        url = cm().read_config("REQUEST", "dev_domain") + \
              sa()['get_security_by_name']['url'] + security_name
        res = requests.request(method="get", url=url, headers=self.headers)
        assert dict(res.json())["code"] == 200

    def get_uma_by_money_manager_sfid(self, sfid):
        url = cm().read_config("REQUEST", "dev_domain") + \
              sa()[
                  'get_uma_by_money_manager_sfid']['url'] + sfid
        res = requests.request(method="get", url=url, headers=self.headers)
        assert dict(res.json())["code"] == 200

    def delete_separate_account_by_sma_sfid(self, sfid):
        url = cm().read_config("REQUEST", "dev_domain") + \
              sa()[
                  'delete_separate_account_by_sma_sfid']['url'] + sfid
        res = requests.request(method="delete", url=url, headers=self.headers)
        assert dict(res.json())["code"] == 200

    def delete_separate_account_by_model_sfid(self, sfid):
        url = cm().read_config("REQUEST", "dev_domain") + \
              sa()[
                  'delete_separate_account_by_model_sfid']['url'] + sfid
        res = requests.request(method="delete", url=url, headers=self.headers)
        assert dict(res.json())["code"] == 200

    def delete_separate_account_by_strategy_sfid(self, sfid):
        url = cm().read_config("REQUEST", "dev_domain") + \
              sa()[
                  'delete_separate_account_by_strategy_sfid']['url'] + sfid
        res = requests.request(method="delete", url=url, headers=self.headers)
        assert dict(res.json())["code"] == 200


