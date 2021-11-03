import os
import pickle
import numpy as np
from sklearn.svm import SVC
from gensim.utils import tokenize
from gensim.models import KeyedVectors
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
# from gensim.parsing.preprocessing import preprocess_string,stem_text,remove_stopwords


class WordEmebdingClassifier:
    def __init__(self):
        self.model = KeyedVectors.load_word2vec_format(
            os.path.join(os.path.dirname(__file__),
                         "embeddings",
                         'glove.6B.200d.w2vformat.txt')
        )
        # self.model = KeyedVectors.load_word2vec_format(
        #     os.path.join("embeddings_files/glove", 'glove.840B.300d.w2vformat.txt'))

    def doc2vec(self, sentences):
        sentence_vec = []
        for index, t in enumerate(sentences):
            temp = []
            for key in tokenize(t, lowercase=True):
                if key in self.model.wv:
                    temp.append(self.model[key])
            sentence_vec.append(np.vstack(temp))
        X = np.stack([np.sum(vec, axis=0) / vec.shape[0]
                     for vec in sentence_vec])
        return X

    def train(self, texts, labels):
        X = self.doc2vec(texts)
        tuned_parameters = {'kernel': ['linear'], 'C': [1, 10]}
        # We will use grid GridSearchCV for hyper parameter tuning, we pass a list of hyper parameters and model will do all the PnC and give the best model as output
        self.clf = GridSearchCV(SVC(C=1, probability=True, class_weight="balanced"),
                                param_grid=tuned_parameters,
                                n_jobs=1,
                                cv=KFold(n_splits=5, shuffle=True),
                                scoring='accuracy')
        self.le = LabelEncoder()
        Y = self.le.fit_transform(labels)
        self.clf.fit(X, Y)

    def eval(self, texts, labels):
        X = self.doc2vec(texts)
        Y = self.le.transform(labels)

        response = {
            "accuracy_score": accuracy_score(self.clf.predict(X), Y),
            "precision_score": precision_score(self.clf.predict(X), Y, average="micro"),
            "recall_score": recall_score(self.clf.predict(X), Y, average="micro"),
            "f1_score": f1_score(self.clf.predict(X), Y, average="micro"),
        }
        return response

    def get_model(self):
        return self.clf

    def set_model(self, model):
        self.clf = model

    def predict(self, text):
        X = self.doc2vec(text)
        return self.clf.predict(X)

    def save(self, name, acc):
        model_filename = f"models/{name}/{name}_WordEmd_{round(acc, 2)}acc.sav"
        labels_filename = f"models/{name}/{name}_WordEmd_{round(acc, 2)}acc_labels.txt"
        # save the model to disk
        pickle.dump(self.clf, open(model_filename, 'wb'))
        f = open(labels_filename, 'w')
        for item in self.le.classes_:
            f.write(item + "\n")
        f.close()
