import pymysql

class mysql_connect:
    db_config = {
        "host": "localhost",
        "port": 3306,                   # fixed: integer
        "user": "root",
        "password": "apurbaict"
        # "database": "your_db_name"    # optional
    }

    def connect_db(self):
        self.db_conn = pymysql.connect(**self.db_config)

    def execute_query(self, query_str, param=None):
        with self.db_conn.cursor() as cursor:  # fixed: db_conn
            cursor.execute(query_str, param)
            result = cursor.fetchall()
            return result

    def close_connection(self):
        self.db_conn.close()
