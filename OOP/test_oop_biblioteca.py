from oop_biblioteca import Libro, Utente, Biblioteca

def test_Libro_prendere_in_prestito():

    """Confermare che il metodo prendere in prestito funzione
    """

    test_libro = Libro("john", "thomas", 123) #Creare nuovo libro per il test
    assert test_libro.prendere_in_prestito() == True
    assert test_libro.prendere_in_prestito() == False   #Dovrebbe essere falso subito dopo è stato preso in prestito

def test_Libro_restituire_libro():

    test_libro = Libro("john", "thomas", 123) #Creare nuovo libro per il test
    test_libro.restituire()
    assert test_libro.disponibile == True
    #bisogna prendere in prestito un libro
    test_libro.prendere_in_prestito()
    test_libro.restituire() 
    assert test_libro.disponibile == True

def test_Utente_prendere_in_prestito():
    test_libro = Libro("IT", "Stephen King", 1350)     
    test_utente = Utente("Massimiliano", "De Bei", "U2")
    test_utente2 = Utente("John", "Thomas", "U1")
    test_utente.prendere_libro_in_prestito(test_libro)

    assert test_libro.disponibile == False
    assert test_libro.titolo in test_utente.libri_presi

    test_utente2.prendere_libro_in_prestito(test_libro)
    assert test_libro.disponibile == False
    assert test_libro.titolo not in test_utente2.libri_presi

def test_Utente_restituire_libro():
    test_libro = Libro("IT", "Stephen King", 1350)     
    test_utente = Utente("Massimiliano", "De Bei", "U2")
    test_utente2 = Utente("John", "Thomas", "U1")
    test_utente.prendere_libro_in_prestito(test_libro)
    test_utente.restituire_libro(test_libro)

    assert test_libro.titolo not in test_utente.libri_presi
    assert test_libro.disponibile == True

    test_utente2.prendere_libro_in_prestito(test_libro)
    assert test_libro.titolo in test_utente2.libri_presi
    assert test_libro.disponibile == False

def test_Biblioteca_aggiungere_libro():

    """Confermare che il metodo per aggiungere un libro funziona
    """
    
    biblioteca_test = Biblioteca("Biblioteca Python")
    test_libro = Libro("john", "thomas", 123) #Creare nuovo libro per il test
    assert biblioteca_test.aggiungere_libro(test_libro) == True
    assert test_libro.titolo in biblioteca_test.libri
    assert biblioteca_test.aggiungere_libro(test_libro) == False

def test_Biblioteca_aggiungere_utente():
    
    biblioteca_test = Biblioteca("Biblioteca Python")
    test_utente = Utente("Massimiliano", "De Bei", "U2")

    assert biblioteca_test.aggiungere_utente(test_utente) == True
    assert test_utente.id_utente in biblioteca_test.utenti
    assert biblioteca_test.aggiungere_utente(test_utente) == False

def test_Biblioteca_trovare_libro_con_titolo():
        biblioteca_test = Biblioteca("Biblioteca Python")

        test_libro = Libro("test", "thomas", 1233) #Creare nuovo libri per il test
        test_libro2 = Libro("asdf", "John", 12223) 
        test_libro3 = Libro("Is this a book", "Francesco", 1) 
        test_libro4 = Libro("Cujo", "Stephen King", 10) 
        test_libro5 = Libro("xyz", "asdf", 123331) 
        
        biblioteca_test.aggiungere_libro(test_libro)  #aggiungere libri
        biblioteca_test.aggiungere_libro(test_libro2)
        biblioteca_test.aggiungere_libro(test_libro3)
        biblioteca_test.aggiungere_libro(test_libro4)
        biblioteca_test.aggiungere_libro(test_libro5)

#Bisogna trovare un modo per paragonare stringhe in minuscole per le condizioni, se no questi assert falliscono

        assert biblioteca_test.trovare_libro_con_titolo("test") == True
        assert biblioteca_test.trovare_libro_con_titolo("ASDF") == True
        assert biblioteca_test.trovare_libro_con_titolo("is this a Book") == True
        assert biblioteca_test.trovare_libro_con_titolo("Stephen King") == False
        assert biblioteca_test.trovare_libro_con_titolo("asdf239sdlk") == False


 


def test_Biblioteca_trovare_libro_con_autore():
    pass

