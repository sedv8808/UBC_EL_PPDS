#!/usr/bin/env python
# coding: utf-8

# # UBC
# ## Programming in Python for DS
# 
# October 24, 2022  
# 
# Instructor: Socorro Dominguez Vidana

# In[1]:


import pandas as pd


# ### Module 2
# 
# Overview:
# 
# - [] Show how to use `.loc` and `.iloc`
# - [] Demonstrate how to rename columns of a dataframe using .rename()
# - [] Create new or columns in a dataframe using .assign() notation.
# - [] Drop columns in a dataframe using .drop()
# - [] Use df[] notation to filter rows of a dataframe.
# - [] Calculate summary statistics on grouped objects using .groupby() and .agg().
# 

# In[2]:


data = {'Animal': ['Falcon', 'Falcon',
                              'Parrot', 'Parrot'],
                   'Max Speed': [380., 370., 24., 26.],
                  'Min Speed': [120., 110., 5., 6.]}
data


# In[3]:


type(data)


# In[4]:


df = pd.DataFrame(data)
df


# In[5]:


pd.DataFrame(df)


# In[6]:


df.describe()


# ## `.loc`

# Select rows and columns based on `label`
# 
# The rule:
# 
# `df.loc[:, start:end:step]` or `df.loc[:, [labels]]`

# In[7]:


df.loc[:, 'Animal':'Max Speed']


# In[8]:


df.loc[:, ['Animal', 'Min Speed']]


# In[9]:


df.loc[0, ['Animal', 'Min Speed']]


# In[10]:


df.loc[0, 'Animal']


# #### `.iloc`

# Same as `loc` but works with index rather than label.

# In[11]:


df.iloc[0, 0]


# In[12]:


df.iloc[:,1]


# In[13]:


df.loc[:, 'Max Speed']


# #### `assign()`

# with `.loc[]`

# In[14]:


df.assign(new_col = df.loc[:, 'Max Speed']*2)


# Keep in mind you are not saving anything here - yet.

# In[15]:


df


# In[16]:


df  = df.assign(new_col = df.loc[:, 'Max Speed']*2)
df


# In[17]:


df


# without `.loc[]`

# In[18]:


df.assign(new_col2 = df['Max Speed']*2)
df.assign( new_col = df.loc[:, 'Max Speed']*2)


# In[19]:


df


# without `.assign()`

# In[20]:


df['new_col3'] = df['Max Speed']*2


# In[21]:


df


# In[22]:


df['new_col3']


# #### `.drop()`

# In[23]:


df.drop(columns = 'Max Speed')


# In[24]:


df


# In[25]:


df.drop(columns = ['Animal', 'Max Speed'])


# In[26]:


df


# In[27]:


df = df.drop(columns = 'new_col3')


# In[28]:


df


# In[29]:


df.rename(columns = {'Max Speed':'max_speed', 
                     'new_col':'speedx2'})


# In[30]:


df


# In[31]:


df.shape 


# In[32]:


df.columns = ['_animal', '_max_speed', '_min_speed', '_speed2']


# In[33]:


df


# #### `filter`

# In[34]:


df


# In[35]:


df['_max_speed'] > 300


# In[36]:


df[df['_max_speed'] > 300]


# ```python
# df[(_____) & (_____)]
# ```

# In[37]:


df[(df['_max_speed'] > 320) & (df['_max_speed'] < 380)]


# #### `.groupby()`

# In[38]:


df


# In[39]:


df.groupby('_animal')


# **What does that even mean??**
# 

# ![](https://media1.giphy.com/media/FcuiZUneg1YRAu1lH2/giphy.gif?cid=ecf05e47t6tl4ppzchujy27worbrevfetpm299tixcfm7sk6&rid=giphy.gif&ct=g)

# ![img](https://miro.medium.com/max/1206/0*5Zzcwe-rlxz-EQ_N)
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# In[40]:


df[df['_animal'] == 'Falcon']


# In[41]:


df2 = df.groupby('_animal').sum()
df2


# `reset_index()`

# In[42]:


df.groupby('_animal').sum()


# In[43]:


df.groupby('_animal').sum().reset_index()


# In[44]:


df.groupby('_animal', as_index=False).sum()


# In[45]:


df2.columns


# In[46]:


df2 = df2.reset_index()
df2


# In[47]:


df3 = df.groupby('_animal').agg({'_max_speed':['mean', 'sum']})
df3


# In[48]:


df3.reset_index()


# In[49]:


df3[df3['_max_speed', 'mean'] > 300]


# In[50]:


df.groupby('_animal').agg(['mean', 'sum']).loc[:,'_max_speed'].reset_index()


# Is there only **ONE** way of doing things?

# ![](https://media2.giphy.com/media/ftqLysT45BJMagKFuk/giphy.gif?cid=ecf05e47zx1vugxxgh9hyet02mwendrr6tfopa20ysvst7pi&rid=giphy.gif&ct=g)

# **The tests are a guide.**
# 
# We cannot make very strict tests. 
# - Inhibit your creativity. 
# 
# We cannot make very lenient tests.
# - Cannot test your output
# 
# Tests are based on:
# - An ideal of best practices
# - Tidy data (more on this next week)
# - A bit of hand holding to make your life in future questions "easier"
# - Beginner friendly skills (if you are a pro, you might find them quite limiting) 
# 
# 

# **Disclaimer:**
# If you want the full mark, you need to pass the test.
# 
# How?
# 
# | NO | YES |
# | --- | --- |
# | ![](https://media3.giphy.com/media/9bXjoBk28pwnKLKoKb/giphy.gif?cid=ecf05e476d0x3f361cv2upqr8x6p1whtx5ggazdhrsoigmf0&rid=giphy.gif&ct=g) | ![](https://media4.giphy.com/media/anSiSGG5YaXeBn5gv4/giphy.gif?cid=ecf05e476d0x3f361cv2upqr8x6p1whtx5ggazdhrsoigmf0&rid=giphy.gif&ct=g)|
# 
# Read the bottom part of the error messages, you might find them helpful.

# 
# #### Summary
# 
# ##### What we did?
# 
# - [x] Show how to use `.loc` and `.iloc`
# - [x] Demonstrate how to rename columns of a dataframe using .rename()
# - [x] Create new or columns in a dataframe using .assign() notation.
# - [x] Drop columns in a dataframe using .drop()
# - [x] Use df[] notation to filter rows of a dataframe.
# - [x] Calculate summary statistics on grouped objects using .groupby() and .agg().

# ##### Extra (time allowing)
# 
# How to change labels based on multiple conditions for different columns (Age in Titanic)

# In[51]:


df = pd.DataFrame({'Animal': ['Falcon', 'Falcon',
                              'Parrot', 'Parrot'],
                   'Max Speed': [380., 370., 24., 26.]})
df


# In[52]:


import numpy as np

conditions = [
    ((df['Animal'] == 'Falcon') & (df['Max Speed'] < 350)),
    ((df['Animal'] == 'Falcon') & (df['Max Speed'] >= 350)),
    ((df['Animal'] == 'Parrot') & (df['Max Speed'] <= 300)),
    ((df['Animal'] == 'Parrot') & (df['Max Speed'] > 300))
    ]

# create a list of the values we want to assign for each condition
values = ['slow_falcon', 'fast_falcon', 'avg_parrot', 'vfast_parrot']

# create a new column and use np.select to assign values to it using our lists as arguments
df['class'] = np.select(conditions, values)

df

