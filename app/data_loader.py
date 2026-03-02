import pandas as pd
DATA_PATH = "data/sales.csv"

def load_data():
    df = pd.read_csv(DATA_PATH)
    df.columns = df.columns.str.strip().str.lower()
    print("COLUMNS:", df.columns.tolist())  # 👈 add this
    return df