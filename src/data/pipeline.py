from pathlib import Path

from data.download import download_data
from data.clean import clean_data
from utils.config import Config


def run_pipeline():
    raw_path = download_data()
    df = clean_data(raw_path)
    Path("data/processed").mkdir(parents=True, exist_ok=True)
    df.to_csv(Config.PROCESSED_DATA_PATH, index=False)
    return df
