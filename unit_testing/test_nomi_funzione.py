from nomi_funzione import formattare_nomi

def test_nome_cognome_formattazione():
    """Confermare la formattazione di un nome normale:
    john
    thomas
    """
    nomi_formattati = formattare_nomi("john", "thomas")
    assert nomi_formattati == "TYPO John Thomas"