# Import Module
import os
from os import path


# Get file content as an array
def print_file_array_from_folder(folder_path):
    files = []

    # Change the directory
    os.chdir(folder_path)

    # iterate through all files
    for file in os.listdir():
        print(file)
        # Check whether file is in json format or not
        if file.endswith(".json"):
            file_path = path.join(folder_path, file)

            with open(file_path, 'r') as f:
                print(f.read())


# Get file content as an array
def get_file_array_from_folder(folder_path):
    files = []

    # Change the directory
    os.chdir(folder_path)

    # iterate through all files
    for file in os.listdir():
        print(file)
        # Check whether file is in json format or not
        if file.endswith(".json"):
            file_path = path.join(folder_path, file)

            with open(file_path, 'r') as f:
                files.append(f.read())

    return files


def get_file_contents(folder_path, file_name):
    file_path = path.join(folder_path, file_name)
    with open(file_path, 'r') as f:
        return f.read()
