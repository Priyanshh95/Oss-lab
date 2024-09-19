#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello")


# In[2]:





# In[29]:


import numpy as np
import matplotlib.pyplot as plt

lions = np.array([15, 16, 17, 20, 19, 21, 23, 24, 25, 27])
elephants = np.array([50, 52, 54, 53, 55, 56, 57, 59, 60, 62])
zebras = np.array([100, 98, 95, 97, 96, 94, 95, 93, 92, 90])

species_data = {'Lions': lions, 'Elephants': elephants, 'Zebras': zebras}

def total_population(species):
    return np.sum(species)

def avg_yearly_population_growth(species):
    return (species[-1] - species[0]) / len(species)

for species, data in species_data.items():
    print(f"Total population of {species} over 10 years: {total_population(data)} thousand")
    print(f"Avg yearly population growth of {species}: {avg_yearly_population_growth(data):.2f} thousand/year")


# In[30]:


def year_over_year_growth_rate(species):
    return np.diff(species) / species[:-1] * 100

for species, data in species_data.items():
    growth_rate = year_over_year_growth_rate(data)
    print(f"Year-over-year growth rate for {species}:\n {growth_rate}")


# In[34]:


years = np.arange(1, 11)

plt.figure(figsize=(10, 6))
for species, data in species_data.items():
    plt.plot(years, data, label=species)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Population Trends')
plt.legend()
plt.grid(True)
plt.show()




# In[32]:


def highest_avg_growth_rate(species_data):
    growth_rates = {species: avg_yearly_population_growth(data) for species, data in species_data.items()}
    return max(growth_rates, key=growth_rates.get)

print(f"Species with the highest average growth rate: {highest_avg_growth_rate(species_data)}")

species_totals = [data[-1] for data in species_data.values()]
plt.bar(species_data.keys(), species_totals)
plt.xlabel('Species')
plt.ylabel('Population at Year 10 (in thousands)')
plt.title('Total Population of Each Species at Year 10')
plt.show()


# In[ ]:




