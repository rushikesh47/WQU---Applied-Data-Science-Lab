# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 09:35:08 2022

@author: rushi
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data/mexico-real-estate-clean.csv')

# Question 1: Which state has the most expensive real estate?

mean_price_by_state = df.groupby('state')['price_usd'].mean().sort_values(ascending=False)


plt.bar(mean_price_by_state.index,mean_price_by_state)
plt.xlabel('State')
plt.ylabel('Mean Price [USD]')
plt.title("Mean House Price by State")

#Looks odd that Queretaro has the most expensive real estate when the GDP  numbers show its not even in the top 10 economies in Mexico.
#Reason for this could be the variation in house sizes so a better metric to look at would be price per m2

df['price_per_m2'] = df['price_usd']/df['area_m2']

mean_price_m2_by_state = df.groupby('state')['price_per_m2'].mean().sort_values(ascending=False)
mean_price_m2_by_state
plt.bar(mean_price_m2_by_state.index, mean_price_m2_by_state)
plt.xlabel('State')
plt.ylabel("Mean Price per M^2[USD]")
plt.title("Mean House Price per M^2 by State")


# Now we see that the capital Mexico City (Distrito Federal) is by far the most expensive market. Additionally, many of the top 10 states by GDP are also in the top 10 most expensive real estate markets. So it looks like this bar chart is a more accurate reflection of state real estate markets.

#Question 2: Is there a relationship between home size and price?

plt.scatter(x=df['area_m2'], y=df['price_usd'])
plt.xlabel('Area [sq meters]')
plt.ylabel("Price [USD]")
plt.title('Price vs Area')

#There seems to be a good amount of positive correlation  between size and price of houses

p_correlation = df['price_usd'].corr(df['area_m2'])
print(p_correlation)
# The correlation coefficient is over 0.5, so there's a moderate relationship house size and price in Mexico. 
# But does this relationship hold true in every state? Let's look at a couple of states, starting with Morelos.

df_morelos = df[df['state']=='Morelos']

plt.scatter(x = df_morelos['area_m2'], y = df_morelos['price_usd'])
plt.xlabel('Area [sq meters]')
plt.ylabel('Price [USD]')
plt.title("Morelos: Price vs. Area")

p_correlation = df_morelos['area_m2'].corr(df_morelos['price_usd'])
print(p_correlation)
# The plot and correlation factor suggests that in Morelos its even stronger

df_mexico_city = df[df['state'] == 'Distrito Federal']
df_mexico_city.head()

# Create a scatter plot price vs area
plt.scatter(x= df_mexico_city['area_m2'], y= df_mexico_city['price_usd'])
plt.xlabel('Area [sq meters]')
plt.ylabel('Price [USD]')
plt.title('Mexico City: Price vs. Area')


p_correlation = df_mexico_city['area_m2'].corr(df_mexico_city['price_usd'])
print(p_correlation)

# Looking at the scatter plot and correlation coefficient, there's see a weak relationship between size and price. How should we interpret this?

# One interpretation is that the relationship we see between size and price in many states doesn't hold true in the country's biggest and most economically powerful urban center because there are other factors that have a larger influence on price.

