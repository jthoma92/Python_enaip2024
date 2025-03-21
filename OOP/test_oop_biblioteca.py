from oop_biblioteca import Libro, Utente, Biblioteca

def test_Libro_prendere_in_prestito():

    """Confermare che il metodo prendere in prestito funzione
    """

    test_libro = Libro("john", "thomas", 123) #Creare nuovo libro per il test
    assert test_libro.prendere_in_prestito() == True
    assert test_libro.prendere_in_prestito() == False   #Dovrebbe essere falso subito dopo è stato preso in prestito

def test_Libro_restituire_libro():

    test_libro = Libro("john", "thomas", 123) #Creare nuovo libro per il test
    assert test_libro.restituire() == True
    #bisogna prendere in prestito un libro
    test_libro.prendere_in_prestito()
    assert test_libro.restituire() == True


def test_Biblioteca_aggiungere_libro():

    """Confermare che il metodo prendere in prestito funzione
    """
    
    biblioteca_test = Biblioteca()
    test_libro = Libro("john", "thomas", 123) #Creare nuovo libro per il test
    assert biblioteca_test.aggiungere_libro(test_libro) == True
    assert test_libro in biblioteca_test.libri

    