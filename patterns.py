import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


country = "USA"
# Create a DataFrame
df = pd.read_excel('pwt1001.xlsx', sheet_name='Data')
df = df[df["countrycode"] == country]
df = df[df["year"] == country]

# Create subplots
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(8, 12))

# Plot population
df = df[df["countrycode"] == country]
df = df.dropna(subset=["pop"])
df = df.dropna(subset=["pl_con"])
df = df.dropna(subset=["emp"])

x = df['year']
y = df['pop']
fit = np.polyfit(x, y, 1)  # Fit a linear trendline (1st-degree polynomial)
axes[0].plot(x, y, marker='o', linestyle='-')
axes[0].plot(x, fit[0] * x + fit[1], color='red', linestyle='--', label='Trendline')
axes[0].set_ylabel('Total Population')
axes[0].set_title('Population')

# Plot Inflation Rate trendline
x = df['year']
y = df['pl_con']
fit = np.polyfit(x, y, 1)  # Fit a linear trendline (1st-degree polynomial)
axes[1].plot(x, y, marker='o', linestyle='--', color='orange')
axes[1].plot(x, fit[0] * x + fit[1], color='red', linestyle='--', label='Trendline')
axes[1].set_ylabel('Inflation Rate')
axes[1].set_title('Inflation Rate Trend')

# Plot Unemployment Rate trendline
x = df['year']
y = df['emp']
fit = np.polyfit(x, y, 1)  # Fit a linear trendline (1st-degree polynomial)
axes[2].plot(x, y, marker='o', linestyle='-.', color='green')
axes[2].plot(x, fit[0] * x + fit[1], color='red', linestyle='--', label='Trendline')
axes[2].set_xlabel('Year')
axes[2].set_ylabel('Unemployment Rate')
axes[2].set_title('Unemployment Rate Trend')

# Add legends
axes[0].legend()
axes[1].legend()
axes[2].legend()

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
