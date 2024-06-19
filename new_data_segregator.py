import os
import shutil

# Original base directory where all images and XML files are stored
base_dir = 'bug bites.v6i.voc'

# New base directory to store the organized files
new_base_dir = 'new data formatted'

# Define the subdirectories
sub_dirs = ['test', 'train', 'valid']

# Define simplified roots for category names to handle variations
categories = {
    'bedbug': ['bedbug', 'bedbugs', "bed_bug", "bed_bugs", "bed-bug", "bed-bugs"],
    'tick': ['tick', "ticks"],
    'mosquito': ['mosquitoes', 'moquitos', "mosquito"],
    'spider': ['spider', 'spders'],
    'flea': ['flea', "fleas"],
    'ant': ['ant', "ants"],
    'chigger': ['chigger', "chiggers"],
    # "bee" : ["bee"],
    'other': []  # 'other' will be a fallback
}

# Create subfolders in each category directory if they do not exist
def setup_directories(new_base, subs, cats):
    if not os.path.exists(new_base):
        os.makedirs(new_base)
    for sub in subs:
        sub_dir_path = os.path.join(new_base, sub)
        if not os.path.exists(sub_dir_path):
            os.makedirs(sub_dir_path)
        for cat in cats:
            dir_path = os.path.join(sub_dir_path, cat)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

setup_directories(new_base_dir, sub_dirs, categories.keys())

# Function to determine the correct folder based on simplified category matching
def get_target_folder(filename):
    filename = filename.lower()
    for category, variants in categories.items():
        if any(variant in filename for variant in variants):
            return category
    return 'other'

# Move files to their respective folders under each subdirectory in the new base directory
for sub_dir in sub_dirs:
    source_dir = os.path.join(base_dir, sub_dir)
    for filename in os.listdir(source_dir):
        # Removing specific format check to include all file types
        source_file = os.path.join(source_dir, filename)
        category = get_target_folder(filename)
        target_dir = os.path.join(new_base_dir, sub_dir, category)
        target_file = os.path.join(target_dir, filename)
        shutil.copy(source_file, target_file)  # Use copy to preserve original files

print("Files have been organized across test, train, and valid folders into the new formatted structure.")
