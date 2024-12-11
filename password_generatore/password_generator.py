#!/usr/bin/python

import random
import sys

password_chars = '1234567890'\
                '!$%&/()=+*^#@'\
                'abcdefghijklmnopqrstuvwxyz'\
                'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def prendere_password_lunghezza():
    password_lunghezza = ''
    while type(password_lunghezza) != int:
        password_lunghezza = input("Inserite la lunghezza di password, o exit per uscire:\n\t")
        try:
            password_lunghezza = int(password_lunghezza)
        except ValueError:
            if password_lunghezza.lower() == "exit":
                break
            print("Input non era del tipo INT - scrivete un numero intero per continuare\n")            
    return password_lunghezza

def generare_random_pass(lunghezza:int):
    random_password = ''
    for char in range(lunghezza):
        random_password += random.choice(password_chars)
    return random_password

#codice che si esegue solo quando eseguito come script (importazione del codice non eseguirà questo)
if __name__ == "__main__":
    #da aggiungere logica qui per prendere argomenti via sys.argv
    p_lunghezza = prendere_password_lunghezza()  
    if p_lunghezza == "exit":
        print("Uscendo dal programma...")
    else: 
        print(generare_random_pass(p_lunghezza))
