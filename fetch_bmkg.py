import requests
import pandas as pd
from datetime import datetime

url = "https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json"
res = requests.get(url).json()
g = res['Infogempa']['gempa']

data = {
    'Tanggal': g['Tanggal'],
    'Jam': g['Jam'],
    'Lintang': g['Lintang'],
    'Bujur': g['Bujur'],
    'Magnitude': g['Magnitude'],
    'Kedalaman': g['Kedalaman'],
    'Wilayah': g['Wilayah'],
    'Dirasakan': g['Dirasakan']
}

df = pd.DataFrame([data])
df.to_csv('data/bmkg_latest.csv', index=False)
print("Data gempa terbaru disimpan.")
