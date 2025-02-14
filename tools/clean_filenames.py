import os
import re

# Define the directory containing the files
directory = "images/temp/"

# Function to clean file names
def clean_filename(filename):
    # Replace spaces, special characters, and non-alphanumeric characters with underscores
    cleaned_name = re.sub(r'[^a-zA-Z0-9_.-]', '_', filename)
    return cleaned_name

# Loop through files in the directory
for filename in os.listdir(directory):
    # Get the full path of the file
    full_path = os.path.join(directory, filename)
    
    # Skip directories (if any)
    if os.path.isfile(full_path):
        # Clean the file name
        new_name = clean_filename(filename)
        
        # Rename the file
        new_full_path = os.path.join(directory, new_name)
        os.rename(full_path, new_full_path)
        print(f"Renamed: {filename} -> {new_name}")