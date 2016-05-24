
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
from math import ceil
import pickle
with open('datapath.txt') as f:
    datapath=f.readlines()[0].rstrip()




# In[3]:

with open('feature_dtypes.pkl', 'r') as f:
    featuredtypes=pickle.load(f)


# In[4]:

dates=[u'srch_ci', u'srch_co','date_time']


# There are some check in/check out dates that this parser can't parse that might be recoverable (ex: someone searched for a checkin date in the year 2557, which is too large for the date time format), but it mostly does a good job.

# In[5]:

parser=lambda x: pd.to_datetime(x, format='%Y-%m-%d',errors='coerce')


# ## Iteration

# In[9]:

nchunks=20
chunksize=ceil(totaltrainrows/nchunks)


# In[10]:

samplerate=0.3


# In[11]:

#%%time
trainit=pd.read_csv(datapath+'train.csv',chunksize=chunksize,iterator=True,dtype=featuredtypes,parse_dates=dates,date_parser=parser)
ichunk=0
for chunk in trainit:
    #Comment the line below to create a sample of the full dataset, not just those where is_booking==True
    chunk=chunk[chunk['is_booking']==True]
    if ichunk==0:
        sample=chunk.sample(frac=samplerate)
    else:
        sample=sample.append(chunk.sample(frac=samplerate),ignore_index=True)
    print('finished chunk '+str(ichunk))
    ichunk+=1


# In[12]:

print('sample shape='+str(sample.shape))


# In[99]:

sample.to_csv(datapath+'thirty_perc_booked_sample.csv')

