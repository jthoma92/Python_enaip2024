from die import Die

#create un dado di 6 lati:
dado_6 = Die()

#Tirare il dado e salvare i risultati in una lista
risultati = []
for roll_num in range(100):
    tiro = dado_6.roll()
    risultati.append(tiro)

print(risultati)
