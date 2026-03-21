import pandas as pd

def clean_data(path):

    df = pd.read_csv(path, sep=";", dtype=str)

    # --- 1. Keep only useful columns ---
    columns_to_keep = [
        "id",
        "Code postal",
        "pop",
        "adresse",
        "ville",
        "geom",
        "Mise à jour des prix",
        "prix_id",
        "Prix",
        "Carburant",
        "Région",
        "Numéro Département",
        "Département",
        "Carburant en rupture",
        "Début rupture",
        "Fin rupture",
        "Automate 24-24 (oui/non)"
    ]

    df = df[columns_to_keep]

    # --- 2. Rename columns (clean names for Python) ---
    df.columns = [
        "id",
        "code_postal",
        "pop",
        "adresse",
        "ville",
        "geom",
        "date_maj",
        "prix_id",
        "prix",
        "carburant",
        "region",
        "departement_code",
        "departement",
        "carburant_rupture",
        "debut_rupture",
        "fin_rupture",
        "automate_24_24"
    ]

    # --- 3. Clean price ---
    df["prix"] = df["prix"].str.replace(",", ".")
    df["prix"] = pd.to_numeric(df["prix"], errors="coerce")

    df = df.dropna(subset=["prix"])

    # --- 4. Convert dates ---
    df["date_maj"] = pd.to_datetime(df["date_maj"], errors="coerce")
    df["debut_rupture"] = pd.to_datetime(df["debut_rupture"], errors="coerce")
    df["fin_rupture"] = pd.to_datetime(df["fin_rupture"], errors="coerce")

    # --- 5. Split geom into latitude / longitude ---
    df[["latitude", "longitude"]] = df["geom"].str.split(",", expand=True)

    df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
    df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")

    df = df.dropna(subset=["latitude", "longitude"])

    # --- 6. Clean text ---
    df["ville"] = df["ville"].str.strip().str.upper()
    df["carburant"] = df["carburant"].str.strip().str.upper()

    # --- 7. Normalize boolean column ---
    df["automate_24_24"] = df["automate_24_24"].map({
        "Oui": True,
        "Non": False
    })

    # --- 8. Remove duplicates ---
    df = df.drop_duplicates()

    return df
