import allure
import inspect
from src.utils.get_log import *
from src.api.amp_api.amp_accloud_api.separate_account import SeparateAccount
from src.utils.get_mariadb_sql import get_sql_data
from src.utils.yaml_data import get_separate_account_content as sa
from src.utils.yaml_data import get_money_manager_content as mm


# @pytest.mark.skip
@allure.epic('amp_accloud_api')
@allure.feature('amp_accloud_api')
@allure.story('separate_account')
# 设置测试用例的标签, 可以设置多个
@allure.tag("amp接口测试", "重要")
class Test_SeparateAccount:
    # @pytest.mark.skip
    @allure.title('test_add_separate_account_sma')
    @allure.severity("critical")
    def test_add_separate_account_sma(self):
        name = mm()['add_money_manager']['name']
        accloud_wtech__category__c = sa()['add_separate_account_sma']['accloud_wtech__category__c']
        accloud_wtech__custodians__c = sa()['add_separate_account_sma']['accloud_wtech__custodians__c']
        accloud_wtech__mmanager__c = \
            get_sql_data("select sfid from development.t_wtech_money_manager where name ='{}';".format(name))[0]
        accloud_wtech__modelname__c = sa()['add_separate_account_sma']['accloud_wtech__modelname__c']
        accloud_wtech__position__c = sa()['add_separate_account_sma']['accloud_wtech__position__c']
        accloud_wtech__risklevel__c = sa()['add_separate_account_sma']['accloud_wtech__risklevel__c']
        accloud_wtech__type__c = sa()['add_separate_account_sma']['accloud_wtech__type__c']
        SeparateAccount().add_separate_account_sma(accloud_wtech__category__c, accloud_wtech__custodians__c,
                                                   accloud_wtech__mmanager__c,
                                                   accloud_wtech__modelname__c, accloud_wtech__position__c,
                                                   accloud_wtech__risklevel__c,
                                                   accloud_wtech__type__c)
        log_info("执行  " + inspect.stack()[0][3])

    # @pytest.mark.skip
    @allure.title('test_update_separate_account_sma')
    @allure.severity("critical")
    def test_update_separate_account_sma(self):
        name = mm()['add_money_manager']['name']
        accloud_wtech__category__c = sa()['update_separate_account_sma']['accloud_wtech__category__c']
        accloud_wtech__custodians__c = sa()['update_separate_account_sma']['accloud_wtech__custodians__c']
        accloud_wtech__mmanager__c = \
            get_sql_data("select sfid from development.t_wtech_money_manager where name ='{}';".format(name))[0]
        accloud_wtech__modelname__c = sa()['update_separate_account_sma']['accloud_wtech__modelname__c']
        accloud_wtech__position__c = sa()['update_separate_account_sma']['accloud_wtech__position__c']
        accloud_wtech__risklevel__c = sa()['update_separate_account_sma']['accloud_wtech__risklevel__c']
        accloud_wtech__type__c = sa()['update_separate_account_sma']['accloud_wtech__type__c']
        sma_sfid = get_sql_data(
            "select sfid from development.t_wtech_separateaccount where mmanager ='{}'  and type = 'Separate Account';".format(
                accloud_wtech__mmanager__c))[0]
        SeparateAccount().update_separate_account_sma(accloud_wtech__category__c, accloud_wtech__custodians__c,
                                                      accloud_wtech__mmanager__c,
                                                      accloud_wtech__modelname__c, accloud_wtech__position__c,
                                                      accloud_wtech__risklevel__c,
                                                      accloud_wtech__type__c, sma_sfid)
        log_info("执行  " + inspect.stack()[0][3])

    # @pytest.mark.skip
    @allure.title('test_add_separate_account_model')
    @allure.severity("critical")
    def test_add_separate_account_model(self):
        name = mm()['add_money_manager']['name']
        accloud_wtech__custodians__c = sa()['add_separate_account_model']['accloud_wtech__custodians__c']
        accloud_wtech__mmanager__c = \
            get_sql_data("select sfid from development.t_wtech_money_manager where name ='{}';".format(name))[0]
        accloud_wtech__modelname__c = sa()['add_separate_account_model']['accloud_wtech__modelname__c']
        accloud_wtech__position__c = sa()['add_separate_account_model']['accloud_wtech__position__c']
        accloud_wtech__risklevel__c = sa()['add_separate_account_model']['accloud_wtech__risklevel__c']
        accloud_wtech__type__c = sa()['add_separate_account_model']['accloud_wtech__type__c']
        SeparateAccount().add_separate_account_model(accloud_wtech__custodians__c,
                                                     accloud_wtech__mmanager__c,
                                                     accloud_wtech__modelname__c, accloud_wtech__position__c,
                                                     accloud_wtech__risklevel__c,
                                                     accloud_wtech__type__c)
        log_info("执行  " + inspect.stack()[0][3])

    # @pytest.mark.skip
    @allure.title('test_add_separate_account_strategy')
    @allure.severity("critical")
    def test_add_separate_account_strategy(self):
        name = mm()['add_money_manager']['name']
        accloud_wtech__custodians__c = sa()['add_separate_account_strategy']['accloud_wtech__custodians__c']

        accloud_wtech__mmanager__c = get_sql_data(
            "select sfid from development.t_wtech_money_manager where name ='{}'".format(name))[0]
        accloud_wtech__modelname__c = sa()['add_separate_account_strategy']['accloud_wtech__modelname__c']
        accloud_wtech__position__c = sa()['add_separate_account_strategy']['accloud_wtech__position__c']
        accloud_wtech__risklevel__c = sa()['add_separate_account_strategy']['accloud_wtech__risklevel__c']
        accloud_wtech__type__c = sa()['add_separate_account_strategy']['accloud_wtech__type__c']

        SeparateAccount().add_separate_account_model(accloud_wtech__custodians__c,
                                                     accloud_wtech__mmanager__c,
                                                     accloud_wtech__modelname__c, accloud_wtech__position__c,
                                                     accloud_wtech__risklevel__c,
                                                     accloud_wtech__type__c)
        log_info("执行  " + inspect.stack()[0][3])

    # @pytest.mark.skip
    @allure.title('test_get_separate_account_no_select')
    @allure.severity("normal")
    def test_get_separate_account_no_select(self):
        SeparateAccount().get_separate_account_no_select()
        log_info("执行  " + inspect.stack()[0][3])

    # @pytest.mark.skip
    @allure.title('test_get_separate_account_by_money_manager_sfid')
    @allure.severity("normal")
    def test_get_separate_account_by_money_manager_sfid(self):
        name = mm()['add_money_manager']['name']
        sfid = get_sql_data("select sfid from development.t_wtech_money_manager where name ='{}'".format(name))[0]
        SeparateAccount().get_separate_account_by_money_manager_sfid(sfid)
        log_info("执行  " + inspect.stack()[0][3])

    # @pytest.mark.skip
    @allure.title('test_get_separate_account_by_name')
    @allure.severity("normal")
    def test_get_separate_account_by_name(self):
        name = sa()['get_separate_account_by_name']['name']
        SeparateAccount().get_separate_account_by_name(name)
        log_info("执行  " + inspect.stack()[0][3])

    # @pytest.mark.skip
    @allure.title('test_get_separate_account_by_sfid')
    @allure.severity("normal")
    def test_get_separate_account_by_sfid(self):
        name = mm()['add_money_manager']['name']
        mmanager = get_sql_data("select sfid from development.t_wtech_money_manager where name ='{}'".format(name))[0]
        sfid = get_sql_data(
            "select sfid from development.t_wtech_separateaccount where mmanager ='{}' and type = 'Separate Account';".format(
                mmanager))[0]
        SeparateAccount().get_separate_account_by_sfid(sfid)
        log_info("执行  " + inspect.stack()[0][3])

    # @pytest.mark.skip
    @allure.title('test_get_security_by_name')
    @allure.severity("normal")
    def test_get_security_by_name(self):
        name = sa()['get_security_by_name']['name']
        SeparateAccount().get_security_by_name(name)
        log_info("执行  " + inspect.stack()[0][3])

    # @pytest.mark.skip
    @allure.title('test_get_uma_by_money_manager_sfid')
    @allure.severity("normal")
    def test_get_uma_by_money_manager_sfid(self):
        name = mm()['add_money_manager']['name']
        sfid = get_sql_data("select sfid from development.t_wtech_money_manager where name ='{}'".format(name))[0]
        SeparateAccount().get_uma_by_money_manager_sfid(sfid)
        log_info("执行  " + inspect.stack()[0][3])

    # @pytest.mark.skip
    @allure.title('test_delete_separate_account_sma')
    @allure.severity("critical")
    def test_delete_separate_account_by_sma_sfid(self):
        name = mm()['add_money_manager']['name']
        mmanager = get_sql_data("select sfid from development.t_wtech_money_manager where name ='{}'".format(name))[0]
        sfid = get_sql_data(
            "select sfid from development.t_wtech_separateaccount where mmanager ='{}' and type = 'Separate Account'".format(
                mmanager))[0]
        log_info(sfid)
        SeparateAccount().delete_separate_account_by_sma_sfid(sfid)
        log_info("执行  " + inspect.stack()[0][3])

    # @pytest.mark.skip
    @allure.title('test_delete_separate_account_by_model_sfid')
    @allure.severity("critical")
    def test_delete_separate_account_by_model_sfid(self):
        name = mm()['add_money_manager']['name']
        mmanager = get_sql_data("select sfid from development.t_wtech_money_manager where name ='{}'".format(name))[0]
        sfid = get_sql_data(
            "select sfid from development.t_wtech_separateaccount where mmanager ='{}' and type = 'Model'".format(
                mmanager))[0]
        SeparateAccount().delete_separate_account_by_model_sfid(sfid)
        log_info("执行  " + inspect.stack()[0][3])

    # @pytest.mark.skip
    @allure.title('test_delete_separate_account_by_strategy_sfid')
    @allure.severity("critical")
    def test_delete_separate_account_strategy(self):
        name = mm()['add_money_manager']['name']
        mmanager = get_sql_data("select sfid from development.t_wtech_money_manager where name ='{}'".format(name))[0]
        sfid = get_sql_data(
            "select sfid from development.t_wtech_separateaccount where mmanager ='{}' and type = 'Strategy';".format(
                mmanager))[0]
        SeparateAccount().delete_separate_account_by_strategy_sfid(sfid)
        log_info("执行  " + inspect.stack()[0][3])

