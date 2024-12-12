#Робота з БД
from errno import errorcode

import mysql
import mysql.connector


db_config = {
    'host': 'localhost',
    'port': 3308,
    'user': 'py213_user',
    'password': 'py213_pass',
    'database': 'py_knp_213',
    'charset': 'utf8mb4',
    'collation': 'utf8mb4_unicode_ci',
}

class Db:
    def __init__(self, config):
        if isinstance(config, dict):
            self.connection = mysql.connector.connect(**db_config)

    def get_connection(self):
        return self.connection


def main():
    try:
        db = Db({
            'host': 'localhost',
            'port': 3308,
            'user': 'py213_user',
            'password': 'py213_pass',
            'database': 'py_knp_213',
            'charset': 'utf8mb4',
            'collation': 'utf8mb4_unicode_ci',
    })
    except mysql.connector.Error as err:
        print(err)
    else:
        print("DB connected")

if __name__ == "__main__": main()




