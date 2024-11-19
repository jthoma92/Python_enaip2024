import random

"""
 2) Programma Magic 8 Ball:
  - Definite una lista con 8 risposte nello stile Magic 8 Ball
  - Prendete input da un utente: chiedete all'utente di inserire una domanda (di solito si o no)
  - Il programma scelgie casualmente una risposta dalla tua lista e risponde con questa all'utente.
  """


palla_magica_risposte = [
    "Per quanto posso vedere, sì",
    "È certo",
    "È decisamente così",
    "Rifai la domanda più tardi",
    "Non posso predirlo ora",
    "Non ci contare",
    "Le prospettive non sono buone",
    "La mia risposta è no",
    "È difficile rispondere, prova di nuovo",
    "Ci puoi contare",
    "Sì, senza dubbio",
    "Concentrati e rifai la domanda"
]

input_utente = ""
while True:
    input_utente = input("Chiedete del futuro alla palla magica 8:\n....o scrivete exit per uscire\n")
    if input_utente.lower() == "exit":
        break
    print(palla_magica_risposte[random.randint(0, len(palla_magica_risposte) - 1)])
