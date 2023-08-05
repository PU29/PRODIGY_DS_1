import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("world_population.csv")

# Grouping data by continent and calculating the sum of population for each year
continent_population = data.groupby('Continent')[['2022 Population', '2020 Population', '2015 Population', '2010 Population', '2000 Population', '1990 Population', '1980 Population', '1970 Population']].sum()

# Creating a bar chart
plt.figure(figsize=(12, 6))
continent_population.plot(kind='bar')
plt.xlabel('Continent')
plt.ylabel('Total Population')
plt.title('Total Population by Continent for Different Years')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()
