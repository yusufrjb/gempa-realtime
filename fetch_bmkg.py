import requests
import pandas as pd
import datetime

URL = "https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json"
CSV_FILE = "bmkg_earthquake_data.csv"

def fetch_earthquake():
    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()["Infogempa"]["gempa"]

    record = {
        "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "tanggal": data.get("Tanggal"),
        "jam": data.get("Jam"),
        "lintang": data.get("Lintang"),
        "bujur": data.get("Bujur"),
        "magnitudo": data.get("Magnitude"),
        "kedalaman": data.get("Kedalaman"),
        "wilayah": data.get("Wilayah"),
        "potensi": data.get("Potensi"),
    }

    try:
        df = pd.read_csv(CSV_FILE)
    except FileNotFoundError:
        df = pd.DataFrame(columns=record.keys())

    # Hindari duplikasi jika gempa sama
    if not ((df["tanggal"] == record["tanggal"]) & (df["jam"] == record["jam"])).any():
        df = pd.concat([df, pd.DataFrame([record])], ignore_index=True)
        df.to_csv(CSV_FILE, index=False)
        print("✅ Data baru ditambahkan")
    else:
        print("⚠️ Data sudah ada, tidak ditambahkan ulang")

if __name__ == "__main__":
    fetch_earthquake()
