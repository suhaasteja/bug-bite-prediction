import os
import shutil

# Define the base directory where all images and XML files are stored
base_dir = 'bug bites.v6i.voc'

# Define the subdirectories
sub_dirs = ['test', 'train', 'valid']

# Define the target categories
categories = ['bedbugs', 'ticks', 'mosquitos', 'spiders', 'fleas', 'ants', 'chiggers', 'extras']

# Create subfolders in each category directory if they do not exist
def setup_directories(base, subs, cats):
    for sub in subs:
        for cat in cats:
            dir_path = os.path.join(base, sub, cat)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

setup_directories(base_dir, sub_dirs, categories)

# Function to determine the correct folder
def get_target_folder(filename):
    for category in categories[:-1]:  # Exclude 'extras' for explicit check
        if category in filename.lower():
            return category
    return 'extras'

# Move files to their respective folders under each subdirectory
for sub_dir in sub_dirs:
    source_dir = os.path.join(base_dir, sub_dir)
    for filename in os.listdir(source_dir):
        # Check for both JPG and XML files
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.xml'):
            source_file = os.path.join(source_dir, filename)
            category = get_target_folder(filename)
            target_dir = os.path.join(base_dir, sub_dir, category)
            shutil.move(source_file, os.path.join(target_dir, filename))

print("Files have been organized across test, train, and valid folders.")
