from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import pandas as pd


def run_model():

    # Import cleaned data
    iris = datasets.load_iris()

    df = pd.DataFrame(iris.data,columns = iris.feature_names)
    df["target"] = iris.target
    y = iris.target
    X = df.drop(columns=["target"])

    # K cross fold validation stratified
    # Splitting and training
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state = 0)

    model = LogisticRegression(random_state = 0)

    model.fit(X_train,y_train)

    y_pred = model.predict(X_test)

    # Performance metrics
    # Print the y_pred, Accuracy, Confusion matrix and classification report containing
    # the Recall, Precision and F-measure
    with open('../model-output/info.txt',"w+") as f:
        print("y_pred is: \n",y_pred,"\n",file=f)
        print("Accuracy:",metrics.accuracy_score(y_test,y_pred),"\n",file=f)
        print("Confusion matrix:\n",metrics.confusion_matrix(y_test,y_pred),"\n",file=f)
        print("Classification report:\n",metrics.classification_report(y_test,y_pred),"\n",file=f)