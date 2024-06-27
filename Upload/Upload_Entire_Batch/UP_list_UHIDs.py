import os

def list_subdirectories(parent_directory):
    subdirectories = []
    # Iterate over all entries (files and directories) in the parent_directory
    for entry in os.listdir(parent_directory):
        # Create the full path to the entry
        entry_path = os.path.join(parent_directory, entry)
        # Check if the entry is a directory and not a file
        if os.path.isdir(entry_path):
            subdirectories.append(entry)
    return subdirectories


if __name__=="__main__":
    print(list_subdirectories("C:/Users/EIOT/Desktop/Unziped_dir"))
