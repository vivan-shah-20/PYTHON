import os

# Specify the path to the directory
directory_path = "/New folder"

# List and print the contents of the directory
try:
    contents = os.listdir(directory_path)
    print("Contents of directory:", directory_path)
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory {directory_path} does not exist.")
except PermissionError:
    print(f"Permission denied to access the directory {directory_path}.")
