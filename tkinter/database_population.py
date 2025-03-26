from mysql.connector import Error, connect

def creare_DATABASE(database_nome):
    
    query_create_db = f"CREATE DATABASE {database_nome}"

    tabella_articoli = """
    CREATE TABLE articoli (
        id_articolo INT NOT NULL AUTO_INCREMENT,
        nome VARCHAR(100) NOT NULL,
        descrizione VARCHAR(250),
        prezzo DECIMAL NOT NULL,
        PRIMARY KEY (id_articolo)
        )
    """

    tabella_customer = """
    CREATE TABLE customer (
        id_customer INT NOT NULL AUTO_INCREMENT,
        nome VARCHAR(100) NOT NULL,
        cognome VARCHAR(100) NOT NULL,
        PRIMARY KEY (id_customer)
        )
    """

    tabella_ordini = """
    CREATE TABLE ordini (
        id_ordine INT NOT NULL AUTO_INCREMENT,
        id_customer INT NOT NULL,
        data_ordine DATE NOT NULL,
        totale DECIMAL NOT NULL,
        PRIMARY KEY (id_ordine),
        FOREIGN KEY (id_customer) REFERENCES customer(id_customer)
        )
    """

    tabella_carrello = """
    CREATE TABLE carrello (
        id_carrello INT NOT NULL AUTO_INCREMENT,
        id_articolo INT NOT NULL,
        id_ordine INT NOT NULL,
        PRIMARY KEY (id_carrello),
        FOREIGN KEY (id_articolo) REFERENCES articoli(id_articolo),
        FOREIGN KEY (id_ordine) REFERENCES ordini(id_ordine)
        )
    """
    #database_nome = input("Inserite nome database da creare: ")

    #Creare DATABASE
    try: 
        with connect(
            host = "localhost",
            user = "python",
            password = "password"
        ) as connection:

            #CREATE DATABASE
            with connection.cursor() as cursor:
                cursor.execute(query_create_db)
    except Error as e:
        print(e)

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

