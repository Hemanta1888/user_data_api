import pymysql

user = 'root'
password = 'Hemanta@211621'
db_name = 'api'

conn = pymysql.connect(
        host='localhost',
        user=user,
        password=password,
        db=db_name,
        )
cursor = conn.cursor()


__tablename__ = 'user_data'
query = "CREATE TABLE IF NOT EXISTS user_data (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name  VARCHAR(100), email VARCHAR(250), place varchar(100))"  # noqa
cursor.execute(query)
