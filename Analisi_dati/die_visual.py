import plotly.express as px
from die import Die

#create un dado di 6 lati:
primo_dado_6 = Die()
secondo_dado_6 = Die()

#Tirare il dado e salvare i risultati in una lista
risultati = []
tiri = 1000
for roll_num in range(tiri):
    tiro = primo_dado_6.roll() + secondo_dado_6.roll()
    risultati.append(tiro)

frequenze = []
risultato_massimale = primo_dado_6.num_sides + secondo_dado_6.num_sides
possibili_risultati = range(2, risultato_massimale+1)
for valore in possibili_risultati:
    frequenza = risultati.count(valore)
    frequenze.append(frequenza)

#visualizzare i risultati:
titolo = f"Risultati: tirando 2 dadi di 6 lati {tiri} volte"
labels =  {'x':'Risultato', 'y': 'Frequenza del risultato'}
fig = px.bar(x=possibili_risultati, y=frequenze, title=titolo, labels=labels)
fig.show()

#salvare grafico
#fig.write_html('2dadi_6_lati_visuale.html')