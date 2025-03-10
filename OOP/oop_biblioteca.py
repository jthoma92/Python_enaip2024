# Gestione di una biblioteca:

# Creare un sistema per gestire libri e utenti in un programma di una biblioteca

# Classi da creare:

# 1. Libro
    # - attributi: titolo, autore, numero di pagine, disponbile (boolean)
    # - metodi __init__, prendere_in_prestito, restituire

# 2. Utente 
    # - Attributi: nome, cognome, id_utente, libri_prese (lista)
    # - Metodi: __init__, prendere_in_prestito_libro, restituire_libro
 
# 3. Biblioteca
    # - Attributi: Libri (dizionario - usare il nome del libro come chiave, 
    # e il Libro oggetto come valore), Utenti (dizionario con Utente ID come chiave,
    # e il Utente Oggetto come valore))
    # Metodi: aggiungere_libro, aggiungere_utente, trovare_libro, trovare_utente

class Libro:

    "Classe per rappresentare libri in biblioteca"
    
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
        self.disponibile = True

    def __str__(self):
        return f"Libro: {self.titolo} di {self.autore} contiene {self.pagine} pagine"

    def prendere_in_prestito(self):
        if self.disponibile == True:
            self.disponibile = False
            return True  #vuol dire che il libro è stato preso 
        return False   # falso: non è stato preso

    def restituire(self):
        self.disponibile = True
        return f"Libro {self.titolo} adesso è disponibile"

class Utente:
    
    """Classe che rappresenta gli utenti di una biblioteca.
        Possono prendere in prestito e restituire libri"""

    def __init__(self, nome, cognome, id_utente):
        self.nome = nome
        self.cognome = cognome
        self.id_utente = id_utente
        self.libri_presi = []

    def prendere_libro_in_prestito(self, libro):
        if libro.prendere_in_prestito() == True:
            self.libri_presi.append(libro.titolo)
            return f"Utente {self.id_utente} ha preso il libro {libro.titolo} in prestito"
        return f"Libro: {libro.titolo} non disponibile"         

    def restituire_libro(self, libro):
        if libro.titolo in self.libri_presi:
            self.libri_presi.remove(libro.titolo)
            return libro.restituire()
        return f"Utente {self.id_utente} non ha attualmente il libro: {libro.titolo}, non possibile restituirlo"

# codice per il testing delle classi

libro1 = Libro("Il Signore Degli Anelli", "JRR Tolkien", 405)  
libro2 = Libro("IT", "Stephen King", 1350)  
libro3 = Libro("East of Eden", "John Steinbeck", 700)  

utente1 = Utente("John", "Thomas", "U1")
utente2 = Utente("Massimiliano", "De Bei", "U2")

print(utente1.prendere_libro_in_prestito(libro1))
print(utente1.prendere_libro_in_prestito(libro2))
print(utente2.prendere_libro_in_prestito(libro3))
print(utente2.prendere_libro_in_prestito(libro1))   #Problema - questo libro è gia in prestito
print(utente1.libri_presi)
print(utente2.libri_presi)
print(utente1.restituire_libro(libro1))
print(utente1.restituire_libro(libro3))   # Problema - non ha questo libro da restituire
print(utente1.libri_presi)

