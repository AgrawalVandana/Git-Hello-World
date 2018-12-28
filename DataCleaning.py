# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 18:16:04 2018

@author: Vandana
"""
# Importing files
import pandas as pd
amazon_reviews=pd.read_csv('C:\\Business Analytics\\MIS612-674_Align IS and Stretegies\\DrA\\Project\\amazon.csv')

amazon_reviews['review'] = amazon_reviews['review'].apply(lambda x: " ".join(x.lower() for x in x.split()))
amazon_reviews['review'].head()


amazon_reviews['review'] = amazon_reviews['review'].str.replace('[^\w\s]','')
amazon_reviews['review'].head()

from nltk.corpus import stopwords
stop = stopwords.words('english')
amazon_reviews['review'] = amazon_reviews['review'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
amazon_reviews['review'].head()

freq = pd.Series(' '.join(amazon_reviews['review']).split()).value_counts()[:10]


from textblob import TextBlob

amazon_reviews['review'][:].apply(lambda x: str(TextBlob(x).correct()))

import numpy as np
tf1 = (amazon_reviews['review'][1:10]).apply(lambda x: pd.value_counts(x.split(" "))).sum(axis = 0).reset_index()
tf1.columns = ['words','tf']

for i,word in enumerate(tf1['words']):
  tf1.loc[i, 'idf'] = np.log(amazon_reviews.shape[0]/(len(amazon_reviews[amazon_reviews['review'].str.contains(word)]))) 
  
  

#freq = pd.Series(' '.join(amazon_reviews['review']).split()).value_counts()[-10:]
from textblob import TextBlob
TextBlob(amazon_reviews['review'][1]).words


from emoji import emojize
bot.send_message(emojize("yummy :cake:", use_aliases=True))
