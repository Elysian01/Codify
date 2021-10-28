from intent_classification import *
from entity_recognition import *


class Codify:
    def __init__(self):
        self.ic = IntentClassfication()
        self.er = EntityRecognition()

    def classify_intent(self, text):
        return self.ic.predict(text, debug=False)

    def recognize_entities(self, text):
        return self.er.get_entities(text)

    def codify_engine(self, text):
        """Given a text input, it will not only classify the intent of the input sentences but will also recognize all entities present in the sentence"""
        classified_intent = self.classify_intent(text)
        entities = self.recognize_entities(text)
        response = {
            "text": text,
            "intent": classified_intent["intent"],
            "entities": entities["entities"],
        }
        return response


if __name__ == "__main__":
    text = "insert median values replacing with the null values"

    codify = Codify()
    response = codify.codify_engine(text)
    print(response)
