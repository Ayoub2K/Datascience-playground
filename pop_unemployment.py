import matplotlib.pyplot as plt
import pandas as pd

country = "USA"
# Create a DataFrame
df = pd.read_excel('pwt1001.xlsx', sheet_name='Data')
df = df[df["countrycode"] == country]

df_unemployment = df.dropna(subset=["emp"])
x_unemployment = df_unemployment['year']
y_unemployment = df_unemployment['emp']

# Create a figure with a single subplot
fig, ax1 = plt.subplots(1, 1, figsize=(8, 6))

# Plot Population and Unemployment Rate
df_pop = df.dropna(subset=["pop"])
x_pop = df_pop['year']
y_pop = df_pop['pop']
ax1.plot(x_pop, y_pop, marker='o', linestyle='-', label='Population (number in millions)')
ax1.plot(x_unemployment, y_unemployment, marker='o', linestyle='-.', color='green', label='Unemployment Rate (number in millions)')
ax1.set_xlabel('Year')
ax1.set_ylabel('Value')
ax1.set_title('Population and Unemployment Rate (number in millions) for {}'.format(country))
ax1.legend()

# Adjust subplot spacing
plt.tight_layout()

# Show the plots
plt.show()
