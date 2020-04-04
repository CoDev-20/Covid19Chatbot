import sys
import speech_recognition as sr
import json
import pickle
import random
import tensorflow.keras as krs
from tensorflow.python.framework import ops
import tensorflow as tf
import numpy as np
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()


with open('intents.json') as file:
    data = json.load(file)

r = sr.Recognizer()

try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)

except:
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in data['intents']:
        for pattern in intent['patterns']:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

        if intent['tag'] not in labels:
            labels.append(intent['tag'])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []
        wrds = [stemmer.stem(w.lower()) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = np.array(training)
    output = np.array(output)

    try:
        with open("data.pickle", "wb") as f:
            pickle.dump((words, labels, training, output), f)
    except Exception as ex:
        print(ex)

ops.reset_default_graph()

# keras
ops.reset_default_graph()
model = krs.Sequential([
    krs.layers.Dense(8, input_shape=(len(training[0]),)),
    krs.layers.Dense(8),
    krs.layers.Dense(len(output[0]), activation="softmax"),
])


model.compile(optimizer="adam",
              loss="categorical_crossentropy", metrics=["acc"])


try:
    model = krs.models.load_model('testmodel')
except Exception as ex:
    model.fit(training, output, epochs=1000, batch_size=8)
    model.save(r"testmodel")



# functions
def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return np.array([bag])


def chat():
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break

        results = model.predict([bag_of_words(inp, words)])
        results_index = np.argmax(results)
        tag = labels[results_index]

        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']

        print("Doc VI: ", random.choice(responses))


def voice():
    choice = input("1 - online\n"
                   "2 - offline\n"
                   "Choose your option:\n")
                   
    print("Speak now", end = ' ')

    if (int(choice) != 1) and (int(choice) != 2):
        print("invalid option")
        voice()
    else:
        r = sr.Recognizer()

        with sr.Microphone() as source:

            while True:
                try:
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source, timeout=5)

                    if int(choice) == 1:
                        inp = r.recognize_google(audio)
                    elif int(choice) == 2:
                        inp = r.recognize_sphinx(audio)

                    results = model.predict([bag_of_words(inp, words)])
                    results_index = np.argmax(results)
                    tag = labels[results_index]

                    for tg in data["intents"]:
                        if tg['tag'] == tag:
                            responses = tg['responses']

                    print(inp)
                    if inp.lower() == 'goodbye':
                        break

                    print("Chatbot: ", random.choice(
                        responses), "\nYou:", end = ' ')
                except Exception as ex:
                    print("Chatbot: Sorry I didn't understand you\nYou:", end = ' ')


def main():
    inp = input("Hi! I'm Chatbot\n"
                "Please type:\n"
                "1 for chat\n"
                "2 for voice\n"
                "quit to quit on chat\n"
                "say goodbye to quit on voice\nYou: ")

    if str(inp) == str("1"):
        chat()
    elif str(inp) == str("2"):
        voice()
    elif str(inp).lower() == 'quit':
        pass
    else:
        print('invalid input')
        main()

main()