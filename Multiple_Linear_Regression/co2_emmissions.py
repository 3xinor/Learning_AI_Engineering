#!/usr/local/bin python3
"""
November 8, 2024
Dave Exinor

Co2 Emmisions Multiple Linear Regression model
Data Found here: https://open.canada.ca/data/en/dataset/98f1a129-f628-4ce4-b24d-6f16bf24dd64/resource/edba4afa-dc19-480c-bbe4-57992fc9d0d6
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Fuel Consumption (L/100km)
# CO2 Emissions (g/km)

# load data
df = pd.read_csv("Fuel_Consumption_Report.csv")
df.head()

cdf = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY', 'FUELCONSUMPTION_HWY', 'FUELCONSUMPTION_COMB', 'CO2EMMISSIONS']]
cdf.head(9)

plt.scatter(cdf.ENGINESIZE, cdf.CO2EMMISSIONS, color='blue')
plt.xlabel("Engine Size")
plt.ylabel("Emmission")
plt.show()