import csv
import re
import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.cross_validation import train_test_split
from sklearn import naive_bayes
from sklearn.metrics import roc_auc_score
from sklearn.linear_model.tests.test_passive_aggressive import random_state
from sklearn.svm.classes import SVC
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.linear_model.stochastic_gradient import SGDClassifier
from sklearn import metrics
from gettext import _token_pattern
import pickle
import math
import numpy as np
from nltk import word_tokenize          
from nltk.stem import WordNetLemmatizer 
from nltk.tag import pos_tag
from sklearn.externals import joblib




def sent(textdata):
    reviewdata=textdata
    df=pd.read_csv("g_train.txt",sep='\t',names=['liked','txt'])
    #df.head()
    stopset=set(stopwords.words('english'))
    #vectorizer=TfidfVectorizer(max_df=0.8,token_pattern='food',use_idf=True,lowercase=True,strip_accents='ascii',stop_words=stopset,ngram_range=(1,2))
    vectorizer=CountVectorizer(ngram_range=(1,3))
    y=df.liked
    #x=vectorizer.fit_transform(df.txt.values.astype('U'))
    x=vectorizer.fit_transform(df.txt.values.astype('U'))
    print(y.shape)
    print(x.shape)
    #x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42)
    clf1=naive_bayes.MultinomialNB()
    clf1.fit(x,y)
    
    str1=reviewdata
    str1=str1.lower()
    dict={}
    word_tokens = word_tokenize(str1)
    if(len(word_tokens)<6):
        dict['text']="review too short"
    else:
        dict['text']="Review length accepted"
    filtered_sentence = [w for w in word_tokens if not w in stopset]
    str2=' '.join(filtered_sentence)
    review_array=[]
    review_array.append(str2)
    rv_arr=[x.lower()for x in review_array]
    review_vector=vectorizer.transform(rv_arr)
    pred_class=clf1.predict(review_vector)
    num=int(pred_class[0])
    print(type(num))
    
    strnew='\n%d\t%s'%(num,str1.strip())
    fw=open("g_train.txt","a")
    fw.write(strnew)
    fw.close()
    #print(pred_class)
    dict['sent_no']=num
    return dict
    
