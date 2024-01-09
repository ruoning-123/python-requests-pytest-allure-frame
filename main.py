import pytest
from src.route.paths import *

if __name__ == '__main__':
    result_dir = "{}/test_result".format(REPORT_PATH)
    report_dir = "{}/test_report".format(REPORT_PATH)
    run_sort = ["-qvs", "--alluredir=%s" % result_dir, "--clean-alluredir",
                'test/test_amp_api/test_amp_accloud_api/test_money_manager.py::Test_MoneyManager']
    # pytest.main(["-qvs", "--alluredir=%s" % result_dir, "--clean-alluredir", "{}\\test_amp_api\\test_amp_accloud_api\\test_cascading_update.py".format(TESTCASE_PATH)])
    pytest.main(run_sort)
    os.system("allure generate --clean %s -o %s" % (result_dir, report_dir))
    # os.system('allure open %s' % report_dir)
