from .intent_classification import *
from .entity_recognition import *


class Codify:
    def __init__(self):
        self.ic = IntentClassfication()

    def classify_intent(self, text):
        return self.ic.predict(text, debug=False)

    def recognize_entities(self, ):
        pass

    def get_codify_response(self, text, intent, entities):
        pass

    def codify_engine(self, text):
        """Given a text input, it will not only classify the intent of the input sentences but will also recognize all entities present in the sentence"""
        classified_intent = self.classify_intent(text)


if __name__ == "__main__":
    input_text = "first 5 rows of our data"

    codify = Codify()
    response = codify.codify_engine(input_text)
    print(response)
