from pathlib import Path
import requests
from config import Config

def download_data():
    response = requests.get(Config.DATA_URL)
    response.raise_for_status()

    data_path = Path("data/raw")
    data_path.mkdir(parents=True, exist_ok=True)

    with open(data_path / "fuel_prices.csv", "wb") as f:
        f.write(response.content)

if __name__ == "__main__":
    download_data()
