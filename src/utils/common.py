import requests
from src.utils.config_data import ConfigMethod as cm


# 刷新token，并写入配置文件my.ini



# 公共header
class CT:
    def __init__(self):
        self.token = cm().read_config("REQUEST", "token")
        self.headers = {
            "Authorization": "Bearer " + self.token
        }


if __name__ == '__main__':
    get_token()
