import os
import pickle
from .intent_word_emb.word_embeding_classifier import WordEmebdingClassifier


class IntentClassfication:
    def __init__(self, model_path=None, label_path=None):

        if model_path is None:
            self.model_path = os.path.join(os.path.dirname(__file__),
                                           "models",
                                           "intent_classification_models",
                                           "Codify_WordEmd_0.89acc.sav")
        else:
            self.model_path = model_path
        if label_path is None:
            self.label_path = os.path.join(os.path.dirname(__file__),
                                           "models",
                                           "intent_classification_models",
                                           "Codify_WordEmd_0.89acc_labels.txt")
        else:
            self.label_path = label_path

        # Load Model
        self.loaded_model = pickle.load(
            open(self.model_path, 'rb'))
        self.model = WordEmebdingClassifier()
        print("Embeddings Model Loaded")
        self.model.set_model(self.loaded_model)

        # Load Labels
        with open(self.label_path, "r") as f:
            self.labels = f.read().split("\n")

    def get_labels(self):
        return self.labels

    def predict(self, text: str, debug=False) -> str:
        text = [text]  # Converting str into list for prediction
        pred_index = self.model.predict(text)[0]
        if debug:
            print(
                f"Text: \t\t\t{text[0]}\nPredicted Intent: \t{self.labels[pred_index]}")
        response = {
            "text": text[0],
            "intent": self.labels[pred_index]
        }
        return response


if __name__ == "__main__":

    ic = IntentClassfication()
    input_text = "first 5 rows of our data"
    ic.predict(input_text, debug=True)
