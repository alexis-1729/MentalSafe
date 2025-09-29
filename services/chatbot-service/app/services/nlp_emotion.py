import tensorflow as tf
import pickle
import pandas as pd
import numpy as np
from preprocess import proccess
from keras.models import load_model 

def analisis(line: str):
    encoder = pickle.load(open('nlp/encoder.pkl', 'rb'))
    cv = pickle.load(open('nlp/CountVectorizer.pkl'))

    model = load_model('my_model.h5')
    intput = proccess(line)

    array = cv.transform([input]).toarray()

    pred = model.predict(array)
    a = np.argmax(pred, axis = 1)
    prediction = encoder.inverse_transform(a)[0]

    return prediction