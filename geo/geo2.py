import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import time

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

# Initialize the geolocator
geolocator = Nominatim(user_agent="geoapiExercises")

# Load the CSV file
data = pd.read_csv('/Users/mac/Desktop/bug-bite-prediction/geo/observations-bedbug.csv')

# Check if the necessary columns are present
if 'latitude' not in data.columns or 'longitude' not in data.columns:
    raise ValueError("CSV file does not contain 'latitude' or 'longitude' columns")

# Fetch counties for each latitude and longitude
data['county'] = data.apply(lambda row: get_county(row['latitude'], row['longitude']), axis=1)

# Save the results to a new CSV file
data.to_csv('/mnt/data/observations_with_counties.csv', index=False)
