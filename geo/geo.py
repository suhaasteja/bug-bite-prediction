import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import time
import os

def get_county(lat, lon):
    try:
        location = geolocator.reverse((lat, lon), exactly_one=True)
        address = location.raw['address']
        county = address.get('county', 'Unknown')
        return county
    except (GeocoderTimedOut, GeocoderServiceError):
        time.sleep(1)  # Retry in case of timeout or service error
        return get_county(lat, lon)
    except Exception as e:
        print(f"Error fetching county for lat {lat} and lon {lon}: {e}")
        return 'Unknown'

def process_file(file_path):
    # Load the CSV data
    data = pd.read_csv(file_path)

    # Check if latitude and longitude columns exist
    if 'latitude' in data.columns and 'longitude' in data.columns:
        # Apply the function to fetch counties
        data['county'] = data.apply(lambda row: get_county(row['latitude'], row['longitude']), axis=1)
    else:
        raise ValueError(f"CSV file {file_path} does not contain 'latitude' or 'longitude' columns")

    # Analyze the most common counties
    top_counties = data['county'].value_counts().head(200)

    # Save the top counties to a new CSV file
    output_filename = os.path.splitext(os.path.basename(file_path))[0] + '_top_counties.csv'
    top_counties.to_csv(output_filename)
    print(f"Processed {file_path} - results saved to {output_filename}")

# Initialize the geolocator
geolocator = Nominatim(user_agent="geoapiExercises")

# Directory containing your CSV files
directory_path = '/Users/mac/Desktop/bug-bite-prediction/geo'

# Loop through each file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory_path, filename)
        process_file(file_path)
