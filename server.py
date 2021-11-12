from flask import Flask
from flask import request
from codify import Codify

app = Flask(__name__)

PORT = 9000
codify = Codify()
print("Intent Classification and Entity Recognition Model Successfully Loaded....")


@app.route('/codify', methods=['POST'])
def codify_request():
    """Given text input, this functions identifies the intent and entities present in it and returns in json format

    Example:
        Accepts Request like:
            {
                "text": "insert median values replacing with the null values"
            }

        Returns:

        {
            'text': 'insert median values replacing with the null values',
            'intent': 'null_imputation',
            'entities': [('STATISTICS', 'median')],
            'code': [
                ['from sklearn.impute import SimpleImputer', '# define the imputer', "imputer = SimpleImputer(missing_values=nan, strategy='median')", '# transform the dataset', 'transformed_values = imputer.fit_transform(values)', '# count the number of NaN values in each column', "print('Missing: %d' % isnan(transformed_values).sum())"],
                ['df.fillna(df.median())', "print('Missing: %d' % isnan(df).sum())"]
            ]
        }
    """
    data = request.get_json()
    text = data.get('text')
    response = codify.codify_engine(text)
    return response


@app.route('/', methods=['GET'])
def home():
    return "Welcome to Codify Server!"


if __name__ == '__main__':
    examples = [
        "insert median values replacing with the null values",
        "Split dataset into training and test set",
        "Duplicate rows in this dataset",
        "Construct a bar plot",
        "Perform Random Forest Regression",
        "Code for all Regression models"
    ]
    print(f"Server running on http://127.0.0.1:{PORT}/")
    print(
        f"for getting code from text, post request on http://127.0.0.1:{PORT}/codify/")
    app.run(host="127.0.0.1", port=PORT, debug=True)
