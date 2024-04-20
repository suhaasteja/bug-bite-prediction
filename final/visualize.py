# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# List of CSV file names
file_names = [
    "bug_bites_data - Spider (training).csv",
    "bug_bites_data - ants (training)(1).csv",
    "bug_bites_data - begbugs (training).csv",
    "bug_bites_data - chiggers (training).csv",
    "bug_bites_data - fleas (training).csv",
    "bug_bites_data - mosquitos (training).csv",
    "bug_bites_data - no_bites (training).csv",
    "bug_bites_data - ticks (training).csv"
]

# Specific column to visualize
column_name = 'county_name'

# Define high-contrast color palettes for each file
colors = [
    ['#FF5733', '#33FFCE', '#33B5FF', '#3352FF', '#A933FF'],
    ['#FFD333', '#FF8333', '#FF3333', '#FF3396', '#FF33E8'],
    ['#33FF57', '#8CFF33', '#E5FF33', '#FFCE33', '#FF8C33'],
    ['#333EFF', '#6C33FF', '#A033FF', '#D433FF', '#FF33C7'],
    ['#33FFDA', '#33FF92', '#33FF57', '#92FF33', '#DAFF33'],
    ['#33C7FF', '#338CFF', '#3352FF', '#3327FF', '#6C33FF'],
    ['#FF8C33', '#FF5733', '#FF3333', '#FF3370', '#FF33AF'],
    ['#D4FF33', '#9EFF33', '#67FF33', '#33FF52', '#33FF8B']
]

# Create a figure to hold the pie charts
fig, axes = plt.subplots(3, 3, figsize=(15, 15))  # Adjust grid size based on number of files
axes = axes.flatten()

# Loop through each file and plot the column data in a pie chart
for idx, file_name in enumerate(file_names):
    # Read the CSV file
    df = pd.read_csv(file_name)
    
    # Check if the column exists in the DataFrame
    if column_name in df.columns:
        # Get the value counts
        counts = df[column_name].value_counts()
        
        # Plot the pie chart in its subplot
        axes[idx].pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90, colors=colors[idx % len(colors)])
        axes[idx].set_title(file_name.split(' - ')[1])  # Title as the bug type

# Hide unused axes if any
for i in range(len(file_names), len(axes)):
    axes[i].set_visible(False)

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
