import numpy as np
import pandas as pd

income = np.array([10000, 15000, 13000, 12000, 16000, 11000, 14000, 17000, 12500, 13500])
income_without_tax = income * 0.7
expenses = np.array([7000, 8000, 7500, 6000, 9000, 8500, 7200, 10000, 6500, 8000])
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(months, income, marker='o', linestyle='-', color='b', label='Income')
plt.title('Income by Month')
plt.xlabel('Months')
plt.ylabel('Income ($)')
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

savings = np.maximum(income_without_tax - expenses, 0)

plt.figure(figsize=(7, 4))
plt.bar(months, savings, color='green', label='Savings')
plt.title('Savings by Month')
plt.xlabel('Months')
plt.ylabel('Savings ($)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(5, 5))

colors = plt.cm.Paired(np.arange(len(months))) # Generates some colors for the pie slices

plt.pie(savings, labels=months, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Monthly Savings as a Percentage of Annual Savings')
plt.show()

import statistics as stats

# Dividing income by quarters
quarter1 = income[0:3] # Jan, Feb, Mar
quarter2 = income[3:6] # Apr, May, Jun
quarter3 = income[6:9] # Jul, Aug, Sep
quarter4 = income[9:12] # Oct, Nov, Dec

# Calculating the average income for each quarter
average_income_q1 = stats.mean(quarter1)
average_income_q2 = stats.mean(quarter2)
average_income_q3 = stats.mean(quarter3)
average_income_q4 = stats.mean(quarter4)

# Printing out the average income for each quarter
print(f"Average income for Quarter 1: {average_income_q1}")
print(f"Average income for Quarter 2: {average_income_q2}")
print(f"Average income for Quarter 3: {average_income_q3}")
print(f"Average income for Quarter 3: {average_income_q4}")

average_incomes = [average_income_q1, average_income_q2, average_income_q3, average_income_q4]
quarters = ['Q1', 'Q2', 'Q3', 'Q4']

# Creating the bar chart
plt.figure(figsize=(7, 4))
plt.bar(quarters, average_incomes, color=['coral', 'skyblue', 'lightgreen', 'cyan'])
plt.title('Average Income per Quarter')
plt.xlabel('Quarter')
plt.ylabel('Average Income ($)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.ylim(0, 17000) # Set y-axis limits for readability
plt.tight_layout()

plt.show()