import matplotlib.pyplot as plt
import pandas as pd

country = "NLD"
# Create a DataFrame
df = pd.read_excel('pwt1001.xlsx', sheet_name='Data')
df = df[df["countrycode"] == country]

# Create a figure with a single subplot
fig, ax = plt.subplots(figsize=(8, 6))

# Plot Population
df_pop = df.dropna(subset=["pop"])
x_pop = df_pop['year']
y_pop = df_pop['pop']
ax.plot(x_pop, y_pop, marker='o', linestyle='-', label='Population')

# Plot Unemployment Rate as a percentage of Population
df_unemployment = df.dropna(subset=["emp"])
y_unemployment_per = df_unemployment['emp'] / df_unemployment['pop'] * 100  # Calculate unemployment rate as a percentage
ax.plot(x_pop, y_unemployment_per, marker='o', linestyle='-.', color='green', label='Unemployment Rate (%)')

ax.set_xlabel('Year')
ax.set_ylabel('Value in millions / Unemployment Rate (%)')
ax.set_title('Population and Unemployment Rate for {}'.format(country))
ax.legend()

# Show the plot
plt.tight_layout()
plt.show()
