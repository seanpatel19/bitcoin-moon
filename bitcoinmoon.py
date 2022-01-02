import pandas as pd 
from pathlib import Path

df_market_data = pd.read_csv(
    Path("/BTC-USD.csv"),
    index_col="Date")


print(df_market_data)