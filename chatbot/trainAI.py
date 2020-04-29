import os
import sys
import json
import pickle
import random
import tensorflow.keras as krs
from tensorflow.python.framework import ops
import tensorflow as tf
import numpy as np
import nltk
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
from gtts import gTTS
import requests
import re


class TrainAI():
    items = 0

    def __init__(self):
        website = r"https://coronavirus-ph-api.herokuapp.com/total/"
        res = requests.get(website)
        jsonContent = json.loads(res.content.decode())
        self.cases = jsonContent['data']['cases']
        self.deaths = jsonContent['data']['deaths']
        self.recov = jsonContent['data']['recoveries']
        self.casesToday = jsonContent['data']['cases_today']
        self.deathsToday = jsonContent['data']['deaths_today']
        self.recovToday = jsonContent['data']['recoveries_today']
        self.admitted = jsonContent['data']['admitted']
        self.fatRate = jsonContent['data']['fatality_rate']
        self.recovRate = jsonContent['data']['recovery_rate']
        self.date = jsonContent['data']['last_update']


#training/loading of model
    def train(self):
        self.stemmer = LancasterStemmer()

        fileDir = os.path.dirname(os.path.abspath(__file__))
        print(fileDir)
        with open(fileDir+r"/session.json", encoding='utf-8') as file:
            self.data = json.load(file)

        try:
            with open(fileDir+r"/data.pickle", "rb") as f:
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
                with open(fileDir+r"/data.pickle", "wb") as f:
                    pickle.dump((self.words, self.labels, self.training, self.output), f)
            except Exception as ex:
                print(ex)

        ops.reset_default_graph() 

        # keras

        try:
            self.model = krs.models.load_model(fileDir+r"/model/testmodel.h5")
            #self.model = pickle.load(open('/model/testmodel.pkl', 'rb'))
        except Exception as ex:
            self.model = krs.Sequential([
                krs.layers.Dense(8, input_shape=(len(self.training[0]),)),
                krs.layers.Dense(8),
                krs.layers.Dense(len(self.output[0]), activation="softmax"),
            ])


            self.model.compile(optimizer="adam",
                        loss="categorical_crossentropy", metrics=["acc"])

            self.model.fit(self.training, self.output, epochs=1000, batch_size=8)
            self.model.save(fileDir+r"/model/testmodel.h5")
            #tf.saved_model.simple_save()
            #pickle.dump(self.model, open('model/testmodel.pkl', 'wb'))

        print(self.model)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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
            #print(results[0])

            if results[0][results_index] > 0.7:
                for tg in self.data["intents"]:
                    if tg['tag'] == tag:
                        responses = tg['responses']

                return random.choice(responses)
            else:
                if re.search(r'^(today)', inp.lower()):  # for cases today
                    return("There are {} new cases, {} new deaths, and {} new recoveries in the Philippines as of {}".format(self.casesToday, self.deathsToday, self.recovToday, self.date))

                elif re.search(r'^(confirm)|^(case)', inp.lower()):  # for confirmed cases
                    return("There are {} confirmed cases in the Philippines as of {}".format(self.cases, self.date))

                elif re.search(r'^(recover)', inp.lower()):  # for recovered
                    return("There are currently {} recovered in the Philippines as of {}".format(self.recov, self.date))

                elif re.search(r'^(death)|^(dead)|^(die)', inp.lower()):  # for deaths
                    return("There are currently {} death cases in the Philippines as of {}".format(self.deaths, self.date))

                elif re.search(r'^(rate)|^(rates)|^(current)', inp.lower()):  # for rates
                    return("The recovery rate is {} and the fatality rate is {} as of {}".format(self.recovRate, self.fatRate, self.date))
                
                elif re.search(r'^(admit)', inp.lower()):  # for deaths
                    return("There are currently {} admissions in the Philippines as of {}".format(self.admitted, self.date))

                else:
                    return("Sorry. I don't have an answer for that.")

    def voice(self, text):
        tts = gTTS(text)
        direc  = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'chatbot_website/static/chatbot_website/audio'))
        filepath = direc + '/audio' + str(self.items) + '.mp3'
        filename = 'audio' + str(self.items) + '.mp3'
        #print(direc)
        tts.save(filepath)
        self.items = self.items + 1
        return filename


##testing purposes
#ai = TrainAI()
#ai.voice("Hello there")
#ai.voice("Hi there")
