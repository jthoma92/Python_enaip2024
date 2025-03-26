from mysql.connector import Error, connect

popolare_tabella_articoli = """
NSERT INTO articoli (nome, descrizione, prezzo) VALUES
('Smartphone', 'Samsung smartphone', 599.99),
('T-shirt', 'Tshirt di moda', 19.99),
('Monopoly (Edizione Star Wars)', 'Il classico gioco da tavolo con tema star wars', 129.99),
('Python Crash Course', 'Un libro completo per imparare a programmare in Python', 29.99),
('Laptop', 'Laptop Asus', 899.99),
('Jeans', 'Jeans standard', 49.99),
('Accessori Gatti', 'Set dei tiragraffi e giocatoli', 39.99),
('Film DVD', 'Film a caso', 14.99);"""
def Popolare_DATABASE(database_nome):
#Popolare tabelle del DATABASE
    try: 
        with connect(
            host = "localhost",
            user = "python",
            password = "password",
            database = database_nome
        ) as connection:
            #CREATE DATABASE
            with connection.cursor() as cursor:
                cursor.execute(tabella_articoli)
                cursor.execute(tabella_customer)
                cursor.execute(tabella_ordini)
                cursor.execute(tabella_carrello)
    except Error as e:
        print(e)

