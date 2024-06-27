import os
import shutil

def copy_directories_to_Batch_dir(target_dir, directory_paths_array):
    """
    Copies directories specified in directory_paths to the target directory.

    Parameters:
    - target_dir (str): Path to the target directory where directories will be copied.
    - directory_paths (list): List of paths to the directories that need to be copied.

    Returns:
    - None
    """
    for dir_path in directory_paths_array:
        if os.path.exists(dir_path) and os.path.isdir(dir_path):
            dir_name = os.path.basename(dir_path)
            target_path = os.path.join(target_dir, dir_name)

            # Check if the directory already exists in the target location
            # if os.path.exists(target_path):
            #     print(f"Directory '{dir_name}' already exists in the target directory.")
        
            try:
                shutil.copytree(dir_path, target_path)
                print(f"Directory '{dir_name}' successfully copied to '{target_dir}'.")
            except Exception as e:
                print(f"Failed to copy directory '{dir_name}': {str(e)}")
        else:
            print(f"Directory '{dir_path}' does not exist or is not a valid directory.")

# Example usage:
if __name__ == "__main__":
    target_directory = "C:/Users/EIOT/Desktop/Target"
    directories_to_copy = join_paths("C:/Users/EIOT/Desktop/Unziped_dir",["105325641","500261503"])

    copy_directories_to_Batch_dir(target_directory, directories_to_copy)
