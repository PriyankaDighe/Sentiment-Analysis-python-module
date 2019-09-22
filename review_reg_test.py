
import restaurant_type

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

count=0
reviewdata=""
def reg_rv(url):
    dict_dt={}
    
    
    with open(r'E:\sampleimages\FinalRv\reviewtxt.csv','r') as f:
            
        reader = csv.reader(f,delimiter=',')
        for row in reader:
            str=','.join(row)
            str=str.split(',',1)
            text=str[1]
            
            match1=re.search(r"[0-9a-zA-Z\s]*REVIEW[S]?,.*[0-9a-zA-Z\s]*FOLLOWER[S]?(.)*just now",text)
            #match1=re.search(r"[0-9a-zA-Z]*REVIEW[S\?],.*[0-9a-zA-Z]*FOLLOWER[S\?](.)*just now",text)
            match3=re.search(r"[\d]*(.)*(MY REVIEW|MY RFVIFW)((.)*\d star[s]?)?",text)
            match4=re.search(r"(.)*NEXT(.)*(EVIEW|FVIFW)",text)
            if match1:
                match2=re.search(r'[0-9]*Like[s]?(.)*[0-9]*Comment[s]?',text)
                #match2=re.search(r"[0-9a-zA-Z]*Like[s\?](.)*[0-9a-zA-Z]*Comment[s\?]",text)
                if match2:
                    #count=count+1
                    b=match1.end()
                    f=match2.start(0)
                    reviewdata=text[b:f-2]
                    
                    
            elif match3:
                #count=count+1
                text=text[match3.end():]
                list1=text.split("OTHER REVIEWS")
                for item in list1:
                    
                    match=re.search(r'[\d]* minutes|[\d]* hours|Just now|January|February|March|April|May|June|July|August|September|October|November|December [\d]+(.)*',item)
                    if match:
                        item=item[:match.start(0)]
                    match=re.search(r'Post a review and tap on Take Screenshot button',item)
                    if match:
                        item=item[:match.start(0)]
                    reviewdata=item
                    
            elif match4:
                #count=count+1
                text=text[match4.end():]
                match=re.search(r'[0-9\.]*Add Photos(.)*@?Tag your friends',text)
                if match:
                    text=text[:match.start(0)]
                reviewdata=text[b:f-2]
    
    dict_dt['review data']=reviewdata
    
    print(reviewdata)
    #dict_dt['review']=reviewdata
    
    df=pd.read_csv("traindata.txt",sep='\t',names=['liked','txt'])
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
    
    
    veg=restaurant_type.res_type(url)
    #print(veg)
    nchk=0
    str1=reviewdata
    str1=str1.lower()
    nveg_food_wordset=['chicken','mutton','murg','fish','prawns','crab','crabs','pomfret','surmai','bombil','bombay duck','bacon','beef','pork','turkey','venison','duck','egg','burji','anda','bhurji']
    word_tokens = word_tokenize(str1)
    if(len(word_tokens)<6):
        #print("review too short")
        dict_dt['additional_data']="review too short"
    for x in word_tokens:
        for y in nveg_food_wordset:
            if x==y and veg==1:
                print("Incorrect review")
                dict_dt['additional_data_2']="Incorrect review"
                nchk=1
    
    filtered_sentence = [w for w in word_tokens if not w in stopset]
    str2=' '.join(filtered_sentence)
    review_array=[]
    review_array.append(str2)
    rv_arr=[x.lower()for x in review_array]
    review_vector=vectorizer.transform(rv_arr)
    pred_class=clf1.predict(review_vector)
    num=int(pred_class[0])
    dict_dt['sent_no']=num
    if nchk==0:
        strnew='\n%d\t%s'%(num,str1.strip())
        fw=open("traindata.txt","a")
        fw.write(strnew)
        fw.close()
    print(dict_dt)
    return dict_dt

