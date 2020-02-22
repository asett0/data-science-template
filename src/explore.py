import pandas as pd
import os
from sklearn import datasets
import seaborn as sns
import logging
import numpy as np

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 500)

# Load dataset

# # File paths
# DATA_DIR = os.path.join("..","raw")
# RAW_DATA = os.path.join(DATA_DIR,"raw-data.csv")

iris = datasets.load_iris()

df = pd.DataFrame(iris.data,columns = iris.feature_names)
df["target"] = iris.target

# Text output
with open('../explore-output/info.txt',"w+") as f:
    print("First 100 rows: \n",df.head(100),"\n",file=f)
    print("Shape of data set:",df.shape,"\n",file=f)
    print("Column datatypes: \n",df.dtypes,"\n",file=f)
    print("Basic statistics: \n",df.describe(),"\n",file=f)
    print("Missing data (%): \n",(df.isnull().sum()/df.shape[0]).sort_values(ascending=False),"\n",file=f)

    # # Skewness of each numerical variable

    # # Stacked bar chart/histograms

    # # Scatter plots

    # # Box plots

    # # Seaborn distplot

    # # Heat map for correlation


# Plots and chart output

# Seaborn pairplot
sns_plot = sns.pairplot(df)
sns_plot.savefig("../explore-output/output.png")





