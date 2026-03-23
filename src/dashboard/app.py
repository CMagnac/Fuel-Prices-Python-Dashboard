from pathlib import Path

from dash import Dash

from data.pipeline import run_pipeline
from services.data_loader import load_data
from dashboard.layout import create_layout
from dashboard.callbacks import register_callbacks
from utils.config import Config


def main():

    # Check if data already exists
    if Path(Config.PROCESSED_DATA_PATH).exists():
        print("Using cached data...")
    else:
        print("Running data pipeline...")
        run_pipeline()

    # Load data
    print("Loading data...")
    df = load_data()

    # Start Dash app
    app = Dash(__name__)

    app.layout = create_layout(df)

    register_callbacks(app, df)

    print("Starting dashboard...")
    app.run(debug=True)


if __name__ == "__main__":
    main()
