import allure
import inspect
from src.utils.get_log import *
from src.api.amp_api.amp_accloud_api.cascading_update import CascadingUpdate
from src.utils.get_mariadb_sql import get_sql_data
from src.utils.yaml_data import get_cascading_update_content as cu
from src.utils.yaml_data import get_money_manager_content as mm


# @pytest.mark.skip
@allure.epic('amp_accloud_api')
@allure.feature('amp_accloud_api')
@allure.story('cascading update')
# 设置测试用例的标签, 可以设置多个
@allure.tag("amp接口测试", "重要")
class Test_CascadingUpdate:
    # @pytest.mark.skip
    @allure.title('test_add_cascading_update_sma')
    @allure.severity("critical")
    def test_add_cascading_update_sma(self):
        name = mm()['add_money_manager']['name']
        mmanager = get_sql_data("select sfid from development.t_wtech_money_manager where name ='{}'".format(name))[0]

        sma_sfid = get_sql_data(
            "select sfid from development.t_wtech_separateaccount where mmanager ='{}' and type = 'Separate Account'".format(
                mmanager))[0]
        external_sfid = get_sql_data(
            "select external_id from development.t_wtech_separateaccount where mmanager ='{}' and type = 'Strategy'".format(
                mmanager))[0]
        ratio = cu()['add_cascading_update_sma']['accloud_wtech__ratio__c']
        CascadingUpdate().add_cascading_update_sma(sma_sfid, external_sfid, ratio)
        log_info("执行  " + inspect.stack()[0][3])

    # @pytest.mark.skip
    @allure.title('test_add_cascading_update_model')
    @allure.severity("critical")
    def test_add_cascading_update_model(self):
        name = mm()['add_money_manager']['name']
        mmanager = get_sql_data("select sfid from development.t_wtech_money_manager where name ='{}'".format(name))[0]

        model_sfid = get_sql_data(
            "select sfid from development.t_wtech_separateaccount where mmanager ='{}' and type = 'Model'".format(
                mmanager))[0]
        external_sfid = get_sql_data(
            "select external_id from development.t_wtech_separateaccount where mmanager ='{}' and type = 'Strategy'".format(
                mmanager))[0]
        ratio = cu()['add_cascading_update_model']['accloud_wtech__ratio__c']
        CascadingUpdate().add_cascading_update_model(model_sfid, external_sfid, ratio)
        log_info("执行  " + inspect.stack()[0][3])

    # @pytest.mark.skip
    @allure.title('test_get_cascading_update_by_sma_sfid')
    @allure.severity("normal")
    def test_get_cascading_update_by_sma_sfid(self):
        name = mm()['add_money_manager']['name']
        mmanager = get_sql_data("select sfid from development.t_wtech_money_manager where name ='{}'".format(name))[0]

        sma_sfid = get_sql_data(
            "select sfid from development.t_wtech_separateaccount where mmanager ='{}' and type = 'Separate Account'".format(
                mmanager))[0]
        CascadingUpdate().get_cascading_update_by_sma_sfid(sma_sfid)
        log_info("执行  " + inspect.stack()[0][3])

    # @pytest.mark.skip
    @allure.title('test_get_cascading_update_by_model_sfid')
    @allure.severity("normal")
    def test_get_cascading_update_by_model_sfid(self):
        name = mm()['add_money_manager']['name']
        mmanager = get_sql_data("select sfid from development.t_wtech_money_manager where name ='{}'".format(name))[0]

        model_sfid = get_sql_data(
            "select sfid from development.t_wtech_separateaccount where mmanager ='{}' and type = 'Model'".format(
                mmanager))[0]
        CascadingUpdate().get_cascading_update_by_model_sfid(model_sfid)
        log_info("执行  " + inspect.stack()[0][3])

    # @pytest.mark.skip
    @allure.title('test_delete_cascading_update_by_model_sfid')
    @allure.severity("critical")
    def test_delete_cascading_update_by_model_sfid(self):
        name = mm()['add_money_manager']['name']
        mmanager = get_sql_data("select sfid from development.t_wtech_money_manager where name ='{}'".format(name))[0]

        sfid = get_sql_data(
            "select sfid from development.t_wtech_separateaccount where mmanager ='{}' and type = 'Model'".format(
                mmanager))[0]
        external_id = get_sql_data(
            "select external_id from development.t_wtech_separateaccount where mmanager ='{}' and type = 'Strategy'".format(
                mmanager))[0]
        model_sfid = get_sql_data(
            "select sfid from development.t_wtech_sma_model_relation where modelsma ='{0}' and sepacc_external_id = '{1}'".format(
                sfid, external_id))[0]
        CascadingUpdate().delete_cascading_update_by_model_sfid(model_sfid)
        log_info("执行  " + inspect.stack()[0][3])

    # @pytest.mark.skip
    @allure.title('test_delete_cascading_update_by_sma_sfid')
    @allure.severity("critical")
    def test_delete_cascading_update_by_sma_sfid(self):
        name = mm()['add_money_manager']['name']
        mmanager = get_sql_data("select sfid from development.t_wtech_money_manager where name ='{}'".format(name))[0]

        sfid = get_sql_data(
            "select sfid from development.t_wtech_separateaccount where mmanager ='{}' and type = 'Separate Account'".format(
                mmanager))[0]
        external_id = get_sql_data(
            "select external_id from development.t_wtech_separateaccount where mmanager ='{}' and type = 'Strategy'".format(
                mmanager))[0]
        sma_sfid = get_sql_data(
            "select sfid from development.t_wtech_sma_model_relation where modelsma ='{0}' and sepacc_external_id = '{1}'".format(
                sfid, external_id))[0]
        CascadingUpdate().delete_cascading_update_by_sma_sfid(sma_sfid)
        log_info("执行  " + inspect.stack()[0][3])
