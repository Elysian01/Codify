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
        "entities": [
            [
                "mean",
                "STATISTICS"
            ]
        ],
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
        "entities": [
            [
                "mean",
                "STATISTICS"
            ]
        ],
        "priority": 2,
        "code": """
                df.fillna(df.mean())
                print('Missing: %d' % isnan(df).sum())
        """
    },
    {
        "id": 3,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
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
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 2,
        "code": """
                df.fillna(df.median())
                print('Missing: %d' % isnan(df).sum())
        """
    },
    {
        "id": 5,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 6,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 7,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 8,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 9,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 10,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 11,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 12,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 13,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 14,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 15,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 16,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 17,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 18,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 19,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 20,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 21,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 22,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 23,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 24,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 25,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 26,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 27,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 28,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 29,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 30,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 31,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 32,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 33,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 34,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 35,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 36,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 37,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 38,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 39,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 40,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 41,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 42,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 43,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 44,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 45,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 46,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 47,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 48,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 49,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 50,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 51,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 52,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 53,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 54,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 55,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 56,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 57,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 58,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 59,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 60,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 61,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 62,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 63,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 64,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 65,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 66,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 67,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 68,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 69,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 70,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 71,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 72,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 73,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 74,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 75,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 76,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 77,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 78,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 79,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 80,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 81,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 82,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 83,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 84,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 85,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 86,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 87,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 88,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 89,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 90,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 91,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 92,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 93,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 94,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 95,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 96,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 97,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 98,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 99,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
    {
        "id": 100,
        "intent": "null_imputation",
        "entities": [
            [
                "median",
                "STATISTICS"
            ]
        ],
        "priority": 1,
        "code": """
        
        """
    },
]


if __name__ == '__main__':
    export_to_json(data)
