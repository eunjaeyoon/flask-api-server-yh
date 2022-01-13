import mysql.connector

def get_connection() :
    connection = mysql.connector.connect(
        host = 'database-1.cvtuufc0they.ap-northeast-2.rds.amazonaws.com',
        database = 'movie_db',
        user = 'movie_user',
        password = '2301'
    )
    return 
