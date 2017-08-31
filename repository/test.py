import dataset

from repository.config import MYSQL_CONN


def insert_phone_email(phone, email):
    conn = MYSQL_CONN
    db = dataset.connect(conn)
    values = dict(phone=phone, email=email, user='fzk')
    print(values)
    db['settings'].update(values, ['fzk'])
    print(db['settings'].all())
    # print(values)

if __name__ == '__main__':
    insert_phone_email('admin', 'fzk')
