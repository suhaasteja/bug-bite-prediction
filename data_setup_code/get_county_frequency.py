import csv
from collections import Counter

def get_column_value_frequencies(csv_file, column_name):
    """
    Reads a specified column from a CSV file and returns a dictionary with the 
    frequency of each value in the column.

    Parameters:
    csv_file (str): The path to the CSV file.
    column_name (str): The name of the column to extract frequencies from.

    Returns:
    dict: A dictionary with keys as unique values from the column and values as their frequencies.
    """
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.DictReader(file)  # Use DictReader to read the CSV by column names
        values = [row[column_name] for row in reader if column_name in row]  # List of all values in the column

    return dict(Counter(values))  # Return a dictionary with the frequency of each value

# Usage example
csv_path = '/Users/mac/Desktop/bug-bite-prediction/training_csv/no_bites_training.csv'
column_to_read = 'county_name'  # Replace 'county_name' with your actual column name
value_frequencies = get_column_value_frequencies(csv_path, column_to_read)

print(value_frequencies)
