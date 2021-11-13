import os
import json

CODIFY_CODEBASE_PATH = os.path.join(
    os.path.dirname(__file__), "codify_codebase.json")

with open(CODIFY_CODEBASE_PATH, "r", encoding="utf-8") as f:
    codebase = json.load(f)


def export_to_json(dataset):
    for data in dataset:
        code = data["code"].strip().split("\n")
        code = [codeline.strip() for codeline in code]
        data["code"] = code
    with open(CODIFY_CODEBASE_PATH, "w", encoding="utf-8") as f:
        f.write(json.dumps(dataset, indent=5))


data = [
    {
        "id": 1,
        "intent": "null_imputation",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """ 
                    from sklearn.impute import SimpleImputer
                    # define the imputer
                    imputer = SimpleImputer(missing_values=nan, strategy='mean')
                    # transform the dataset
                    transformed_values = imputer.fit_transform(values)
                    # count the number of NaN values in each column
                    print('Missing: %d' % isnan(transformed_values).sum())
                """
    }, {
        "id": 2,
        "intent": "null_imputation",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 2,
        "code": """
                df.fillna(df.mean(), inplace = True)
                print('Missing: %d' % isnan(df).sum().sum())
        """
    },
    {
        "id": 3,
        "intent": "null_imputation",
        "entity_name": "STATISTICS",
        "entity_value": "median",
        "priority": 1,
        "code": """
                from sklearn.impute import SimpleImputer
                # define the imputer
                imputer = SimpleImputer(missing_values=nan, strategy='median')
                # transform the dataset
                transformed_values = imputer.fit_transform(values)
                # count the number of NaN values in each column
                print('Missing: %d' % isnan(transformed_values).sum())
        """
    },
    {
        "id": 4,
        "intent": "null_imputation",
        "entity_name": "STATISTICS",
        "entity_value": "median",
        "priority": 2,
        "code": """
                df.fillna(df.median(), inplace = True)
                print('Missing: %d' % isnan(df).sum().sum())
        """
    },
    {
        "id": 5,
        "intent": "csv_pandas",
        "entity_name": "",
        "entity_value": "",
        "priority": 1,
        "code": """
        import pandas as pd
        df = pd.read_csv("./data.csv", encoding = "utf-8")
        """
    },
    {
        "id": 6,
        "intent": "train_test_split",
        "entity_name": "",
        "entity_value": "",
        "priority": 1,
        "code": """
        from sklearn.model_selection import train_test_split

        X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 41)

        print("Shape of X train = ",X_train.shape)
        print("Shape of y train = ",y_train.shape)
        print("Shape of X test = ",X_test.shape)
        print("Shape of y test = ",y_test.shape)
        """
    },
    {
        "id": 7,
        "intent": "classification",
        "entity_name": "AMOUNT",
        "entity_value": "all",
        "priority": 1,
        "code": """
        from sklearn.naive_bayes import GaussianNB
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.linear_model import LogisticRegression
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.svm import SVC


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


        """
    },
    {
        "id": 8,
        "intent": "describe_data",
        "entity_name": "STATISTICS",
        "entity_value": "statistics",
        "priority": 1,
        "code": """
            from IPython.display import display
            
            def columns_type(df) -> tuple:
                '''
                return number of categorical and numerical columns
                '''
                numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
                num_cols = df.select_dtypes(include=numerics).columns.tolist()
                cat_columns = len(df.select_dtypes(include="O").columns.tolist())
                num_columns = len(num_cols)
                return (cat_columns, num_columns)
        
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
        """
    },
    {
        "id": 9,
        "intent": "classify_eval",
        "entity_name": "evaluation",
        "entity_value": "classification",
        "priority": 1,
        "code": """
        from sklearn.metrics import accuracy_score
        from sklearn.metrics import classification_report

        i = 0
        for key, value in model_dict.items():
            print(f"{value} Model ")
            print(f"\nClassification Report: \n{classification_report(y_test, models[i].predict(X_test))}")
            print(f"\n{value} model accuracy: {round(accuracy_score(y_test, models[i].predict(X_test)), 2)}")
            print(f'\n{"-"*55}\n')
            i+=1
        """
    },
    {
        "id": 10,
        "intent": "null_percent",
        "entity_name": "",
        "entity_value": "",
        "priority": 1,
        "code": """
        from IPython.display import display
        
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
        """
    },
    {
        "id": 11,
        "intent": "view_data",
        "entity_name": "VIEW",
        "entity_value": "head",
        "priority": 1,
        "code": """
        df.head()
        """
    },
    {
        "id": 12,
        "intent": "view_data",
        "entity_name": "VIEW",
        "entity_value": "tail",
        "priority": 1,
        "code": """
        df.tail()
        """
    },
    {
        "id": 13,
        "intent": "view_data",
        "entity_name": "VIEW",
        "entity_value": "sample",
        "priority": 1,
        "code": """
        df.sample()
        """
    },
    {
        "id": 14,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 15,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 16,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 17,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 18,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 19,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 20,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 21,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 22,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 23,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 24,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 25,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 26,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 27,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 28,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 29,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 30,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 31,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 32,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 33,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 34,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 35,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 36,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 37,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 38,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 39,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 40,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 41,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 42,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 43,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 44,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 45,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 46,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 47,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 48,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 49,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 50,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 51,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 52,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 53,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 54,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 55,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 56,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 57,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 58,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 59,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 60,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 61,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 62,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 63,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 64,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 65,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 66,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 67,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 68,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 69,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 70,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 71,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 72,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 73,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 74,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 75,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 76,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 77,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 78,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 79,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 80,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 81,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 82,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 83,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 84,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 85,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 86,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 87,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 88,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 89,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 90,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 91,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 92,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 93,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 94,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 95,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 96,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 97,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 98,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 99,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 100,
        "intent": "put_intent",
        "entity_name": "STATISTICS",
        "entity_value": "mean",
        "priority": 1,
        "code": """
        
        """
    },
]


if __name__ == '__main__':
    export_to_json(data)
    print(f"Codify Dataset Created and File Stored with Name 'codidy_codebase.json'")
