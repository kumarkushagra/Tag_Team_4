import os
import zipfile

def Extract_Delete_all_zips(directory):
    """
    Extracts all ZIP files in the specified directory and deletes the original ZIP files.
    
    Args:
    - directory (str): Path to the directory containing ZIP files.
    
    Returns:
    - None
    """
    # Ensure the directory path ends with a slash for joining correctly
    if not directory.endswith('/'):
        directory += '/'
    
    # Get a list of all files in the directory
    files = os.listdir(directory)
    
    # Iterate through all files
    for file in files:
        if file.endswith('.zip'):
            # Construct the full file path
            file_path = os.path.join(directory, file)
            
            # Extract the contents of the ZIP file
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(directory)
            
            # Delete the original ZIP file after extraction
            os.remove(file_path)
            print(f"Extracted and deleted: {file_path}")

if __name__=="__main__":
    download_directory="C:/Users/EIOT/Desktop/sample"
    Extract_Delete_all_zips(download_directory)  # Replace with your directory path