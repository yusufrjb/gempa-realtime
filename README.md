
# Gempa Realtime

[![Fetch BMKG Earthquake Data](https://github.com/yusufrjb/gempa-realtime/actions/workflows/bmkg_earthquake.yml/badge.svg)](https://github.com/YOUR_USERNAME/gempa-realtime/actions/workflows/bmkg_earthquake.yml)

**Gempa Realtime** adalah proyek otomatis yang mengambil data gempa bumi terkini dari [BMKG](https://bmkg.go.id) (Badan Meteorologi, Klimatologi, dan Geofisika) dan menyimpannya secara periodik ke dalam file CSV. Data diperbarui setiap **10 menit** melalui GitHub Actions.

## Fitur

- Mengambil data gempa real-time dari API resmi BMKG
- Menyimpan riwayat gempa dalam format CSV (`data/bmkg_latest.csv`)
- Berjalan otomatis setiap 10 menit via GitHub Actions
- Dapat dijalankan secara manual kapan saja
- Data mencakup: tanggal, jam, koordinat, magnitudo, kedalaman, wilayah, dan laporan dirasakan

## Kolom Data

| Kolom        | Deskripsi                                |
|--------------|------------------------------------------|
| Tanggal      | Tanggal kejadian gempa                   |
| Jam          | Waktu kejadian gempa (WIB)               |
| Lintang      | Koordinat lintang                        |
| Bujur        | Koordinat bujur                          |
| Magnitude    | Kekuatan gempa (Skala Richter)           |
| Kedalaman    | Kedalaman gempa (km)                     |
| Wilayah      | Lokasi pusat gempa                       |
| Dirasakan    | Laporan gempa dirasakan (skala MMI)      |

## Cara Penggunaan

### Prasyarat

- Python 3.6+
- pip (Python package manager)

### Instalasi

```bash
git clone https://github.com/YOUR_USERNAME/gempa-realtime.git
cd gempa-realtime
pip install -r requirements.txt
```

### Menjalankan Secara Manual

```bash
python fetch_bmkg.py
```

File `data/bmkg_latest.csv` akan dibuat atau diperbarui secara otomatis.

## Otomatisasi

Proyek ini menggunakan **GitHub Actions** untuk menjalankan script setiap 10 menit secara otomatis. Workflow akan:

1. Checkout repository
2. Setup Python 3.11
3. Install dependensi
4. Menjalankan script `fetch_bmkg.py`
5. Commit dan push data terbaru ke repository

Untuk menjalankan workflow secara manual, buka tab **Actions** > **Fetch BMKG Earthquake Data** > **Run workflow**.

## Sumber Data

Data gempa bumi bersumber dari **BMKG (Badan Meteorologi, Klimatologi, dan Geofisika)** melalui endpoint:
```
https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json
```

## Lisensi

Proyek ini dilisensikan di bawah **MIT License**. Lihat file [LICENSE](LICENSE) untuk informasi lebih lanjut.
