import allure
import inspect
from src.utils.get_log import *
from src.api.amp_api.amp_accloud_api.money_manager import MoneyManager

from src.utils.get_mariadb_sql import get_sql_data
from src.utils.yaml_data import get_money_manager_content as mm


# @pytest.mark.skip
@allure.epic('amp_accloud_api')
@allure.feature('amp_accloud_api')
@allure.story('money_manager')
# 设置测试用例的标签, 可以设置多个
@allure.tag("amp接口测试", "重要")
class Test_MoneyManager:
    # 设置测试用例的级别  blocker > critical > normal > minor > trivial
    @allure.title('test_add_money_manager')
    @allure.severity("critical")
    def test_add_money_manager(self):
        name = mm() \
            ['add_money_manager']['name']
        accloud_wtech__manager_overview__c = mm() \
            ['add_money_manager']['accloud_wtech__manager_overview__c']
        MoneyManager().add_money_manager(name, accloud_wtech__manager_overview__c)
        log_info("执行  " + inspect.stack()[0][3])

    @allure.title('test_update_money_manager')
    @allure.severity("critical")
    def test_update_money_manager(self):
        name = mm() \
            ['update_money_manager']['name']
        sfid = get_sql_data("select sfid from development.t_wtech_money_manager where name ='{}'".format(name))[0]
        accloud_wtech__manager_overview__c = mm() \
            ['update_money_manager']['accloud_wtech__manager_overview__c']
        MoneyManager().update_money_manager(sfid, name, accloud_wtech__manager_overview__c)
        log_info("执行  " + inspect.stack()[0][3])

    @allure.title('test_get_money_manager_by_name')
    @allure.severity("normal")
    def test_get_money_manager_by_name(self):
        name = mm() \
            ['get_money_manager_by_name']['name']
        MoneyManager().get_money_manager_by_name(name)
        log_info("执行  " + inspect.stack()[0][3])

    @allure.title('test_get_money_manager_by_sfid')
    @allure.severity("normal")
    def test_get_money_manager_by_sfid(self):
        name = mm() \
            ['get_money_manager_by_name']['name']
        sfid = get_sql_data(
            "select sfid from development.t_wtech_money_manager where name ='{}'".format(name))[0]
        MoneyManager().get_money_manager_by_sfid(sfid)
        log_info("执行  " + inspect.stack()[0][3])

    @allure.title('test_delete_money_manager_by_sfid')
    @allure.severity("critical")
    def test_delete_money_manager_by_sfid(self):
        name = mm()['get_money_manager_by_name']['name']
        sfid = get_sql_data(
            "select sfid from development.t_wtech_money_manager where name ='{}'".format(name))[0]
        MoneyManager().delete_money_manager_by_sfid(sfid)
        log_info("执行  " + inspect.stack()[0][3])
