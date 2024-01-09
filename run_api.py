import pytest
from src.route.paths import *
from src.utils.token import get_token

result_dir = "{}/test_result".format(REPORT_PATH)
report_dir = "{}/test_report".format(REPORT_PATH)


def run_amp_api_items():
    mm = 'test/test_amp_api/test_amp_accloud_api/test_money_manager.py::Test_MoneyManager::'
    sa = 'test/test_amp_api/test_amp_accloud_api/test_separate_account.py::Test_SeparateAccount::'
    cu = 'test/test_amp_api/test_amp_accloud_api/test_cascading_update.py::Test_CascadingUpdate::'
    pd = 'test/test_amp_api/test_amp_accloud_api/test_product_detail.py::Test_ProductDetail::'

    run_sort = ["-qvs", "--alluredir=%s" % result_dir, "--clean-alluredir",
                mm + str('test_add_money_manager'), mm + str('test_update_money_manager'),
                mm + str('test_get_money_manager_by_name'), mm + str('test_get_money_manager_by_sfid'),
                sa + str('test_add_separate_account_sma'), sa + str('test_update_separate_account_sma'),
                sa + str('test_add_separate_account_model'), sa + str('test_add_separate_account_strategy'),
                cu + str('test_add_cascading_update_sma'),
                cu + str('test_add_cascading_update_model'),
                cu + str('test_get_cascading_update_by_sma_sfid'),
                cu + str('test_get_cascading_update_by_model_sfid'),
                cu + str('test_delete_cascading_update_by_model_sfid'),
                cu + str('test_delete_cascading_update_by_sma_sfid'),
                sa + str('test_get_separate_account_no_select'),
                sa + str('test_get_separate_account_by_money_manager_sfid'),
                sa + str('test_get_separate_account_by_name'), sa + str('test_get_separate_account_by_sfid'),
                sa + str('test_get_security_by_name'), sa + str('test_get_uma_by_money_manager_sfid'),
                sa + str('test_delete_separate_account_by_sma_sfid'),
                sa + str('test_delete_separate_account_by_model_sfid'),
                pd + str('test_add_product_detail'),
                pd + str('test_update_product_detail'),
                pd + str('test_get_product_detail_by_strategy_sfid'),
                pd + str('test_delete_product_detail_by_sfid'),
                sa + str('test_delete_separate_account_strategy'),
                mm + str('test_delete_money_manager_by_sfid')
                ]
    pytest.main(run_sort)
    os.system("allure generate --clean %s -o %s" % (result_dir, report_dir))


# if __name__ == '__main__':
#     result_dir = "{}/test_result".format(REPORT_PATH)
#     report_dir = "{}/test_report".format(REPORT_PATH)
#     run_sort = ["-qvs", "--alluredir=%s" % result_dir, "--clean-alluredir",
#                 'test/test_amp_api/test_amp_accloud_api/test_money_manager.py::Test_MoneyManager::test_add_money_manager',
#                 'test/test_amp_api/test_amp_accloud_api/test_separate_account.py::Test_SeparateAccount::test_add_separate_account_sma']
#     pytest.main(run_sort)
#     os.system("allure generate --clean %s -o %s" % (result_dir, report_dir))
if __name__ == '__main__':
    get_token()
    run_amp_api_items()
