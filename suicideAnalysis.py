#!/usr/bin/env python
# coding: utf-8

# # Suicide Analysis: Shaping Insights for Change in India
# 
#  
#  **Suicides In India**
#  
#  ◾️ Suicide is considered as a disease and according to the report of WHO
#  
#  ◾️ Globally, suicide claims around 800,000 lives each year
#  
#  ◾️ It is a leading cause of death among youngster
#  
#  ◾️ Every hour, 1 **student commits suicide** in India
#  
#  ◾️ There are various causes of suicides like professional/career problems, sense of isolation, abuse, violence, family    problems, mental disorders, addiction to alcohol, financial loss, chronic pain etc.
#  
#  --------------------------------------------------------------------
#  

# **Project's Objective**
# 
# 🔶 Analyze historical suicide data to understand long-term trends and fluctuations.
# 
# 🔶 Identify the most vulnerable demographic groups and their unique risk factors.
# 
# 🔶 Advocate for mental health awareness and effective suicide prevention policies based on data-driven insights.
# 
# 
#  **Suicide is preventable through awareness, support, and access to mental health care**
#  
#  
#  ---------------------------------------------------------------------------

# **Stages Of Project**
# 
# ◾️ Data Collection
# 
# ◾️ Data Cleaning
# 
# ◾️ Analysis And Visualization
# 
# ◾️ Findings
# 
# -----------------------------------------------------------------------------
# 

# **Import all required packages / libraries**

# In[24]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# **Stage 1: Data Collection**
# 
# 🔷 The dataset we are utilizing is sourced from Kaggle [DataSet](https://www.kaggle.com/datasets/rajanand/suicides-in-india)
# 
# 🔷 This dataset encompasses data for the years spanning from __2001 to 2012__

# In[6]:


# Importing DataSet ( reading of dataset using pandas )

df = pd.read_csv('Suicides.csv')


# In[8]:


df.head()


# 
# -----------------------------------------------------------------------------
# 
# **Stage 2 : Data Cleaning**
# 

# In[9]:


# checking if data is correct or not or having any NaN values

df.isna().sum()


# __There are no NaN values__

# In[10]:


# check for any duplicate values in dataset

df.duplicated().sum()


# __There are no Duplicate values in the dataset__

# In[11]:


# Extract the unique values from the 'State' column

df['State'].unique()


# __The Total (All India) Total (States) Total (Uts) are not needed , so we will delete / drop them from dataset__

# In[12]:


df.drop(df[df['State']=='Total (States)'].index,inplace = True)

df.drop(df[df['State']=='Total (All India)'].index,inplace = True)

df.drop(df[df['State'] == 'Total (Uts)'].index, inplace = True)


# In[13]:


df['State'].unique()


# In[14]:


df.head()


# In[15]:


df['Year'].unique()


# In[16]:


df['Type_code'].unique()


# In[17]:


df['Type'].unique()


# __To remove columns named "Causes Not known," "Other Causes (Please Specify)," and "By Other means (please specify)" and change the name of "Bankruptcy or Sudden change in Economic," we can perform the following actions on our DataFrame in Python:__

# In[18]:


df.drop(df[df['Type'] == 'Other Causes (Please Specity)'].index, inplace = True)

df.drop(df[df['Type'] == 'Causes Not known'].index, inplace = True)

df.drop(df[df['Type'] == 'By Other means (please specify)'].index, inplace = True)

df['Type'] = df['Type'].replace(['Bankruptcy or Sudden change in Economic'],'Bankruptcy or Sudden change in Economic Status')


# In[19]:


df['Gender'].unique()


# In[20]:


df['Age_group'].unique()


# __we are going to make two DataFrames one contains 0-100 age group used to analysis total suicide countand another contains the without 0-100 age group to remove ambiguity in dataset while calculating age related analysis.__

# In[22]:


df_ab = df[df['Age_group'] != '0-100+']
df_ab


# 
# -----------------------------------------------------------------------------
# 
# **Stage 3: Analysis And Visualization of Data**
# 
#  🔴 Grouping data based on State counting the total suicides
#     

# In[35]:


df_state =df.groupby(by=['State']).sum().Total.sort_values(ascending = False)

# Define a custom color palette
custom_palette = sns.color_palette("Set2", len(df_state))

# Bargraph for State and Total count
plt.figure(figsize=(15,8))
sns.barplot(x=df_state,y=df_state.index, palette=custom_palette)
plt.xlabel('Total suicides')
plt.title('Suicides state wise')
plt.show()


# __Conclusion : - Maharashtra have the high number of suicide cases amoung all the states__

# -----------------------------------------------------------------------------
# 🔴 Visualizing Data Based on the Age_group and Gender and Count total Suicides

# In[55]:


data = df_ab[['Age_group','Gender','Total']]

edSort = data.groupby(['Age_group','Gender'],as_index=False).sum().sort_values('Total',ascending=False)

# Define a custom color palette
custom_palette2 = ["#7E1CBE","#FFC300"]

#BarGraph for Age_group, Gender and Total count

plt.figure(figsize=(12,6))
sns.barplot(x='Age_group',y='Total',hue='Gender',data=edSort,palette=custom_palette2)
plt.xlabel('Age Group')
plt.title('Based on Age Group')
plt.show()


# __Conclusion : - Suicide amoung Male is high than Female__

# -----------------------------------------------------------------------------
# 🔴 Visualizing Data Based on Age_group

# In[56]:


df_age = df_ab.groupby(by = ['Age_group'])

# BarGraph
plt.figure(figsize=(10,6))
sns.barplot(x=df_age.sum().Total.index,y=df_age.sum().Total.values)
plt.xlabel('Age')
plt.ylabel('Total')
plt.title('Age-wise suicide rate count')
plt.show()


# __Conclusion : - The Age groups 15-29 and 30-44 have the high suicide rates__

# -----------------------------------------------------------------------------
# 🔴 Visualizing Data Based on Year

# In[61]:


years = range(2001, 2013)  # Years from 2001 to 2012
sizes = []
total=df.shape[0]

for year in years:
    count = df[df['Year'] == year]['Year'].count()
    percentage = (count / total) * 100
    sizes.append(percentage)

# label for the pie chart
labels = [str(year) for year in years]

# Explode one of the slices 
explode = [0] * 10 + [0.4] + [0]

# Create the pie chart
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.2f%%',
        shadow=True, startangle=90)
ax1.axis('equal')

plt.show()


# __Conclusion : -The suicide rate is constant for all years__

# -----------------------------------------------------------------------------
# 
# 🔴 Visualizing Data based on Social Status

# In[63]:


# Filter data by Social_Status

df_social_st = df[df['Type_code']=='Social_Status']

# Grouping Data based on Social Status

df_socgrp = df_social_st.groupby(by=['Type'])
df_sgtotal = df_socgrp.sum().Total.sort_values(ascending = False)

# Bargraph based on Social Status

plt.figure(figsize=(12,7))
sns.barplot(x=df_sgtotal.index, y=df_sgtotal.values)
plt.title('Social Status')
plt.show()


# __Conclusion : - The highest number of suicides occur among individuals who are married__

# -----------------------------------------------------------------------------
# 
# 🔴 Visualizing bargraph based on Education Status and total suicides

# In[69]:


# Filter data based on type code

df_edu_st = df[df['Type_code']=='Education_Status']

# Grouping Data 

df_edugrp = df_edu_st.groupby(by = ['Type']).sum().Total.sort_values(ascending=True)

# Bargraph based on Education Status and total suicides

plt.figure(figsize=(13,7))
sns.barplot(y=df_edugrp.index,x=df_edugrp.values)
plt.ylabel('Education')
plt.title('Education status of suicide people')
plt.xlabel('Total')
plt.show()


# __Conclusion : - Higher educational status have low suicide count__

# 
# -----------------------------------------------------------------------------
# 
# 🔴 Visualizing Data of different professional profile

# In[65]:


# Filter the data based on type code

df_profile = df[df['Type_code']=='Professional_Profile']
df_profile= df_profile[df_profile['Type']!='Others (Please Specify)']

# Grouping Data of different professional profile

df_profilegroup = df_profile.groupby(by = ['Type']).sum().Total.sort_values(ascending=True)

# Bargraph for professional profile and total count

plt.figure(figsize=(13,7))
sns.barplot(y=df_profilegroup.index,x=df_profilegroup.values)
plt.title('Professional Profile')
plt.xlabel('Total')
plt.ylabel('Profession')
plt.show()


# __Conclusion : - The highest incidence of suicides is observed within the category of married house wifes.__

# -----------------------------------------------------------------------------
# 
# 🔴 Visualizing graph for different causes of suicide and total count

# In[66]:


# Filter data based on causes

filtered = np.where((df['Type_code'] == 'Causes'))

# Group the data

df_causesgroup = df.iloc[filtered].groupby(by = ['Type']).sum().Total.sort_values(ascending=True)

# graph for different causes and total count

plt.figure(figsize=(13,7))
sns.barplot(y=df_causesgroup.index,x=df_causesgroup.values)
plt.title('Causes')
plt.show()


# __Conclusion : - The primary cause of the highest number of suicides is family-related issues__

# -----------------------------------------------------------------------------
# 
# 🔴 Visualizing pie chart of age group 60+ and their reasons

# In[67]:


# filter Data based on age 60+

filtered = np.where(df['Age_group'] == '60+')
df_60 = df.iloc[filtered]

# removing unnecessary information

filtered = np.where(df_60['Type'] != 'Others (Please Specify)' )
df_60grp = df_60.groupby(by = ['Type']).sum().Total.sort_values(ascending=False)


# In[68]:


# pie chart of age group 60+ and their reasons

pie, ax = plt.subplots(figsize=[10,6])
data = df_60grp.values[11:1:-1]
keys = df_60grp.index[11:1:-1]
palette_color = sns.color_palette('dark')
plt.pie(x=data, autopct="%.1f%%", explode=[0.03]*10, labels=keys, pctdistance=0.5)
plt.xlabel(' 60+ group their profession and reasons')
plt.show()


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# 
# 
# __Insights derived from the analysis indicates...__
# 
# 📌 __Maharashtra__ have the high suicide count
# 
# 📌 __Suicide in male are more__ than female
# 
# 📌 __Married__ individuals committed more suicide
# 
# 📌 From professional profile, __house wife commit more suicide__
# 
# 📌 From the Analysis, __higher educational status have low suicide count__
# 
# 📌 __Family problems__ is the common and major causes for the high suicide count
# 

# In[ ]:




