import pandas as pd

from .intent_classification import *
from .entity_recognition import *


class Codify:
    def __init__(self):

        self.codebase_path = str(os.path.join(
            os.path.dirname(__file__),
            "data",
            "codify_codebase.json")
        )
        self.codebase = pd.read_json(self.codebase_path)
        print("\nCodify Codebase Successfully Loaded\n")
        self.ic = IntentClassfication()
        self.er = EntityRecognition()

    def remove_punctuations(self, text):
        chars = "\\`*_{}[]()^&@<>#+.!$'%"
        for c in chars:
            text = text.replace(c, "")
            text = text.replace('"', "")
            text = text.replace('/', " ")
            text = text.replace(',', " ")
            text = text.replace('-', " ")
        return text.strip()

    def clean_text(self, text):
        shortforms = {
            "reg": "regression",
            "clf": "classification",
            "svm": "support vector classifier",
            "svc": "support vector classifier",
            "dtree": "decision tree classifier",
            "rvc": "random forest classifier",
            "ada": "adaptive",
            "lr": "logistic regression",
            "knn": "k nearest neighbor",
            "gd": "gradient boost",
            "adaboost": "adaptive boosting",
            "xgboost": "extreme gradient boosting",
            "gbm": "gradient boosting machine",
            "lightgbm": "light gradient boosting machine",
            "kfold": "k fold"
        }
        cleaned = []
        text = self.remove_punctuations(text)
        for word in text.split():
            if word in shortforms:
                cleaned.append(shortforms[word].lower())
            else:
                cleaned.append(word.lower())
        return' '.join([str(word) for word in cleaned])

    def classify_intent(self, text):
        return self.ic.predict(text, debug=False)

    def recognize_entities(self, text):
        return self.er.get_entities(text)

    def get_code(self, intent, entity_name=None, entity_value=None):
        results = []
        intent_search_result = self.codebase.loc[self.codebase["intent"] == intent]

        if not entity_name:
            results.append(intent_search_result["code"].values)

        if not intent_search_result.empty and entity_name:
            entity_name_search_result = intent_search_result.loc[
                self.codebase["entity_name"] == entity_name]
            if not entity_name_search_result.empty and entity_value:
                entity_value_search_result = entity_name_search_result.loc[
                    self.codebase["entity_value"] == entity_value]
                if not entity_value_search_result.empty:
                    results.append(entity_value_search_result["code"].values)
                else:
                    results.append(entity_name_search_result["code"].values)
            else:
                results.append(intent_search_result["code"].values)

        response = []
        # print(results)
        for result in results[0]:
            response.append(result)
        return response

    def codify_engine(self, text):
        """Given a text input, it will not only classify the intent of the input sentences but will also recognize all entities present in the sentence"""
        text = self.clean_text(text)
        classified_intent = self.classify_intent(text)
        entities = self.recognize_entities(text)
        if "entity_name" in entities:
            code = self.get_code(
                classified_intent["intent"], entities["entity_name"], entities["entity_value"])
        else:
            code = self.get_code(
                classified_intent["intent"])
        response = {
            "text": text,
            "intent": classified_intent["intent"],
            "entities": entities["entities"],
            "code": code
        }
        return response


if __name__ == "__main__":
    text = "insert median values replacing with the null values"

    codify = Codify()
    response = codify.codify_engine(text)
    print(response)
