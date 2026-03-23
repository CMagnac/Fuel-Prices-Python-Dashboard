from pathlib import Path
import requests
from utils.config import Config

def download_data():
    response = requests.get(Config.DATA_URL)
    response.raise_for_status()

    data_path = Path("data/raw")
    data_path.mkdir(parents=True, exist_ok=True)
    file_path = data_path / "fuel_prices.csv"
    
    with open(file_path, "wb") as f:
        f.write(response.content)
    return str(file_path)
