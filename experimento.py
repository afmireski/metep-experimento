import pandas as pd

import matplotlib.pyplot as plt
from functools import reduce

datasets = ['ethereum', 'bitcoin']
dataframes = []

# Read BigQuery CSV data
for dataset in datasets:
    df = pd.read_csv(f'data/{dataset}-transactions.csv', index_col=0, parse_dates=True)
    dataframes.append(df.rename(columns={'txn_count':f'{dataset}_txn'})) # Rename default column name to eth_txn


txn_df = reduce(lambda left,right: pd.merge(left, right, on='timestamp1'),dataframes)  # Merge all datasets

txn_df.plot(kind='line')
plt.xlabel('Time')
plt.ylabel('Txs Count')
plt.show()