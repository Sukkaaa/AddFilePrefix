import os

def add_prefix_to_files(directory_path, prefix):
    # List all files in the directory
    files = os.listdir(directory_path)

    # Iterate through each file
    for file in files:
        # Check if the item is a file (not a directory)
        if os.path.isfile(os.path.join(directory_path, file)):
            # Construct the new filename with the prefix
            new_filename = prefix + file
            # Rename the file with the new filename
            os.rename(os.path.join(directory_path, file), os.path.join(directory_path, new_filename))
            print(f"Renamed {file} to {new_filename}")

# Directory containing the files
directory_path = "/User/Desktop/directory"
# Prefix to add to the filenames
prefix = "sukka_"

# Call the function to add prefix to files
add_prefix_to_files(directory_path, prefix)
