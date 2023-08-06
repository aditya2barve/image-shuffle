import os
import random
import shutil
import argparse

def shuffle_files(source_folder, dest_folder):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Get a list of all the files in the source folder
    files = os.listdir(source_folder)

    # Shuffle the list of files
    random.shuffle(files)

    # Copy each file to the destination folder with a randomized name
    for i, file in enumerate(files):
        # Get the file extension
        _, ext = os.path.splitext(file)

        # Generate a random name for the file
        new_name = str(i+1) + ext

        # Copy the file to the destination folder with the new name
        shutil.copy(os.path.join(source_folder, file), os.path.join(dest_folder, new_name))

if __name__ == '__main__':
    # Parse the command line arguments
    parser = argparse.ArgumentParser(description='Shuffle files in a folder and copy them to a new folder with randomized names')
    parser.add_argument('source_folder', help='The path to the source folder')
    parser.add_argument('dest_folder', help='The path to the destination folder')
    args = parser.parse_args()

    # Call the shuffle_files function with the command line arguments
    shuffle_files(args.source_folder, args.dest_folder)