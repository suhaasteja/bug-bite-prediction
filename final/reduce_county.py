import pandas as pd
import os

# Define the list of CSV files
csv_files = [
    "bug_bites_data - Spider (training).csv",
    "bug_bites_data - ants (training)(1).csv",
    "bug_bites_data - begbugs (training).csv",
    "bug_bites_data - chiggers (training).csv",
    "bug_bites_data - fleas (training).csv",
    "bug_bites_data - mosquitos (training).csv",
    "bug_bites_data - ticks (training).csv"
]

# Create a new directory for the output files
output_dir = "processed_data"
os.makedirs(output_dir, exist_ok=True)

# Process each file
for file_name in csv_files:
    # Load the data
    df = pd.read_csv(file_name)

    # Calculate frequency of each county
    county_freq = df['county_name'].value_counts(normalize=True)

    # Determine the number of samples to take from each county
    n_samples = 200
    samples_per_county = (county_freq * n_samples).round().astype(int)

    # Sample the data
    sampled_df = pd.DataFrame()
    for county, n in samples_per_county.items():
        sampled_rows = df[df['county_name'] == county].sample(min(len(df[df['county_name'] == county]), n), random_state=1)
        sampled_df = pd.concat([sampled_df, sampled_rows])

    # Save the sampled data to a new CSV file
    new_file_name = f"{output_dir}/{file_name.replace('.csv', '_reduced.csv')}"
    sampled_df.to_csv(new_file_name, index=False)

print("Data processing complete. Files saved in 'processed_data' folder.")
