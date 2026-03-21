from download import download_data
from clean import clean_data
from utils.config import Config

def run_pipeline():
    raw_path = download_data()
    df = clean_data(raw_path)
    df.to_csv(Config.PROCESSED_DATA_PATH, index=False)

if __name__ == "__main__":
    run_pipeline()
