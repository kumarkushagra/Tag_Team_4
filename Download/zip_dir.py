import os
import zipfile

def zip_directory(directory_path,Name_of_ZIP_File):
    """
    Compresses the folders inside a given directory into a ZIP file.

    Args:
    - directory_path (str): Path to the directory containing folders to be zipped.
    - zip_path (str): Path to the output ZIP file.

    Raises:
    - FileNotFoundError: If the specified directory does not exist.
    """

    zip_path = os.path.join(directory_path, f"{Name_of_ZIP_File}.zip")

    # Check if the directory exists
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

    # Initialize the ZIP file object
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Walk through all the items in the directory
        for item in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item)
            # Check if the item is a directory
            if os.path.isdir(item_path):
                for root, dirs, files in os.walk(item_path):
                    for file in files:
                        # Construct the full local file path
                        local_file = os.path.join(root, file)
                        # Construct the archive path (relative to the directory)
                        archive_name = os.path.relpath(local_file, directory_path)
                        # Add file to ZIP
                        zipf.write(local_file, archive_name)

    print(f"Folders in '{directory_path}' zipped successfully to '{zip_path}'.")


if __name__=="__main__":
    directory_path = "C:/Users/EIOT/Desktop/sample/"  # Replace with your desired download directory

    zip_path="/ZIP_FILES/"
    Name_of_ZIP_File="Zip_file_Name"
    
    zip_directory(directory_path,Name_of_ZIP_File)
