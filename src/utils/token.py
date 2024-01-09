from src.route.paths import CONFIG_PATH
from src.utils.config_data import ConfigMethod as cm
import requests
from configparser import ConfigParser


def get_token():
    cf = ConfigParser()
    headers = {
        "Authorization": cm().read_config("TOKEN", "authorization")
    }
    url = cm().read_config("REQUEST", "dev_domain") + cm().read_config("TOKEN", "token_url")

    res = requests.request(method="post", url=url, headers=headers)
    cf.read(CONFIG_PATH, encoding="utf-8")
    cf.set('REQUEST', 'token', dict(res.json())['data']['accessToken'])
    cf.write(open(CONFIG_PATH, 'w'))
    return
