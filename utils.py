
import pandas as pd
import os

def load_csv_data(symbol, data_dir="stock_data_csvs"):

    try:
        path = os.path.join(data_dir, f"{symbol}.csv")
        df = pd.read_csv(path, parse_dates=["Date"], index_col="Date")
        return df
    except FileNotFoundError:
        return None
