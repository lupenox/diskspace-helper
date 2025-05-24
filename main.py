# main.py

import shutil
import os

def get_disk_usage(path="/"):
    """
    Gets the disk usage of the specified path if its a file
    """
    total, used, free = shutil.disk_usage(path)
    print(f"Total: {total // (2**30)} GB") #Convert to GB
    print(f"Used: {used // (2**30)} GB")
    print(f"Free: {free // (2**30)} GB")

def get_file_size(file_path):
    if os.path.isfile(file_path):
        try:
            size = os.path.getsize(file_path)
            return size // (2**20) # Convert to MB
        except (FileNotFoundError, PermissionError):
            print(f"Error: File not found or permissioin denied for {file_path}")
            return None  
    return None
     
if __name__ == "__main__":
    get_disk_usage()
    path = input("Enter file path to check size: ")
    file_size = get_file_size(path)

    if file_size is not None:
        print(f"File size: {file_size} MB")
        print(f"File path: {path}")
    else:
        print("File size could not be determined")