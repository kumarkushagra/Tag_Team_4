import os

def join_paths(parent_dir, subdirs_array):
    """
    Create an array of full paths by joining parent directory
    with each item in the subdirectories array.
    
    Args:
    - parent_dir (str): Parent directory path.
    - subdirs_array (list): List of subdirectory names.
    
    Returns:
    - list: List of full paths formed by joining parent_dir with each subdirectory.
    """
    full_paths = []
    for subdir in subdirs_array:
        full_path = os.path.join(parent_dir, subdir)
        full_path = full_path.replace("\\", "/")  # Replace backslashes with forward slashes
        full_paths.append(full_path)
    return full_paths

# Example usage:
if __name__=="__main__":
    parent_dir = "C:/Users/EIOT/Desktop/Unziped_dir"
    # subdirs_array = os.listdir('C:/Users/EIOT/Desktop/Unziped_dir')  # Replace with actual path to subdirectories
    joined_paths = join_paths(parent_dir, subdirs_array)
    print(joined_paths)
