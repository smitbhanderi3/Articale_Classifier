import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
import base64
import numpy as np

ps = PorterStemmer()



def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

model = pickle.load(open('model.pkl','rb'))

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()



st.title("Atical Classifier")

input_sms = st.text_area("Enter the message")

def checker(heading,body):
    """Pass a heading, and body of the article to use this function.
        Returns whether article is sports or business."""
    temp=heading+' '+body
    t=temp.split(' ')
    data=[]
    for i in words_dict:
        data.append(t.count(i[0]))
    news_tyep=model.predict(np.array(data).reshape(1,3500))[0]
    if news_tyep==0:
        return 'sports'
    if news_tyep==1:
        return 'business'
