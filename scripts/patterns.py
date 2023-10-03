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
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

# Plot Population and Unemployment Rate
df_pop = df.dropna(subset=["pop"])
x_pop = df_pop['year']
y_pop = df_pop['pop']
ax1.plot(x_pop, y_pop, marker='o', linestyle='-', label='Population ')
ax1.plot(x_unemployment, y_unemployment, marker='o', linestyle='-.', color='green', label='Unemployment Rate')
ax1.set_xlabel('Year')
ax1.set_ylabel('Value in millions')
ax1.set_title('Population and Unemployment Rate  for {}'.format(country))
ax1.legend()

# Plot Unemployment Rate as a percentage of Population
df_unemployment = df.dropna(subset=["emp"])
y_unemployment_per = df_unemployment['emp'] / df_unemployment['pop'] * 100  # Calculate unemployment rate as a percentage
ax2.plot(x_unemployment, y_unemployment_per, marker='o', linestyle='-.', color='green')
ax2.set_ylabel('Unemployment Rate (%)')
ax2.set_title('Unemployment Rate (% of Population) for {}'.format(country))

# Adjust subplot spacing
plt.tight_layout()

# Show the plots
plt.show()
