from mysql.connector import Error, connect
from getpass import getpass

database_nome = "shop_online"
query_delete_db = f"DROP DATABASE {database_nome}"

def delete_DATABASE(query):
    try: 
        with connect(
            host = "localhost",
            user = "python",
            password = "password"
        ) as connection:

            #CREATE DATABASE
            with connection.cursor() as cursor:
                cursor.execute(query)
    except Error as e:
        print(e)

if __name__ == "__main__":
    delete_DATABASE(query_delete_db)