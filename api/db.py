from repository.common import DbCommon
from config.config import OPTION


def insert_data(table='', data={}):
    # 先将管理员看到的table转换为数据库的table
    table = OPTION.get(table)
    dbc = DbCommon()
    import datetime
    i =datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data.update(dict(add_date=i))
    print(data)
    return dbc.set_data(table, data)


if __name__ == '__main__':
    print(insert_data('test', data=dict(value='fzk22')))

