import dataset

from repository.config import MYSQL_CONN
from util import md5


def login_check(username, password):
    conn = MYSQL_CONN
    db = dataset.connect(conn)
    values = []
    for value in db['admin'].all():
        values.append((value.get('username'), value.get('password')))
    # print(values[0][0], values[0][1])
    # print(md5(password.encode('utf-8')))
    if username == values[0][0] and md5(password.encode('utf-8')) == values[0][1]:
        return True
    else:
        return False

if __name__ == '__main__':
    print(login_check('admin', 'fzk'))
