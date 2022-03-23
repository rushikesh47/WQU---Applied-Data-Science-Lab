# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 09:34:33 2022

@author: rushi
"""

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly
pio.renderers.default='svg'

df = pd.read_csv('data/mexico-real-estate-clean.csv')


# Visualizing the data using lat and lon values 
fig = px.scatter_mapbox(
    df,  # Our DataFrame
    lat="lat",
    lon="lon",
    center={"lat": 19.43, "lon": -99.13},  # Map will be centered on Mexico City
    width=600,  # Width of map
    height=600,  # Height of map
    hover_data=["price_usd"],  # Display price when hovering mouse over house
)

fig.update_layout(mapbox_style="open-street-map")
# Looking at this map we can see that the houses are concentrated in certain areas


plotly.offline.plot(fig, filename="plots/map.html")

#Viewing 10 most prevalent states

df['state'].value_counts().head(10)

#Analyzing the statistical parameters for price and area
df[['area_m2','price_usd']].describe()

# Let's start by looking at "area_m2". It's interesting that the mean is larger than the median (another name for the 50% quartile). Both of these statistics are supposed to give an idea of the "typical" value for the column, so why is there a difference of almost 15 m2 between them? To answer this question, we need to see how house sizes are distributed in our dataset. Let's look at two ways to visualize the distribution: a histogram and a boxplot.

plt.hist(df['area_m2'])
plt.xlabel('Area [sq meters]')
plt.ylabel('Frequency')
plt.title('Distribution of Home Sizes')

#Looking at our histogram, we can see that "area_m2" skews left. In other words, there are more houses at the lower end of the distribution (50–200m2) than at the higher end (250–400m2). That explains the difference between the mean and the median.

plt.boxplot(df['area_m2'], vert=False)
plt.xlabel('Area [sq meters]')
plt.title('Distribution of Home Sizes')

#To verify if price has the same distribution as the area we'll plot the same two graphs for it

plt.hist(df['price_usd'])
plt.xlabel('Price [USD]')
plt.ylabel('Frequency')
plt.title('Distribution of Home Prices')

#Looks like "price_usd" is even more skewed than "area_m2". What does this bigger skew look like in a boxplot?

plt.boxplot(df['price_usd'], vert = False)
plt.xlabel('Price [USD]')
plt.title('Distribution of Home Prices')

#Looks like price USD has some outliers
#This marks the end of EDA for this dataset