from mysql.connector import Error, connect

def delete_DATABASE():
    database_nome = "shop_online"
    query_delete_db = f"DROP DATABASE {database_nome}"
    try: 
        with connect(
            host = "localhost",
            user = "python",
            password = "password"
        ) as connection:

            #Cancellare DATABASE
            with connection.cursor() as cursor:
                cursor.execute(query_delete_db)
    except Error as e:
        print(e)
