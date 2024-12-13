#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 
import seaborn as sb
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import datetime as dt

import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[2]:


df = pd.read_csv("../DataSets/project data.csv")
df


# In[3]:


df["Daily_Return"] = (df.Close - df.Open) / df.Open * 100
df


# In[4]:


df["Price_Range"] = df.High - df.Low 
df


# In[5]:


df["Volatility"] = (df.High - df.Low) / df.Close * 100
df


# In[6]:


df['Cumulative_Return'] = (df['Adj Close'].pct_change()).cumsum()
df


# In[7]:


df["Average_Price"] = (df.Open + df.Close) / 2 
df


# # Data Visualisation

# In[8]:


#count plot 
plt.figure(figsize=(10,6))
sb.countplot( x=df.Symbol)
plt.xticks(rotation=90)


# In[9]:


plt.figure(figsize=(10,6))
sb.countplot( x=df.Category)
plt.xticks(rotation=90)


# In[10]:


avg_daily_return = df.groupby('Category')['Daily_Return'].mean().reset_index()
avg_daily_return


# In[11]:


plt.figure(figsize=(10,6))
sb.barplot(data=avg_daily_return, x='Category', y='Daily_Return')
plt.xticks(rotation=45, ha='right')
plt.title('Average Daily Return by Sector')
plt.xlabel('Symbol')
plt.ylabel('Average Daily Return')
plt.show()


# In[12]:


volatility_by_sector = df.groupby('Category')['Daily_Return'].std().reset_index()
volatility_by_sector


# In[13]:


plt.figure(figsize=(10,6))
sb.barplot(data=volatility_by_sector, x='Category', y='Daily_Return')
plt.xticks(rotation=45, ha='right')
plt.title('Average Volatility by Sector (Standard Deviation of Daily Return)')
plt.xlabel('Symbol')
plt.ylabel('Volatility (Standard Deviation)')


# In[14]:


avg_price_range = df.groupby('Category')['Price_Range'].mean().reset_index()
avg_price_range


# In[15]:


plt.figure(figsize=(10,6))
sb.barplot(data=avg_price_range, x='Category', y='Price_Range')
plt.xticks(rotation=45, ha='right')
plt.title('Average Price Range by Sector')
plt.xlabel('Symbol')
plt.ylabel('Average Price Range')
plt.show()


# In[16]:


#line plot
plt.figure(figsize=(10,6))
sb.lineplot(x=df.Symbol, y=df.Volatility)
plt.title('Volatility Symbol Over Time')
plt.xticks(rotation=90)
plt.show()


# In[17]:


plt.figure(figsize=(10,6))
sb.lineplot(x=df.Close, y=df.Symbol)
plt.title('Volatility Symbol Over Time')
plt.xticks(rotation=90)
plt.show()


# In[18]:


#pie plot
sector_counts = df['Category'].value_counts()
plt.figure(figsize=(8,8))
plt.pie(sector_counts, labels=sector_counts.index)
plt.title('Proportion of Stocks by Sector')
plt.axis('equal')
plt.show()


# In[19]:


sector_cumulative_return = df.groupby('Category')['Cumulative_Return'].sum()
plt.figure(figsize=(8,8))
plt.pie(sector_cumulative_return, labels=sector_cumulative_return.index)
plt.title('Percentage of Total Cumulative Return by Sector')
plt.axis('equal')
plt.show()


# In[20]:


df.Daily_Return.fillna(0,inplace=True)


# In[21]:


#histplot
sb.histplot(df.Daily_Return)
plt.title('Distribution of Daily Returns')
plt.show()


# In[22]:


sb.histplot(df.Close)
plt.title('Distribution of close')
plt.show()


# In[23]:


sb.histplot(df.Price_Range)
plt.title('Distribution of Price_Range')
plt.show()


# In[24]:


#pointplot
sb.pointplot(x=df.Category, y=df.Price_Range)
plt.title('Price Range of Sectors')
plt.show()


# In[25]:


plt.figure(figsize=(10,5))
sb.pointplot(x=df.Category, y=df.Daily_Return)
plt.title('daily_Return of Sectors')
plt.show()


# In[26]:


#Stripplot 
plt.figure(figsize=(10,8))
sb.stripplot(x=df.Category, y=df.Daily_Return)
plt.title('Spread of Daily Returns Across Sectors')
plt.show()


# In[27]:


plt.figure(figsize=(10,4))
sb.stripplot(x=df.Category, y=df.Volatility)
plt.title('Spread of Volatility Across Sectors')
plt.show()


# In[28]:


#Violin Plot 
plt.figure(figsize=(10,4))
plt.figure(figsize=(10,4))
sb.violinplot(x=df.Category, y=df.Daily_Return)
plt.title('Spread of Volatility Across Sectors')
plt.show()


# In[29]:



plt.figure(figsize=(10,4))
sb.violinplot(x=df.Category, y=df.Volatility)
plt.title('Spread of Volatility Across Sectors')
plt.show()


# In[30]:


#swarmplot
plt.figure(figsize=(10,4))
sb.swarmplot(x=df.Category, y=df.Close)
plt.title('Spread of Close Across Sectors')
plt.show()


# In[31]:


plt.figure(figsize=(15,10))
sb.swarmplot(x=df.Symbol, y=df.Volatility)
plt.title('Spread of Volatility Across Sectors')
plt.xticks(rotation=90)
plt.show()


# In[32]:


#Scatter Plot 
plt.figure(figsize=(12,8))
sb.scatterplot(data=df, x='Open', y='Close', hue='Symbol')
plt.title('Relationship Between Open and Close Prices for Different Symbols')
plt.xlabel('Opening Price')
plt.ylabel('Closing Price')
plt.show()


# In[33]:


#Scatter Plot 
plt.figure(figsize=(12,8))
sb.scatterplot( x=df.Daily_Return, y=df.Volatility)
plt.title('Relationship Between Daily_Return and Volatility')
plt.xlabel('Daily_Return')
plt.ylabel('.Volatility Price')
plt.show()


# In[34]:


plt.figure(figsize=(12,8))
sb.scatterplot( x=df.Close, y=df.Price_Range)
plt.title('Relationship Between Close and Price_Range')
plt.xlabel('Close')
plt.ylabel('Price_Range')
plt.show()


# In[35]:


plt.figure(figsize=(12,8))
sb.boxplot(x=df.Category , y=df.Daily_Return)
plt.title('Distribution of Category by Daily_Return')
plt.xlabel('Category')
plt.ylabel('Daily_Return')
plt.show()


# In[36]:


plt.figure(figsize=(12,8))
sb.boxplot(x=df.Symbol , y=df.Price_Range)
plt.title('Distribution of Symbol by Price_Range')
plt.xticks(rotation=90)
plt.show()


# In[37]:


#Pairplot 
price_data = df[['Open', 'Close', 'High', 'Low']]
sb.pairplot(price_data)
plt.suptitle('Pair Plot of Open, Close, High, and Low')
plt.show()


# In[38]:


price = df[["Daily_Return","Price_Range", "Volatility","Category"]]
sb.pairplot(price)
plt.suptitle('Pair Plot of Open, Close, High, and Low')
plt.show()


# In[39]:


#Jointplot 
sb.jointplot(x=df.Daily_Return, y=df.Volatility,kind='kde')
plt.title('Daily Return vs Volatility with KDE')
plt.show()


# In[40]:


sb.jointplot(x=df.Price_Range, y=df.Close,)
plt.title(' price range and closing price relate with both scatter')
plt.show()


# In[41]:


#KDE Plot 
sb.kdeplot(df['Daily_Return'])
plt.title('Density Distribution of Daily Returns')
plt.show()


# In[42]:


sb.kdeplot(df[['Volatility','Category']])
plt.title(' volatility differ for stocks from different sectors')
plt.show()


# In[ ]:




