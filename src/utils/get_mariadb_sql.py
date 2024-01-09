#!/usr/bin/python
import psycopg2
from src.utils.config_data import ConfigMethod as CM

# 打开数据库连接
db = psycopg2.connect(
    host=CM().read_config("MARIADB", "host"),
    port=CM().read_config("MARIADB", "port"),
    user=CM().read_config("MARIADB", "user"),
    password=CM().read_config("MARIADB", "password"),
    database=CM().read_config("MARIADB", "database")
    # database='development'
)


def get_sql_data(sql):
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sql)
    # 使用 fetchone() 方法获取单条数据.
    results = cursor.fetchone()
    # 关闭数据库连接
    return results
    # db.close()


if __name__ == '__main__':
    print(get_sql_data('select version()'))
