import os

# Path to the folder
folder_path = "Data Analysis"

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    old_path = os.path.join(folder_path, filename)
    
    # Skip directories, only rename files
    if os.path.isfile(old_path):
        # Convert to lowercase and replace spaces with underscores
        new_filename = filename.lower().replace(" ", "_")
        new_path = os.path.join(folder_path, new_filename)
        
        # Rename the file
        os.rename(old_path, new_path)
        print(f'Renamed: {filename} -> {new_filename}')
