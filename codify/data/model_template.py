# load csv file
from IPython.display import display
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import pandas as pd
df = pd.read_csv("./data.csv", encoding="utf-8")

# head of dataset
df.head()

# percentage of null values


def null_columns_percentage(df) -> pd.DataFrame:
    '''
        Prints Null Information of dataframe,i.e. only the number of rows having null values and their null percentage
    '''
    print("\nNull Information of Dataframe: \n")
    null_df = pd.DataFrame(df.isnull().sum()).reset_index()
    null_df.columns = ["column_name", "null_rows"]
    null_df["null_percentage"] = null_df["null_rows"]*100 / df.shape[0]
    null_df = null_df[null_df["null_percentage"] != 0].sort_values(
        "null_percentage", ascending=False).reset_index(drop=True)
    print(
        f"\nThere are total {null_df.shape[0]} columns having null values out of {df.shape[1]} columns in dataframe\n")
    display(null_df)
    return null_df


null_columns_percentage(df)


# replace null values with their mean values
df.fillna(df.mean(), inplace=True)
print('Missing: %d' % df.isnull().sum().sum())

# dataset statistics


def columns_type(df) -> tuple:
    '''
        return number of categorical and numerical columns
    '''
    numerics = ['int16', 'int32', 'int64',
                'float16', 'float32', 'float64']
    num_cols = df.select_dtypes(include=numerics).columns.tolist()
    cat_columns = len(df.select_dtypes(
        include="O").columns.tolist())
    num_columns = len(num_cols)
    return (cat_columns, num_columns)


def null_columns_percentage(df) -> pd.DataFrame:
    '''
    Prints Null Information of dataframe,i.e. only the number of rows having null values and their null percentage
    '''
    print("\nNull Information of Dataframe: \n")
    null_df = pd.DataFrame(df.isnull().sum()).reset_index()
    null_df.columns = ["column_name", "null_rows"]
    null_df["null_percentage"] = null_df["null_rows"] * \
        100 / df.shape[0]
    null_df = null_df[null_df["null_percentage"] != 0].sort_values(
        "null_percentage", ascending=False).reset_index(drop=True)
    print(
        f"\nThere are total {null_df.shape[0]} columns having null values out of {df.shape[1]} columns in dataframe\n")
    display(null_df)
    return null_df


def statistics(df) -> None:
    '''
    Gives number of categorical and numerical columns, description and info regarding the dataframe
    '''
    attribute_types = columns_type(df)
    print(
        f"\nThere are total {attribute_types[0]} categorical and {attribute_types[1]} numerical columns\n")

    print("Description of Data:\n")
    display(df.describe())

    print("Information regarding data: \n")
    display(df.info())

    if df.isnull().sum().sum() > 0:
        null_columns_percentage(df)
    else:
        print(
            "\nCongrats!!, The Dataframe has NO NULL VALUES\n")


statistics(df)

# Split the dataset into train and test set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=41)

print("Shape of X train = ", X_train.shape)
print("Shape of y train = ", y_train.shape)
print("Shape of X test = ", X_test.shape)
print("Shape of y test = ", y_test.shape)

# fit all classification models

model_dict = {1: "Support Vector Machine", 2: "Decision Tree",
              3: "Random Forest", 4: "KNN", 5: "Naive Bayes"}


def model(X_train, y_train, X_test, y_test):

    # Logistic Regression
    #     logistic_classifier = LogisticRegression()
    #     logistic_classifier.fit(X_train,y_train)
    #     logistic_classifier_score = logistic_classifier.score(X_test, y_test)
    #     print("Logistic Regression Accuracy: ", logistic_classifier_score * 100)

    # Support Vector Classification
    sv_classifier = SVC(kernel="rbf")
    sv_classifier.fit(X_train, y_train)
    sv_classifier_score = sv_classifier.score(X_test, y_test)
    print("Support Vector Machine Accuracy: ", sv_classifier_score * 100)

    # Decision Tree
    dt_classifier = DecisionTreeClassifier(criterion="gini")
    dt_classifier.fit(X_train, y_train)
    dt_classifier_score = dt_classifier.score(X_test, y_test)
    print("Decision Tree Accuracy: ", dt_classifier_score * 100)

    # Random Forest
    rf_classifier = RandomForestClassifier(n_estimators=100, criterion="gini")
    rf_classifier.fit(X_train, y_train)
    rf_classifier_score = rf_classifier.score(X_test, y_test)
    print("Random Forest Accuracy: ", rf_classifier_score * 100)

    # KNN
    knn_classifier = KNeighborsClassifier(n_neighbors=5)
    knn_classifier.fit(X_train, y_train)
    knn_classifier_score = knn_classifier.score(X_test, y_test)
    print("KNN Accuracy: ", knn_classifier_score * 100)

    # Naive Bayes
    naive_classifier = GaussianNB()
    naive_classifier.fit(X_train, y_train)
    naive_classifier_score = naive_classifier.score(X_test, y_test)
    print("Naive Bayes Accuracy: ", naive_classifier_score * 100)

    return sv_classifier, dt_classifier, rf_classifier, knn_classifier, naive_classifier


models = model(X_train, y_train, X_test, y_test)


# evaluate classification

for i in range(len(model)):
    print("Model ", i)
    print(classification_report(y_test, model[i].predict(X_test)))
    print(accuracy_score(y_test, model[i].predict(X_test)))
    print()
