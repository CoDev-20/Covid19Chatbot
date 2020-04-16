#local

import os
import sys
import speech_recognition as sr
import json
import pickle
import random
import tensorflow.keras as krs
#import keras as krs
from tensorflow.python.framework import ops
import tensorflow as tf
import numpy as np
import nltk
from nltk.stem.lancaster import LancasterStemmer

#heroku
# import os
# import sys
# import speech_recognition as sr
# import json
# import pickle
# import random
# import keras as krs
# import numpy as np
# import nltk
# from nltk.stem.lancaster import LancasterStemmer


class TrainAI():
    #training/loading of model
    def train(self):
        self.stemmer = LancasterStemmer()

        fileDir = os.path.dirname(os.path.abspath(__file__))
        print(fileDir)
        with open(fileDir+r"\intents.json") as file:
            self.data = json.load(file)

        try:
            with open(fileDir+r"\data.pickle", "rb") as f:
                self.words, self.labels, self.training, self.output = pickle.load(f)

        except:
            self.words = []
            self.labels = []
            docs_x = []
            docs_y = []

            for intent in self.data['intents']:
                for pattern in intent['patterns']:
                    wrds = nltk.word_tokenize(pattern)
                    self.words.extend(wrds)
                    docs_x.append(wrds)
                    docs_y.append(intent["tag"])

                if intent['tag'] not in self.labels:
                    self.labels.append(intent['tag'])

            self.words = [self.stemmer.stem(w.lower()) for w in self.words if w != "?"]
            self.words = sorted(list(set(self.words)))

            self.labels = sorted(self.labels)

            self.training = []
            self.output = []

            out_empty = [0 for _ in range(len(self.labels))]

            for x, doc in enumerate(docs_x):
                bag = []
                wrds = [self.stemmer.stem(w.lower()) for w in doc]

                for w in self.words:
                    if w in wrds:
                        bag.append(1)
                    else:
                        bag.append(0)

                output_row = out_empty[:]
                output_row[self.labels.index(docs_y[x])] = 1

                self.training.append(bag)
                self.output.append(output_row)

            self.training = np.array(self.training)
            self.output = np.array(self.output)

            try:
                with open(fileDir+r"\data.pickle", "wb") as f:
                    pickle.dump((self.words, self.labels, self.training, self.output), f)
            except Exception as ex:
                print(ex)

        ops.reset_default_graph() #uncomment for local, comment for heroku

        # keras



        try:
            self.model = krs.models.load_model(fileDir+r"\testmodel.h5")
        except Exception as ex:
            self.model = krs.Sequential([
                krs.layers.Dense(8, input_shape=(len(self.training[0]),)),
                krs.layers.Dense(8),
                krs.layers.Dense(len(self.output[0]), activation="softmax"),
            ])


            self.model.compile(optimizer="adam",
                        loss="categorical_crossentropy", metrics=["acc"])

            self.model.fit(self.training, self.output, epochs=1000, batch_size=8)
            self.model.save(fileDir+r"\testmodel.h5")


    # functions
    def bag_of_words(self, s, words):
        bag = [0 for _ in range(len(words))]

        s_words = nltk.word_tokenize(s)
        s_words = [self.stemmer.stem(word.lower()) for word in s_words]

        for se in s_words:
            for i, w in enumerate(words):
                if w == se:
                    bag[i] = 1

        return np.array([bag])


    def chat(self, text):
        while True:
            inp = text

            results = self.model.predict([self.bag_of_words(inp, self.words)])
            results_index = np.argmax(results)
            tag = self.labels[results_index]

            for tg in self.data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']

            return random.choice(responses)

#----------------------------------------------------------------
    #soon
    # def voice(self):
    #     choice = input("1 - online\n"
    #                 "2 - offline\n"
    #                 "Choose your option:\n")
                    
    #     print("Speak now", end = ' ')

    #     if (int(choice) != 1) and (int(choice) != 2):
    #         print("invalid option")
    #         voice()
    #     else:
    #         r = sr.Recognizer()

    #         with sr.Microphone() as source:

    #             while True:
    #                 try:
    #                     r.adjust_for_ambient_noise(source)
    #                     audio = r.listen(source, timeout=5)

    #                     if int(choice) == 1:
    #                         inp = r.recognize_google(audio)
    #                     elif int(choice) == 2:
    #                         inp = r.recognize_sphinx(audio)

    #                     results = self.model.predict([bag_of_words(inp, words)])
    #                     results_index = np.argmax(results)
    #                     tag = labels[results_index]

    #                     for tg in data["intents"]:
    #                         if tg['tag'] == tag:
    #                             responses = tg['responses']

    #                     print(inp)
    #                     if inp.lower() == 'goodbye':
    #                         break

    #                     print("Chatbot: ", random.choice(
    #                         responses), "\nYou:", end = ' ')
    #                 except Exception as ex:
    #                     print("Chatbot: Sorry I didn't understand you\nYou:", end = ' ')