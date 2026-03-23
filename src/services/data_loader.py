import pandas as pd

from utils.config import Config

def load_data():
    return pd.read_csv(Config.PROCESSED_DATA_PATH)
