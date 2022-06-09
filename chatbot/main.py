from urllib import response
import nltk 
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy as np
import tflearn
import tensorflow as tf
from tensorflow.python.framework import ops
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
classifier = Sequential()

import random
import json
import pickle

with open("intents.json") as file:
    data = json.load(file)

train = input("Train the model type in (train): ")
#Data preprocessing start
if train.lower() == "train":
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in data['intents']:
        for pattern in intent['patterns']:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent['tag'])

        if intent["tag"] not in labels:
            labels.append(intent['tag'])

    #Getting rid of duplicate words
    words = [stemmer.stem(w.lower()) for w in words if w not in "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    '''
    Turning words into a bag of words.
    When feeding our model we want our words
    to be numeric instead of string value.
    So I'm going to do OHE the words turning
    them to numeric values.

    How we going to store it
    word list: ['a', 'am', 'be']
    OHE: [1, 0, 1]

    Put a 1 if that word exist else put a 0
    '''

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        #Bag of words
        bag = []

        wrds = [stemmer.stem(w) for w in doc]

        #Going through all the words
        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        #Look through label list look for tag and set that output to 1
        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    #turn them into arrays for easier model training
    training = np.array(training)
    output = np.array(output)

    with open('data.pickel', 'wb') as f:
        pickle.dump((words, labels, training, output), f)

else:
    with open('data.pickel', 'rb') as f:
        words, labels, training, output = pickle.load(f)
#Data preprocessing end

#Model creation start
ops.reset_default_graph()
#Input layer trying to get the length from none on
net = tflearn.input_data(shape= [None, len(training[0])])
net = tflearn.fully_connected(net, 16, activation="relu") #hidden layer
net = tflearn.fully_connected(net, 16, activation="relu") #hidden layer
#Output layer solfmax 
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)
#end model creation


#Start training
'''
training = input values
output = output values
n_epoch = how many times do I want to train same dataset
batch_sizes = how many samples of data will pass through at a time 
show_metric = Makes the output look nicer
'''

if train.lower() == "train":
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("model.tflearn")

else:
    model.load("model.tflearn")



def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words if word not in "?"]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return np.array(bag)


#Generate user input
def chat():
    #user input
    print("Start talking with bot!(type 'quit' to stop)")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break
        
        #All this is going to give us a matrix of numbers where the numbers are probabilities of each class
        results = model.predict([bag_of_words(inp, words)])
        #Argmax will grab the index of highest probability in the matrix
        results_index = np.argmax(results)
        tag = labels[results_index]
        
        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']

        print(random.choice(responses))


chat()