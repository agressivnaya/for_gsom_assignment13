import seaborn as sns
import matplotlib.pyplot as plt

# Load the car_crashes dataset
car_crashes = sns.load_dataset('car_crashes')

# Set seaborn style for better visualization
sns.set(style='whitegrid')

# the first visualisation
plt.figure(figsize=(6, 5))
sns.heatmap(car_crashes.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Car Accident Factors')
plt.show()

# the second visualisation
plt.figure(figsize=(8, 6))
sns.scatterplot(data=car_crashes, x='ins_premium', y='ins_losses', hue='abbrev', size='total')
plt.title('Insurance Premium vs. Insurance Losses by State')
plt.xlabel('Insurance Premium ($)')
plt.ylabel('Insurance Losses ($)')
plt.legend(title='State')
plt.show()

# the third visualisation
plt.figure(figsize=(10, 5))
sns.barplot(data=car_crashes, x='abbrev', y='speeding', palette='coolwarm')
plt.title('Percentage of Drivers Speeding in Fatal Collisions')
plt.xlabel('State Abbreviation')
plt.ylabel('Percentage Speeding')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()