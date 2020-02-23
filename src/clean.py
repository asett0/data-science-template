import pandas as pd
from sklearn import decomposition
from sklearn.preprocessing import LabelEncoder()

iris = datasets.load_iris()

df = pd.DataFrame(iris.data,columns = iris.feature_names)
df["target"] = iris.target
X = df.drop(columns=["target"])

# Remove duplicated rows

# Drop columns with too much missing data
# More than 50% is good starting point
# df.drop(columns = ["DROPPED","COLUMN","LABELS"],inplate = True)

# Transform data to their correct data types

# Filling missing data with average for numerical data (imputation)

# A "null_value" for categorical data. Since missing data can also be a predictive factor

# Feature engineering

# Outlier removal

# Principal component analysis
pca = decomposition.PCA(n_components=3)
pca.fit(X)
X = pca.transform(X)

# Pickle and save
