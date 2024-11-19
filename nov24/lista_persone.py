"""
1) prende input dall'utente per memorizzare dei nomi:
 - Il sviluppatore può definire quanti nomi verrano memorizzati
 - il programma chiederà all'utente per questi nomi, tutti verrano salvati in una lista.
 - alla fine, potete ordinare la lista in ordine alfabetica per essere stampata in terminale
 - Aggiungete una funzione per trovare il nome più lungo
 - aggiungete una funzione per rimuovere un nome (metodo 
"""

import time

def popolare_lista() -> list:
    lista_di_persone = []
    for user_input in range(5):
        lista_di_persone.append(input("Inserite il nome della persona:\n"))
    return lista_di_persone

def nome_più_lunga(lista: list) -> str:
    nome_lungo = ""
    for nome in lista:
        if len(nome_lungo) < len(nome):
            nome_lungo = nome
    return nome_lungo

def rimuovere_persone(lista: list, nome_da_togliere: str) -> list:
    print(f"lista originale: {lista}")
    nuova_lista = []
    for nome in lista:
        if nome != nome_da_togliere:
            nuova_lista.append(nome)
    print(f"lista cambiata: {nuova_lista}")
    return nuova_lista

"""Una soluzione alternativa utilizza una comprensione delle liste:
nuova_lista = [valore for valore in lista if valore != nome]
"""
def rimuovere_con_comprensione(lista: list, nome_da_togliere: str) -> list:
    print(f"lista originale: {lista}")
    nuova_lista = [valore for valore in lista if valore != nome_da_togliere]
    print(f"lista cambiata: {nuova_lista}")
    return nuova_lista

#se si vuole una lista già pronta per testing, o usare funzione popolare_lista():
lista_di_persone = ["john", "michael", "thomas", "lewis", "lewis", "mevio", "john", "michael",
                    "mevio", "tizio", "caio", "sempronio", "mevio", "mevio", "sempronio", "tizio",
                    "michael", "john", "caio", "lewis", "john", "thomas", "thomas", "sempronio", "tizio"]


print(f"il nome più lungo nella lista: {nome_più_lunga(lista_di_persone)}")

start_time = time.process_time()
rimuovere_persone(lista_di_persone, input("Inserite il nome della persona da TOGLIERE:  "))
stop_time = time.process_time()
print("************************************\n"
        "PRIMO TEMPO PER CICLO CON ALGROITMO:\n"
        f"\t{stop_time - start_time}\n"
        "************************************"
        )

#seconda volta con funzione che rimuove una persona con comprensione

print(f"il nome più lungo nella lista: {nome_più_lunga(lista_di_persone)}")

start_time = time.process_time()
rimuovere_con_comprensione(lista_di_persone, input("Inserite il nome della persona da TOGLIERE:\n"))
stop_time = time.process_time()
print("************************************\n"
        "SECONDO TEMPO CON COMPRENSIONE:\n"
        f"\t{stop_time - start_time}\n"
        "************************************"
        )
    


