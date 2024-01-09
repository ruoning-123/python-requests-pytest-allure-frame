import allure
import inspect
from src.utils.get_log import *
from src.api.amp_api.amp_accloud_api.product_detail import ProductDetail

from src.utils.get_mariadb_sql import get_sql_data
from src.utils.yaml_data import get_product_detail_content as pd
from src.utils.yaml_data import get_money_manager_content as mm


# @pytest.mark.skip
@allure.epic('amp_accloud_api')
@allure.feature('amp_accloud_api')
@allure.story('product_detail')
# 设置测试用例的标签, 可以设置多个
@allure.tag("amp接口测试", "重要")
class Test_ProductDetail:
    # 设置测试用例的级别  blocker > critical > normal > minor > trivial
    @allure.title('test_add_product_detail')
    @allure.severity("critical")
    def test_add_product_detail(self):
        active = pd() \
            ['add_product_detail']['accloud_wtech__active__c']
        portfgross1mo = pd() \
            ['add_product_detail']['accloud_wtech__portfgross1mo__c']
        name = mm()['add_money_manager']['name']
        mmanager = get_sql_data("select sfid from development.t_wtech_money_manager where name ='{}'".format(name))[0]
        strategy_sfid = get_sql_data(
            "select sfid from development.t_wtech_separateaccount where mmanager ='{}' and type = 'Strategy'".format(
                mmanager))[0]
        ProductDetail().add_product_detail(active, portfgross1mo, strategy_sfid)
        log_info("执行  " + inspect.stack()[0][3])

    @allure.title('test_update_product_detail')
    @allure.severity("normal")
    def test_update_product_detail(self):
        name = mm()['add_money_manager']['name']
        mmanager = get_sql_data("select sfid from development.t_wtech_money_manager where name ='{}'".format(name))[0]
        strategy_sfid = get_sql_data(
            "select sfid from development.t_wtech_separateaccount where mmanager ='{}' and type = 'Strategy'".format(
                mmanager))[0]
        detail_sfid = \
            get_sql_data(
                "select sfid from development.t_wtech_ampproductdetail where sepacc ='{}'".format(strategy_sfid))[
                0]
        active = pd() \
            ['update_product_detail']['accloud_wtech__active__c']
        portfgross1mo = pd() \
            ['update_product_detail']['accloud_wtech__portfgross1mo__c']
        ProductDetail().update_product_detail(detail_sfid, active, portfgross1mo, strategy_sfid)
        log_info("执行  " + inspect.stack()[0][3])

    @allure.title('test_get_product_detail_by_strategy_sfid')
    @allure.severity("normal")
    def test_get_product_detail_by_strategy_sfid(self):
        name = mm()['add_money_manager']['name']
        mmanager = get_sql_data("select sfid from development.t_wtech_money_manager where name ='{}'".format(name))[0]
        strategy_sfid = get_sql_data(
            "select sfid from development.t_wtech_separateaccount where mmanager ='{}' and type = 'Strategy'".format(
                mmanager))[0]
        ProductDetail().get_product_detail_by_strategy_sfid(strategy_sfid)
        log_info("执行  " + inspect.stack()[0][3])

    @allure.title('test_delete_product_detail_by_sfid')
    @allure.severity("critical")
    def test_delete_product_detail_by_sfid(self):
        name = mm()['add_money_manager']['name']
        mmanager = get_sql_data("select sfid from development.t_wtech_money_manager where name ='{}'".format(name))[0]
        strategy_sfid = get_sql_data(
            "select sfid from development.t_wtech_separateaccount where mmanager ='{}' and type = 'Strategy'".format(
                mmanager))[0]
        detail_sfid = \
            get_sql_data(
                "select sfid from development.t_wtech_ampproductdetail where sepacc ='{}'".format(strategy_sfid))[
                0]
        ProductDetail().delete_product_detail_by_sfid(detail_sfid)
        log_info("执行  " + inspect.stack()[0][3])
