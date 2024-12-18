from pathlib import Path
import matplotlib.pyplot as plt
import csv
from datetime import datetime

path = Path('weather_data\sitka_weather_2021_simple.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for indice, header in enumerate(header_row):
    print(indice, header)

#Da convertire le temperature alte e basse in celsius (sono in fahrenheit)
alte, basse, date = [], [], []
for riga in reader:
    alta = int(riga[4])
    alte.append(alta)
    bassa = int(riga[5])
    basse.append(bassa)
    data = datetime.strptime(riga[2], '%Y-%m-%d')
    date.append(data)

plt.style.use('seaborn-v0_8-notebook')
fig, ax = plt.subplots()
ax.plot(date, alte, color = 'red')
ax.plot(date, basse, color = 'blue')
ax.fill_between(date, alte, basse, facecolor='purple', alpha=0.2)

#impostare nome del grafico e assi
ax.set_title("Temperature altee basse, 2021", fontsize=24)
ax.set_xlabel("Data", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperatura (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
