from pathlib import Path
import json

percorso = Path('eq_data\eq_1_day_m1.geojson')
contenuti = percorso.read_text(encoding='utf-8')
tutti_eq_dati = json.loads(contenuti)

percorso = Path('eq_data\leggibile_eq_1_day_m1.geojson')
contenuti_leggibili = json.dumps(tutti_eq_dati, indent=4)
percorso.write_text(contenuti_leggibili)

