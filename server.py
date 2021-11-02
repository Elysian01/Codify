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
            "entities": [
                [
                    "median",
                    "STATISTICS"
                ]
            ],
            "intent": "null_imputation",
            "text": "insert median values replacing with the null values"
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
    app.run(host="127.0.0.1", port=PORT, debug=True)
