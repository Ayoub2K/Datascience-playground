import matplotlib.pyplot as plt
import pandas as pd

country = "USA"
# Create a DataFrame
df = pd.read_excel('pwt1001.xlsx', sheet_name='Data')
df = df[df["countrycode"] == country]

# Create a figure with a single subplot
fig, ax1 = plt.subplots(1, 1, figsize=(8, 6))

# Plot Unemployment Rate as a percentage of Population
df_unemployment = df.dropna(subset=["emp"])
x_unemployment = df_unemployment['year']
y_unemployment = df_unemployment['emp'] / df_unemployment['pop'] * 100  # Calculate unemployment rate as a percentage
ax1.plot(x_unemployment, y_unemployment, marker='o', linestyle='-.', color='green')
ax1.set_ylabel('Unemployment Rate (%)')
ax1.set_title('Unemployment Rate (% of Population) for {}'.format(country))

# Adjust subplot spacing
plt.tight_layout()

# Show the plots
plt.show()
