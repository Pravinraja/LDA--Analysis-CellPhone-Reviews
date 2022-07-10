#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Install Scrapy first: use command and run: 
get_ipython().system('conda install -c conda-forge scrapy')


# In[ ]:


#Install Scrapy from home directory (EX. C:/Users/Prav)
get_ipython().system('pip install scrapy')
#After installation scrapy it will create following directories below
#C:\Users\Prav\amazon_reviews_scraping\amazon_reviews_scraping\spiders


# In[ ]:


#we need to update review.py with our python program to get latest data or reviews
# -*- coding: utf-8 -*-
 
# Importing Scrapy Library
import scrapy
 
# Creating a new class to implement Spide
class AmazonReviewsSpider(scrapy.Spider):
 
    # Spider name
    name = 'amazon_reviews'
 
    # Domain names to scrape
    allowed_domains = ['amazon.com']
 
    # Base URL for the Samsung Phone reviews
    myBaseUrl = "https://www.amazon.com/Samsung-Unlocked-Fingerprint-Recognition-Long-Lasting/dp/B082XY23D5/ref=sr_1_3?dchild=1&keywords=samsung%2Bs20&qid=1606682820&sr=8-3&th=1"
    start_urls=[]
 
    # Creating list of urls to be scraped by appending page number a the end of base url
    for i in range(1,121):
        start_urls.append(myBaseUrl+str(i))
 
    # Defining a Scrapy parser
    def parse(self, response):
            data = response.css('#cm_cr-review_list')
 
            # Collecting product star ratings
            star_rating = data.css('.review-rating')
 
            # Collecting user reviews
            comments = data.css('.review-text')
            count = 0
 
            # Combining the results
            for review in star_rating:
                yield{'stars': ''.join(review.xpath('.//text()').extract()),
                      'comment': ''.join(comments[count].xpath(".//text()").extract())
                     }
                count=count+1


# In[ ]:


#Run the program below. This will create review. csv
get_ipython().system(' C:\\Users\\Prav\\amazon_reviews_scraping\\amazon_reviews_scraping\\spiders>scrapy runspider amazon_review.py -o review.csv')


# In[2]:


#importing pandas dataframe will make it easier csv file
import scrapy # import scrapy
import pandas as pd #import pandas dataframe to easier read data
import matplotlib as plt #visualize and plot data
 
df=pd.read_csv("review.csv") #read csv
df.head(25) #bring first 25


# In[6]:


#Scoring for the reviews to plot
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt 
 
dataset = pd.read_csv("review.csv")
summarised_results = dataset["score"].value_counts() #trial and error
plt.bar(summarised_results.keys(), summarised_results.values)
plt.show()


# In[9]:


get_ipython().system('dir #show directories')


# In[23]:





# In[24]:





# In[25]:





# In[7]:





# In[8]:





# In[9]:





# In[12]:





# In[15]:





# In[16]:





# In[17]:





# In[20]:





# In[ ]:




