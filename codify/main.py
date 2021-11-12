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

    def classify_intent(self, text):
        return self.ic.predict(text, debug=False)

    def recognize_entities(self, text):
        return self.er.get_entities(text)

    def get_code(self, intent, entity_name, entity_value):
        results = []

        intent_search_result = self.codebase.loc[self.codebase["intent"] == intent]
        if not intent_search_result.empty:
            entity_name_search_result = intent_search_result.loc[
                self.codebase["entity_name"] == entity_name]
            if not entity_name_search_result.empty:
                entity_value_search_result = entity_name_search_result.loc[
                    self.codebase["entity_value"] == entity_value]
                if not entity_name_search_result.empty:
                    results.append(entity_value_search_result["code"].values)
                else:
                    results.append(entity_name_search_result["code"].values)
            else:
                results.append(intent_search_result["code"].values)

        response = []
        for result in results[0]:
            response.append(result)
        return response

    def codify_engine(self, text):
        """Given a text input, it will not only classify the intent of the input sentences but will also recognize all entities present in the sentence"""
        classified_intent = self.classify_intent(text)
        entities = self.recognize_entities(text)
        code = self.get_code(
            classified_intent["intent"], entities["entity_name"], entities["entity_value"])
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
