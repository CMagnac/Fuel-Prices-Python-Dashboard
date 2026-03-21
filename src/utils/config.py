"""
environment variables
"""
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class Config:
    DATA_URL = os.getenv("DATA_URL")
    DEBUG = os.getenv("DEBUG", "False") == "True"
    RAW_DATA_PATH = os.getenv("RAW_DATA_PATH", "data/raw/")
    PROCESSED_DATA_PATH = os.getenv(
        "PROCESSED_DATA_PATH",
        "data/processed/clean_prices.csv"
    )
