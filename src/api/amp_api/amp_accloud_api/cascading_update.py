import requests
from src.utils.config_data import ConfigMethod as cm
from src.utils.common import CT
from src.utils.yaml_data import get_cascading_update_content as cu


class CascadingUpdate(CT):
    def add_cascading_update_sma(self, sma_sfid, external_sfid, ratio):
        url = cm().read_config("REQUEST", "dev_domain") + cu()[
            'add_cascading_update_sma']['url']
        res = requests.request(method="post", url=url, json=[{
            "accloud_wtech__modelsma__c": sma_sfid,
            "accloud_wtech__sepacc__r__accloud_wtech__external_id__c": external_sfid,
            "accloud_wtech__ratio__c": ratio
        }],
                               headers=self.headers)
        assert dict(res.json())["code"] == 200

    def add_cascading_update_model(self, model_sfid,
                                   external_sfid, ratio):
        url = cm().read_config("REQUEST", "dev_domain") + cu()[
            'add_cascading_update_model']['url']
        res = requests.request(method="post", url=url, json=[{
            "accloud_wtech__modelsma__c": model_sfid,
            "accloud_wtech__sepacc__r__accloud_wtech__external_id__c": external_sfid,
            "accloud_wtech__ratio__c": ratio
        }],
                               headers=self.headers)
        assert dict(res.json())["code"] == 200

    def get_cascading_update_by_sma_sfid(self, sma_sfid):
        url = cm().read_config("REQUEST", "dev_domain") + cu()[
            'get_cascading_update_by_sma_sfid']['url'] + sma_sfid
        res = requests.request(method="get", url=url, headers=self.headers)
        assert dict(res.json())["code"] == 200

    def get_cascading_update_by_model_sfid(self, model_sfid):
        url = cm().read_config("REQUEST", "dev_domain") + cu()[
            'get_cascading_update_by_model_sfid']['url'] + model_sfid
        res = requests.request(method="get", url=url, headers=self.headers)
        assert dict(res.json())["code"] == 200

    def delete_cascading_update_by_model_sfid(self, model_sfid):
        url = cm().read_config("REQUEST", "dev_domain") + cu()[
            'delete_cascading_update_by_model_sfid']['url'] + model_sfid
        res = requests.request(method="delete", url=url, headers=self.headers)
        assert dict(res.json())["code"] == 200

    def delete_cascading_update_by_sma_sfid(self, sma_sfid):
        url = cm().read_config("REQUEST", "dev_domain") + cu()[
            'delete_cascading_update_by_sma_sfid']['url'] + sma_sfid
        res = requests.request(method="delete", url=url, headers=self.headers)
        assert dict(res.json())["code"] == 200
