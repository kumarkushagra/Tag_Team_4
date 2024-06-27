import os
import shutil


def delete_except_zips(directory):
    """
    Deletes everything inside the specified directory except for .zip files.
    
    Args:
    - directory (str): Path to the directory to clean up.
    
    Returns:
    - None
    """
    # Ensure the directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")

    # Iterate through all files and subdirectories in the directory
    for root, dirs, files in os.walk(directory, topdown=False):
        # Delete subdirectories
        for name in dirs:
            shutil.rmtree(os.path.join(root, name))
        
        # Delete files except for .zip files
        for name in files:
            if not name.endswith('.zip'):
                os.remove(os.path.join(root, name))


if __name__=="__main__":
    directory= "C:/Users/EIOT/Desktop/sample"  # Replace with your desired download directory
    delete_except_zips(directory)
