import json
import spacy


class EntityRecognition:
    def __init__(self, model_path=None):
        if model_path is None:
            self.model_path = "models/entity_recognition/"
        else:
            self.model_path = model_path

        self.model = spacy.load(self.model_path)

    def get_entities(self, text):
        doc = self.model(text)
        response = {
            "text": text,
            "entities": [(ent.text, ent.label_) for ent in doc.ents],
        }
        # print("For text: {}\nEntities: {}".format(text, response))
        return response


if __name__ == '__main__':

    er = EntityRecognition()
    text = "insert median values replacing with the null values"
    response = er.get_entities(text)
