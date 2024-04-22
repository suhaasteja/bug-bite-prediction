import csv
import random

def random_select_from_dict(data_dict, num_items):
    if num_items > len(data_dict):
        raise ValueError("The number of items requested exceeds the number of items available.")
    selected_keys = random.sample(list(data_dict.keys()), num_items)
    return {key: data_dict[key] for key in selected_keys}

def update_csv_with_counties(csv_file, selected_counties):
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        rows = list(reader)  # Convert iterator to list to reuse

    if len(rows) < len(selected_counties):
        raise ValueError("Not enough rows in the CSV file to match the number of selected counties.")
    
    # Assign county names to each row
    for row, county in zip(rows, selected_counties):
        row['county_name'] = county

    # Write the updated data back to the CSV
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)

# Data from your JSON
county_data = {
  "Los Angeles": 60,
  "San Jose": 40,
  "Sonoma": 21,
  "San Francisco": 17,
  "San Diego": 12,
  "Oakland": 11,
  "Sacramento": 9,
  "Bakersfield": 9,
  "Humboldt": 6,
  "Vallejo": 5,
  "Pomona": 4,
  "Fresno": 4,
  "Anaheim": 3,
  "": 79
}

# Randomly select county names
num_items = 14  # Adjust to match the number of rows in your CSV
try:
    selected_items = random_select_from_dict(county_data, num_items)
    selected_counties = list(selected_items.keys())
except ValueError as e:
    print(e)
    exit(1)

# Update CSV with the selected counties
csv_path = '/Users/mac/Desktop/bug-bite-prediction/data_setup_code/image_names_ticks.csv'  # Path to your CSV file
try:
    update_csv_with_counties(csv_path, selected_counties)
    print("CSV file has been updated with random county names.")
except ValueError as e:
    print(e)
