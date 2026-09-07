from pymysql import connect


def connection():
    connection = connect(
        host="localhost",
        user="root",
        password="sai93928",
        database="rental"
    )

    return connection