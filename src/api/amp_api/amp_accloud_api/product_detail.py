import time
import requests
from src.utils.config_data import ConfigMethod as cm
from src.utils.common import CT
from src.utils.yaml_data import get_product_detail_content as pd
from src.utils.get_mariadb_sql import get_sql_data
from src.utils.yaml_data import get_money_manager_content as mm


class ProductDetail(CT):
    def add_product_detail(self, active, portfgross1mo, sepacc):
        url = cm().read_config("REQUEST", "dev_domain") + pd()[
            'add_product_detail']['url']
        res = requests.request(method="post", url=url, json={
            'accloud_wtech__active__c': active,
            'accloud_wtech__portfgross1mo__c': portfgross1mo,
            'accloud_wtech__sepacc__c': sepacc
        },
                               headers=self.headers)
        assert dict(res.json())["code"] == 200

    def update_product_detail(self, detail_sfid, active, portfgross1mo, sepacc):
        name = mm()['add_money_manager']['name']
        mmanager = get_sql_data("select sfid from development.t_wtech_money_manager where name ='{}'".format(name))[0]
        strategy_sfid = get_sql_data(
            "select sfid from development.t_wtech_separateaccount where mmanager ='{}' and type = 'Strategy'".format(
                mmanager))[0]
        detail_sfidt = \
            get_sql_data(
                "select sfid from development.t_wtech_ampproductdetail where sepacc ='{}'".format(strategy_sfid))[
                0]
        url = cm().read_config("REQUEST", "dev_domain") + \
              pd()['update_product_detail']['url'] + detail_sfidt
        res = requests.request(method="patch", url=url, json={
            "sfid": detail_sfid,
            'accloud_wtech__active__c': active,
            'accloud_wtech__portfgross1mo__c': portfgross1mo,
            'accloud_wtech__sepacc__c': sepacc
        },
                               headers=self.headers)
        assert dict(res.json())["code"] == 200

    def get_product_detail_by_strategy_sfid(self, sfid):
        url = cm().read_config("REQUEST", "dev_domain") + \
              pd()[
                  'get_product_detail_by_strategy_sfid']['url'] + sfid
        res = requests.request(method="get", url=url, headers=self.headers)
        assert dict(res.json())["code"] == 200

    def delete_product_detail_by_sfid(self, detail_sfid):
        url = cm().read_config("REQUEST", "dev_domain") + \
              pd()[
                  'delete_product_detail_by_sfid']['url'] + detail_sfid
        res = requests.request(method="delete", url=url, headers=self.headers)
        time.sleep(3)
        assert dict(res.json())["code"] == 200
