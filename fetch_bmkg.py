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
import os

csv_path = 'data/bmkg_latest.csv'

# Kalau file belum ada → buat baru, kalau sudah → append tanpa header
if not os.path.exists(csv_path):
    df.to_csv(csv_path, index=False)
else:
    df.to_csv(csv_path, mode='a', header=False, index=False)

