#  AI Assingment
# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'Literacy Rate.csv'  # Ensure this file is in the same directory as the script
data = pd.read_csv("./dataset/Literacy Rate.csv")

# Clean the dataset (drop NaN values for simplicity)
clean_data = data.dropna()

# Select the top 10 countries for visualization
top_countries = clean_data.head(10)

# Extract relevant columns
countries = top_countries['Country']
literacy_rates = top_countries['Literacy Rate'] * 100  # Convert to percentage

# Creating the plot
plt.figure(figsize=(12, 6))
plt.bar(countries, literacy_rates, color='skyblue', edgecolor='black')

# Adding labels and title
plt.title('Literacy Rates of Top 10 Countries', fontsize=16)
plt.xlabel('Country', fontsize=14)
plt.ylabel('Literacy Rate (%)', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()
