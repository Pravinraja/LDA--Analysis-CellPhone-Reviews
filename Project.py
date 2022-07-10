#!/usr/bin/env python
# coding: utf-8

# In[27]:


#Packages Used and Imported
import re #clean our text using regex
import csv #this will read the csv file
from collections import defaultdict # accumlating values
from nltk.corpus import stopwords #remove stopwords
from gensim import corpora #create corpus and dictionary for LDA model
from gensim.models import LdaModel #use the LDA model
import pyLDAvis.gensim #visualise LDA model 
import pandas as pd # bring in panda data frames to easier readable format
import nltk #nlp library to perform NLP
nltk.download('stopwords') #stopwords run trial


# In[28]:


#This is performing file operations to get the file contents
fileContents = defaultdict(list)
with open('FinalData.csv', 'r', encoding="utf-8") as f: #configure utf-8 to bypass any text issues
    reader = csv.DictReader(f)
    for row in reader: # read a row in this format {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value. K and V is each one value
            fileContents[k].append(v) # this will append the value into the appropriate list


# In[29]:


#print file contents for review (#in our case it is under the extract column in the csv file)
from nltk.tokenize import word_tokenize
reviews = fileContents[ 'extract']
print(reviews) 


# In[30]:


#cleaning the data. This will remove uncessary spaces between words and punctuation as well
reviews = [re.sub(r'[^\w\s]','',str(item)) for item in reviews]
print(reviews)


# In[31]:


#Stop Words Implementation
# It is important to use stopwords because stop words occur in abundance mean they provide little to no unique information
#stopwords = set(stopwords.words('english'))
#from nltk.corpus import stopwords
#stopwords=stopwords.words('english')
#stopwords.extend(["diehard", "sim", "phone", "week", "release","used",]) 
#print(stopwords)
#clean = [word for word in reviews if word not in stopwords]
#clean_text = ' '.join(clean)
#words = re.findall('\w+', clean_text)
#print(clean)


# In[33]:


#this is splitting the words using comma so it will be easier to read each word
#this also make sure this is also implemented alongside the stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stopwords=stopwords.words('english')
#use extend for specific words that add no value or use to the model. Pretty important
stopwords.extend(["diehard", "sim", "phone", "phones", "mobile","smartphone", "iphone", "Apple", "apple", "blakberry", "Blackberry", "Nokia","nokia", "Samsung", "samsung", "Use", "Nubia", "Talk", "im","1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "bought", "Bought", "case", "android", "case", "One"]) 
texts = [[word for word in document.lower().split() if word not in stopwords] for document in reviews]
print(texts)


# In[34]:


#Taking out the less frequent words
#take a look at the words with most occurences
frequency = defaultdict(int)
for text in texts:
    for token in text:
         frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1] for text in texts]
print(frequency)


# In[35]:


#This will assemble our text into a corpus dictionary
dictionary = corpora.Dictionary(texts)
print(dictionary)


# In[36]:


#Convert document (a list of words) into the bag-of-words format. 
corpus = [dictionary.doc2bow(text) for text in texts]
print(corpus)


# In[37]:


#We will guess the number of topics that could be in our LDA model
#Note: For the LDA model to run we need a corpus, a set number of topics, a dicationary, and a set number of iterations
#that will be passed in your paramter also known as paramter passing. Finally, you can visualize the model. 
##This might take some time. So please be patient.
NUM_TOPICS = 20
ldamodel = LdaModel(corpus, num_topics = NUM_TOPICS, id2word=dictionary, passes=15)
print(ldamodel)


# In[38]:


#This will show LDA model topics
#Yes, this does look hard to read and messy that's why we setup pandas dataframe below to read it easier
topics = ldamodel.show_topics()
for topic in topics:
    print(topic)


# In[39]:


##This is our setup of pandas dataframe below to read it easier
#This is shown like an excel format for each topic
word_dict = {};
for i in range(NUM_TOPICS):
    words = ldamodel.show_topic(i, topn = 20)
    word_dict['Topic # ' + '{:02d}'.format(i+1)] = [i[0] for i in words]
pd.DataFrame(word_dict)


# In[40]:


#we use a pyplot to display the LDA model in a multi-dimeonsinal model
#we can also traverse through mutiple topics in a multi-heirchal model
#for our insights, the most relevant terms with the most frequency can give the most accurate reviews and vice versa
#as people could commonly come on an agreement on a certain issue of the smartphone or a likeable feature
lda_display = pyLDAvis.gensim.prepare(ldamodel, corpus, dictionary, sort_topics=False)
pyLDAvis.display(lda_display)


# In[ ]:




