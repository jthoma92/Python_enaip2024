from nomi_funzione import formattare_nomi

while True:
    print('\nInserire "q" per uscire a qualsiasi momento....')
    nome = input("\nInserire il nome:  ")
    if nome == "q":
        break
    cognome = input("\nInserire il cognome:  ")
    if nome == "q": 
        break

    nome_cognome_formattato = formattare_nomi(nome, cognome)
    print(f"Nomi ben formattati: {nome_cognome_formattato}")
