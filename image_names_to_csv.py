import pandas as pd
import os

# Path to the directory containing images
images_folder_path = 'images/training/ticks'

# Path to your CSV file
csv_file_path = 'images/training/ticks/image_names_ticks.csv'

# Function to check if the file ends with png, jpeg, or jpg
def is_image_file(filename):
    return filename.lower().endswith(('.png', '.jpeg', '.jpg'))

# List all image filenames in the specified directory that match the criteria
image_files = [f for f in os.listdir(images_folder_path) if os.path.isfile(os.path.join(images_folder_path, f)) and is_image_file(f)]

# Check if the CSV file exists and read it if it does
if os.path.exists(csv_file_path):
    df_existing = pd.read_csv(csv_file_path)
    existing_images = set(df_existing['image_name'].dropna())
else:
    df_existing = pd.DataFrame(columns=['image_name'])
    existing_images = set()

# Filter out images that are already in the CSV
new_images = [image for image in image_files if image not in existing_images]

# Create a DataFrame for the new images
df_new = pd.DataFrame(new_images, columns=['image_name'])

# Append these new images to the existing dataframe if there are any
if not df_new.empty:
    df_updated = pd.concat([df_existing, df_new], ignore_index=True)
    # Save the updated DataFrame back to CSV
    df_updated.to_csv(csv_file_path, index=False)
    print(f"Added {len(new_images)} new image(s) to the CSV file.")
else:
    print("No new images to add. CSV file is up-to-date.")
