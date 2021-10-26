from .intent_classification import *
from .entity_recognition import *


def classify_intent():
    pass


def recognize_entities():
    pass


def print_codify(text, intent, entities):
    pass


def get_codify_response(text, intent, entities):
    pass


def codify_engine(input_text):
    """Given a text input, it will not only classify the intent of the input sentences but will also recognize all entities present in the sentence"""
    pass


if __name__ == "__main__":
    input_text = ""

    output = codify_engine(input_text)
    print_codify(output)
