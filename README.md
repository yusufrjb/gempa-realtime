
# Gempa Realtime

[![Fetch BMKG Earthquake Data](https://github.com/yusufrjb/gempa-realtime/actions/workflows/bmkg_earthquake.yml/badge.svg)](https://github.com/YOUR_USERNAME/gempa-realtime/actions/workflows/bmkg_earthquake.yml)

**Gempa Realtime** is an automated project that fetches the latest earthquake data from [BMKG](https://bmkg.go.id) (Indonesian Agency for Meteorology, Climatology and Geophysics) and periodically stores it in a CSV file. Data is updated every **10 minutes** via GitHub Actions.

## Features

- Fetches real-time earthquake data from BMKG's official API
- Stores earthquake history in CSV format (`data/bmkg_latest.csv`)
- Runs automatically every 10 minutes via GitHub Actions
- Supports manual execution at any time
- Includes: date, time, coordinates, magnitude, depth, region, and felt reports

## Data Fields

| Field       | Description                            |
|-------------|----------------------------------------|
| Tanggal     | Date of the earthquake                 |
| Jam         | Time of the earthquake (WIB)           |
| Lintang     | Latitude coordinate                    |
| Bujur       | Longitude coordinate                   |
| Magnitude   | Earthquake magnitude (Richter scale)   |
| Kedalaman   | Earthquake depth (km)                  |
| Wilayah     | Epicenter location                     |
| Dirasakan   | Felt earthquake reports (MMI scale)    |

## Usage

### Prerequisites

- Python 3.6+
- pip (Python package manager)

### Installation

```bash
git clone https://github.com/YOUR_USERNAME/gempa-realtime.git
cd gempa-realtime
pip install -r requirements.txt
```

### Running Manually

```bash
python fetch_bmkg.py
```

The file `data/bmkg_latest.csv` will be created or updated automatically.

## Automation

This project uses **GitHub Actions** to run the script every 10 minutes automatically. The workflow will:

1. Checkout the repository
2. Setup Python 3.11
3. Install dependencies
4. Run `fetch_bmkg.py`
5. Commit and push the latest data

To run the workflow manually, go to the **Actions** tab > **Fetch BMKG Earthquake Data** > **Run workflow**.

## Data Source

Earthquake data is sourced from **BMKG (Badan Meteorologi, Klimatologi, dan Geofisika)** via:
```
https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json
```

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
