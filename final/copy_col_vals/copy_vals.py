import pandas as pd
import os

# Define pairs of source and target files assuming they are in the same directory
file_pairs = [
    ("bug_bites_data - Spider (training)_reduced.csv", "bug_bites_data - Spider (training).csv"),
    ("bug_bites_data - ants (training)(1)_reduced.csv", "bug_bites_data - ants (training)(1).csv"),
    ("bug_bites_data - begbugs (training)_reduced.csv", "bug_bites_data - begbugs (training).csv"),
    ("bug_bites_data - chiggers (training)_reduced.csv", "bug_bites_data - chiggers (training).csv"),
    ("bug_bites_data - fleas (training)_reduced.csv", "bug_bites_data - fleas (training).csv"),
    ("bug_bites_data - mosquitos (training)_reduced.csv", "bug_bites_data - mosquitos (training).csv"),
    ("bug_bites_data - ticks (training)_reduced.csv", "bug_bites_data - ticks (training).csv"),
    # Note: There is no corresponding source file for 'no_bites' in your list
]

# Columns to replace (example, adjust as needed)
columns_to_replace = ['latitude', 'longitude', 'county_name']  # Replace these with actual column names that need to be updated

# Create a new directory for the output files
output_dir = "updated_csvs"
os.makedirs(output_dir, exist_ok=True)

# Process each pair of files
for source_file, target_file in file_pairs:
    # Load the data from both files
    source_df = pd.read_csv(source_file)
    target_df = pd.read_csv(target_file)

    # Replace the selected column values from the source to the target
    for column in columns_to_replace:
        if column in source_df.columns and column in target_df.columns:
            target_df[column] = source_df[column]
        else:
            print(f"Column {column} not found in files {source_file} or {target_file}")

    # Save the updated dataframe to a new CSV file in the created directory
    new_file_name = os.path.join(output_dir, os.path.basename(target_file))
    target_df.to_csv(new_file_name, index=False)

    print(f"Updated {target_file} saved as {new_file_name}")

print("All files processed and saved in 'updated_csvs' folder.")
