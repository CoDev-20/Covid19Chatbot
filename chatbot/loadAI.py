#local
import os
import sys
import speech_recognition as sr
import json
import random
from gtts import gTTS
import requests
import re
import nltk
import numpy as np

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


class LoadAI():
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


#loading of model
    def loadAI(self):
        pass

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
