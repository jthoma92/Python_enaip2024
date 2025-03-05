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
    
    disponible = True

    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def prendere_in_presito(self):
        if self.disponible == True:
            self.disponible = False
            return "Libro preso"
        return "Libro Non disponibile"

    def restituire(self):
        self.disponible = True
        return f"Libro {self.titolo} adesso è disponibile"

#libro1 = Libro("Il Signore Degli Anelli", "JRR Tolkien", 405)

#print(libro1.titolo, libro1.autore, libro1.pagine, libro1.disponible)
        