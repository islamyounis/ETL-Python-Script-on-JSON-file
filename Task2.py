#!/usr/bin/env python
# coding: utf-8

# ### Problem Descripition 
# 
# In 2012, URL shortening service Bitly partnered with the US government website USA.gov to provide a feed of anonymous data gathered from users who shorten links ending with .gov or .mil.
# 
# The text file comes in JSON format and here are some keys and their description. They are only the most important ones for this task.

# |key| description |
# |---|-----------|
# | a|Denotes information about the web browser and operating system|
# | tz | time zone |
# | r | URL the user come from |
# | u | URL where the user headed to |
# | t | Timestamp when the user start using the website in UNIX format |
# | hc | Timestamp when user exit the website in UNIX format |
# | cy | City from which the request intiated |
# | ll | Longitude and Latitude |

# In the cell, I tried to provide some helper code for better understanding and clearer vision
# 
# -**HINT**- Those lines of code may be not helping at all with your task.

# In[5]:


import pandas as pd
import numpy as np
import json
import argparse
from pathlib import Path
import requests
import datetime
import time

start_time = time.time()


parser = argparse.ArgumentParser()

parser.add_argument("path",type=Path,help='Please write the path for your JSON file')

parser.add_argument("-u","--unix", action="store_true")

args = parser.parse_args() 

if args.unix:
    u = True
else: 
    u = False

records = pd.read_json(args.path, lines=True)


# In[ ]:


# I will try to retrieve one instance of the file in a list of dictionaries
# import json
# df = [json.loads(line) for line in open('D:/iti/python/data/usa.json')]
# Print the first occurance
# records
# type(df)

# records = pd.DataFrame(df)


# In[7]:


# so now i just need to trun the dic list to data frame
rec_df = records.drop(['c', 'nk', 'gr', 'g', 'h', 'l', 'al', 'hh'], axis=1)
rec_df.columns


# In[8]:


rec_df


# ## Required

# In[9]:


import re
# this fun extract the browser from column a
def trn_to_web(line):
    return re.search(r"^[^\s/]+", line).group() 

rec_df['web_browser'] = rec_df['a'].apply(lambda x: trn_to_web(x))


# In[10]:


# this fun extract the browser from column a
def trn_to_os(line):
    y = 'Not Found'
    x = re.search(r"\([A-Za-z]+", line)
    if x is not None:
        t = x.group()
        y = re.search(r"[A-Za-z]+", t).group()
    return y

rec_df['operating_sys'] = rec_df['a'].apply(lambda x:trn_to_os(x))


# In[11]:


# this fun extract the FROM URL from column r
def trn_to_FURL(line):
    y = 'direct link'
    x = re.search(r"([A-Za-z]+(\.[A-Za-z]+)+)", line)
    if x is not None:
        y = x.group()
    return y

rec_df['from_url'] = rec_df['r'].apply(lambda x:trn_to_FURL(x))


# In[12]:


# this fun extract the browser from column a
def trn_to_TURL(line):
    return re.search(r"([A-Za-z]+(\.[A-Za-z]+)+)", line).group() 

rec_df['to_url'] = rec_df['u'].apply(lambda x: trn_to_TURL(x))


# In[13]:


# checking for nulls and try to cancel it
rec_df['cy'].isnull().sum()
rec_df['cy'].fillna('Not Found', inplace=True)

# this fun extract the browser from column a
def trn_to_city(line):
    return re.search(r"[A-Za-z]+.*[A-Za-z]+", line).group() 

rec_df['city'] = rec_df['cy'].apply(lambda x: trn_to_city(x))


# In[14]:


# checking for nulls and try to cancel it
rec_df['ll'].isnull().sum()
rec_df['ll'].fillna('Not Found', inplace=True)

# this fun extract the longitude from column ll
def trn_to_longit(line):
    y = 'Not Found'
    x = re.search(r"([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[Ee]([+-]?\d+))?", str(line)) # here i just casting to str
    if x is not None:
        y = x.group()

    return y

rec_df['longitude'] = rec_df['ll'].apply(lambda x : trn_to_longit(x))


# In[15]:


# this fun extract the latitude from column ll
def trn_to_latit(line):
    y = 'Not Found'
    x = re.findall(r"([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[Ee]([+-]?\d+))?", str(line))
    if len(x) > 0: # checking on the lst is empty or not
        y = x[1][0]

    return y

rec_df['latitude'] = rec_df['ll'].apply(lambda x : trn_to_latit(x))


# In[16]:


rec_df['tz'] = rec_df['tz'].str.replace(r'^\s*$', 'NotFound', regex=True) # replace any empty space with NOt Found
# this fun extract the browser from column a
def trn_to_TZ(line):
    return re.search(r"[^']*", line).group() 

rec_df['time_zone'] = rec_df['tz'].apply(lambda x: trn_to_TZ(x))


# In[17]:


import datetime # for converting unix time to datetime
def tim_con(x):
    return str(datetime.datetime.fromtimestamp(x))


# In[18]:


# for time in & out
if u == False:
    rec_df['time_in'] = rec_df['t'].apply(lambda x: tim_con(x))
    rec_df['time_out'] = rec_df['hc'].apply(lambda x: tim_con(x))
    
else:
    rec_df['time_in'] = rec_df['t']
    rec_df['time_out'] = rec_df['hc']


# In[19]:


tran_df = rec_df.drop(['a', 'tz', 'r', 'u', 't', 'hc', 'cy', 'll'], axis=1)


# In[20]:


tran_df


# In[21]:


# here i just tried to save the dataframe as a CSV file
tran_df.to_csv(r'data.csv')

#execution time
end_time = time.time()
total_time = end_time - start_time
print(f"Total execution time: {total_time} seconds")


# Write a script can transform the JSON files to a DataFrame and commit each file to a sparete CSV file in the target directory and consider the following:
# 
#         

# All CSV files must have the following columns
# - web_browser
#         The web browser that has requested the service
# - operating_sys
#         operating system that intiated this request
# - from_url
# 
#         The main URL the user came from
# 
#     **note**:
# 
#     If the retrived URL was in a long format `http://www.facebook.com/l/7AQEFzjSi/1.usa.gov/wfLQtf`
# 
#      make it appear in the file in a short format like this `www.facebook.com`
#      
#     
# - to_url
# 
#        The same applied like `to_url`
#    
# - city
# 
#         The city from which the the request was sent
#     
# - longitude
# 
#         The longitude where the request was sent
# - latitude
# 
#         The latitude where the request was sent
# 
# - time_zone
#         
#         The time zone that the city follow
#         
# - time_in
# 
#         Time when the request started
# - time_out
#         
#         Time when the request is ended
#         
#         
# **NOTE** :
# 
# Because that some instances of the file are incomplete, you may encouter some NaN values in your transforamtion. Make sure that the final dataframes have no NaNs at all.

# ### Script Details

# The Script itself must do the following before and after trasforamtion: 
#     
# - One positional argument which is the directory path with that have the files.
# 
# 
# - One optional argument **-u**. If this argument is passed will maintain the UNIX format of timpe stamp and if not                passed the time stamps will be converted.
# 
# 
# - Check if the files have any dublicates in between **checksum** and print a messeage that indicate that.
# 
# 
# - Print a message after converting each file with the number of rows transformed and the path of this file
# 
# 
# - At the end of this script print the total excution time.
#     
