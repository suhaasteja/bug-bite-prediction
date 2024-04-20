import pandas as pd
import requests

# Load the CSV file
data = pd.read_csv('/Users/mac/Desktop/bug-bite-prediction/geo/observations-mosquitos.csv')

# Check if the necessary columns are present
if 'latitude' not in data.columns or 'longitude' not in data.columns:
    raise ValueError("CSV file does not contain 'latitude' or 'longitude' columns")

# Extract the latitude and longitude columns as a list of tuples
lat_longs = list(zip(data['latitude'], data['longitude']))

# API base URL
base_url = "https://geo.fcc.gov/api/census/area"

# List to hold data
results = []

# Iterate over each latitude and longitude pair
for lat, lon in lat_longs:
    params = {
        'lat': lat,
        'lon': lon,
        'censusYear': 2020,
        'format': 'json'
    }

    # Make the request to the API
    response = requests.get(base_url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        result = response.json()
        if result['results']:
            county_name = result['results'][0]['county_name']
            results.append({'latitude': lat, 'longitude': lon, 'county_name': county_name})
        else:
            print(f"No results found for ({lat}, {lon})")
    else:
        print(f"Failed to fetch data for ({lat}, {lon}): {response.status_code}")

# Create a DataFrame from the results
df = pd.DataFrame(results)

# Save the DataFrame to a CSV file
df.to_csv('/Users/mac/Desktop/bug-bite-prediction/geo/county_names_mosquitos.csv', index=False)

print("CSV file has been created.")
