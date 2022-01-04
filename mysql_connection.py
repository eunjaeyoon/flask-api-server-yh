import mysql.connector

def get_connection() :
    connection = mysql.connector.connect(
        host = 'database-1.cvtuufc0they.ap-northeast-2.rds.amazonaws.com',
        database = 'test',
        user = 'admin',
        password = 'dms230145'
    )
    return 