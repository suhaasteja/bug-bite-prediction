import os
import csv

def save_image_names_to_csv(directory, output_file='image_names_ticks.csv'):
    # List all files in the specified directory
    image_names = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    # Sort the list of image names
    image_names.sort()
    
    # Write the sorted list of image names to a CSV file
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        for name in image_names:
            writer.writerow([name])  # Each image name in its own row

# Specify the directory containing the images
directory_path = '/Users/mac/Desktop/bug-bite-prediction/images/training/ticks'

# Call the function with the directory path
save_image_names_to_csv(directory_path)
