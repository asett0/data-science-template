import pandas as pd
import os

# File paths
DATA_DIR = os.path.join("..","raw")
RAW_DATA = os.path.join(DATA_DIR,"raw-data.csv")

# View head of raw data
raw_data_df = pd.read_csv(RAW_DATA)
print(raw_data_df.head(100))

# View data types
print(raw_data_df.dtypes)

# Basic statistics
print(raw_data_df.describe())

# Find percentage of missing data in each column
(raw_data_df.isnull().sum()/raw_data_df.shape[0]).sort_values(ascending=False)



