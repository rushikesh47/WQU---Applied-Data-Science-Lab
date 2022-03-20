# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 20:34:20 2022

@author: rushi
"""

import pandas as pd

# Importing all the csv data in dataframes
df1 = pd.read_csv(r'data/mexico-real-estate-1.csv')
df2 = pd.read_csv(r'data/mexico-real-estate-2.csv')
df3 = pd.read_csv(r'data/mexico-real-estate-3.csv')
df1.info()
df1.head()

# Data Preparation for first csv 
df1.dropna(inplace=True)
df1['price_usd'] = df1['price_usd'].str.replace('$','')
df1['price_usd'] = df1['price_usd'].str.replace(',','')
df1['price_usd'] = df1.price_usd.astype(float)

# Data Preparation for second csv 
df2.info()
df2.dropna(inplace=True)
df2.head()

df2['price_usd'] = df2['price_mxn']/19
df2.head()
df2=df2.drop('price_mxn', axis='columns')

#Data Preparation for Thrid csv
df3.info()
df3.head()

df3.dropna(inplace=True)
df3[['lat','lon']] = df3['lat-lon'].str.split(',', expand=True)
df3.head()
df3['state'] = df3['place_with_parent_names'].str.split('|', expand=True)[2]
df3.head()

df3=df3.drop(['lat-lon','place_with_parent_names'], axis='columns')
df3.head()


df = pd.concat([df1,df2,df3])
print(df.shape)
df.head()

df.to_csv('data/mexico-real-estate-clean.csv', index=False)
