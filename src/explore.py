import pandas as pd
import os
from sklearn import datasets
import seaborn as sns
import logging
import numpy as np
from matplotlib import pyplot as plt
import matplotlib


def run_explore():
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
    y = iris.target
    X = df.drop(columns=["target"])

    # Text output
    with open('../explore-output/info.txt',"w+") as f:
        print("Colums: ",list(df.columns),"\n",file=f)
        print("100 sample rows from dataframe: \n",df.sample(100,random_state=0),"\n",file=f)
        print("Shape of data set:",df.shape,"\n",file=f)
        print("Column datatypes: \n",df.dtypes,"\n",file=f)
        print("Basic statistics: \n",df.describe(),"\n",file=f)
        print("Missing data (%): \n",(df.isnull().sum()/df.shape[0]).sort_values(ascending=False),"\n",file=f)
        print("No of Observations of each target:\n",df["target"].value_counts(),"\n",file=f)
        
        # Skewness of each numerical variable

        # Stacked bar chart/histograms

        # Scatter plots

        # Seaborn joint plots

    # Plots and chart output

    # Seaborn pairplots
    plt.figure()
    sns.pairplot(df,hue="target").savefig("../explore-output/pairplot-by-Y.png")
    sns.pairplot(X).savefig("../explore-output/pairplot.png")

    # Distribution plots of individual features
    for c in X.columns:
        plt.figure()
        sns.distplot(df[c]).get_figure().savefig("../explore-output/{}-distplot.png".format(c))

    # Box plot to show outliers and percentiles
    plt.figure()
    sns.boxplot(data=X).get_figure().savefig("../explore-output/boxplot.png")

    # Heat map for correlation
    plt.figure(figsize=[10,10])
    sns.heatmap(X.corr(),annot=True).get_figure().savefig("../explore-output/correlation-heatmap.png")

    # Violin plot
