import os

def create_subdirectory(parent_path, subdirectory_name):
    """
    Creates a new subdirectory inside a specified parent directory.

    Args:
    - parent_path (str): Path of the parent directory where the new subdirectory will be created.
    - subdirectory_name (str): Name of the new subdirectory to be created.

    Returns:
    - str: Full path of the newly created subdirectory if successful, None otherwise.
    """
    # Combine parent path and subdirectory name to get full path of the new directory
    new_directory_path = os.path.join(parent_path, subdirectory_name)
    new_directory_path.replace("\\", "/")

    try:
        # Create the directory if it does not exist
        os.makedirs(new_directory_path, exist_ok=True)
        print(f"Directory '{subdirectory_name}' created successfully.")
        return new_directory_path
    except OSError as e:
        print(f"Error creating directory '{subdirectory_name}' in {parent_path}: {e}")
        return None

# Example usage:
if __name__=="__main__":
    parent_directory = 'C:/Users/EIOT/Desktop/tar'
    new_directory_name = 'Batch'

    created_directory = create_subdirectory(parent_directory, new_directory_name)

    if created_directory:
        print(f"New directory created at: {created_directory}")
    else:
        print("Failed to create the directory.")
