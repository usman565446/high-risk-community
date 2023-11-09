# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 08:46:29 2023

@author: Malik
"""

import pandas as pd
data = pd.read_csv("C:\\Users\\Malik\\Downloads\\covid-geography\\mmsa-icu-beds.csv")
print(data.head())


import matplotlib.pyplot as plt

# line plot
plt.figure(figsize=(12, 6))
data_subset = data.iloc[::5]  # Show every 5th label
plt.plot(data_subset['MMSA'], data_subset['total_at_risk'], marker='o', linestyle='-')
plt.xlabel('MMSA')
plt.ylabel('Total at Risk')
plt.title('Total at Risk by MMSA')
plt.xticks(rotation=90)
plt.grid(True)
plt.show()

## Bar Chart
plt.figure(figsize=(12, 6))
data_subset = data.iloc[::5]  # Show every 5th label
plt.bar(data_subset['MMSA'], data_subset['total_percent_at_risk'])
plt.xlabel('MMSA')
plt.ylabel('Total Percent at Risk')
plt.title('Total Percent at Risk by MMSA')
plt.xticks(rotation=90)
plt.show()

## SCatter plot
plt.figure(figsize=(8, 6))
plt.scatter(data['high_risk_per_ICU_bed'], data['high_risk_per_hospital'], s=data['icu_beds']*5, c=data['total_at_risk'], cmap='viridis')
plt.xlabel('High Risk per ICU Bed')
plt.ylabel('High Risk per Hospital')
plt.title('Relationship between High Risk per ICU Bed and High Risk per Hospital')
plt.colorbar(label='Total at Risk')
plt.show()