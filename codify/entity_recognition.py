import os
import spacy


class EntityRecognition:
    def __init__(self, model_path=None):
        if model_path is None:
            self.model_path = os.path.join(
                os.path.dirname(__file__),
                "models",
                "entity_recognition/"
            )
        else:
            self.model_path = model_path

        self.model = spacy.load(self.model_path)

    def get_entities(self, text):
        doc = self.model(text)
        if doc.ents:
            for ent in doc.ents:
                entity_name = ent.label_
                entity_value = ent.text
                break
            response = {
                "text": text,
                "entity_name": entity_name,
                "entity_value": entity_value,
                "entities": [[ent.label_, ent.text] for ent in doc.ents],
            }
        else:
            response = {
                "text": text,
                "entities": "",
            }
        # print("For text: {}\nEntities: {}".format(text, response))
        return response


if __name__ == '__main__':

    er = EntityRecognition()
    text = "insert median values replacing with the null values"
    response = er.get_entities(text)
    print(response)
