# REMEMBER THAT ZIP_FILE_Path MUST BE EMPTY!!!
# Logic here first deletes all zip files from the directory,then starts DOWNLOADING
import requests
import os
import zipfile
import shutil

from .get_all_studies import get_all_studies
from .download_study_zip import download_study_zip
from .extract_delete_all_zip import Extract_Delete_all_zips
from .zip_dir import zip_directory
from .delete_all_except_zip import delete_except_zips


# def delete_except_zips(directory):
#     """
#     Deletes everything inside the specified directory except for .zip files.
    
#     Args:
#     - directory (str): Path to the directory to clean up.
    
#     Returns:
#     - None
#     """
#     # Ensure the directory exists
#     if not os.path.exists(directory):
#         raise FileNotFoundError(f"The directory '{directory}' does not exist.")

#     # Iterate through all files and subdirectories in the directory
#     for root, dirs, files in os.walk(directory, topdown=False):
#         # Delete subdirectories
#         for name in dirs:
#             shutil.rmtree(os.path.join(root, name))
        
#         # Delete files except for .zip files
#         for name in files:
#             if not name.endswith('.zip'):
#                 os.remove(os.path.join(root, name))


# def zip_directory(directory_path,Name_of_ZIP_File):
#     """
#     Compresses the folders inside a given directory into a ZIP file.

#     Args:
#     - directory_path (str): Path to the directory containing folders to be zipped.
#     - zip_path (str): Path to the output ZIP file.

#     Raises:
#     - FileNotFoundError: If the specified directory does not exist.
#     """

#     zip_path = os.path.join(directory_path, f"{Name_of_ZIP_File}.zip")

#     # Check if the directory exists
#     if not os.path.exists(directory_path):
#         raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

#     # Initialize the ZIP file object
#     with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
#         # Walk through all the items in the directory
#         for item in os.listdir(directory_path):
#             item_path = os.path.join(directory_path, item)
#             # Check if the item is a directory
#             if os.path.isdir(item_path):
#                 for root, dirs, files in os.walk(item_path):
#                     for file in files:
#                         # Construct the full local file path
#                         local_file = os.path.join(root, file)
#                         # Construct the archive path (relative to the directory)
#                         archive_name = os.path.relpath(local_file, directory_path)
#                         # Add file to ZIP
#                         zipf.write(local_file, archive_name)

#     return zip_path

# def Extract_Delete_all_zips(directory):
#     """
#     Extracts all ZIP files in the specified directory and deletes the original ZIP files.
    
#     Args:
#     - directory (str): Path to the directory containing ZIP files.
    
#     Returns:
#     - None
#     """
#     # Ensure the directory path ends with a slash for joining correctly
#     if not directory.endswith('/'):
#         directory += '/'
    
#     # Get a list of all files in the directory
#     files = os.listdir(directory)
    
#     # Iterate through all files
#     for file in files:
#         if file.endswith('.zip'):
#             # Construct the full file path
#             file_path = os.path.join(directory, file)
            
#             # Extract the contents of the ZIP file
#             with zipfile.ZipFile(file_path, 'r') as zip_ref:
#                 zip_ref.extractall(directory)
            
#             # Delete the original ZIP file after extraction
#             os.remove(file_path)
#             print(f"Extracted and deleted: {file_path}")

# def download_study_zip(study_id, download_directory):
#     """
#     Download a ZIP archive of a medical study from an Orthanc server.

#     Parameters:
#     - orthanc_url (str): Base URL of the Orthanc server.
#     - study_id (str): ID of the study to download.
#     - download_directory (str): Directory where the study ZIP file will be saved.

#     Returns:
#     - bool: True if download was successful, False otherwise.
#     """

#     # By default
#     orthanc_url="http://localhost:8042"
#     try:
#         # Construct the URL for downloading the study ZIP archive
#         print(study_id)
#         study_zip_url = f"{orthanc_url}/studies/{study_id}/archive"
        
#         # Send a GET request to the URL
#         response = requests.get(study_zip_url)
        
#         # Check if the request was successful (status code 200)
#         if response.status_code == 200:
#             # Save the study ZIP file to the download directory
#             study_file_path = os.path.join(download_directory, f"{study_id}.zip")
#             study_file_path=study_file_path.replace('\\','/')
#             print(study_file_path)
#             with open(study_file_path, 'wb') as study_file:
#                 study_file.write(response.content)
#             return True
#         else:
#             # print(f"Failed to download study {study_id}. Status code: {response.status_code}")
#             return False
#     except requests.exceptions.RequestException as e:
#         print(f"Request failed: {e}")
#         return False

# def get_all_studies(orthanc_url="http://localhost:8042"):
#     studies_url = f"{orthanc_url}/studies"
#     response = requests.get(studies_url)
#     if response.status_code != 200:
#         print("Failed to retrieve studies")
#         return
    
#     return response.json()
def download_studies(downalod_dir,Name_of_ZIP_File, studies = None):
    if studies == None:
        studies = get_all_studies()


    for study_id in studies:
        # Downloading .ziped studies
        download_study_zip(study_id,downalod_dir)
        Extract_Delete_all_zips(downalod_dir)
    zip_path = zip_directory(downalod_dir,Name_of_ZIP_File)
    delete_except_zips(downalod_dir)
    return zip_path




if __name__== "__main__":
    download_dir = "ZIP_FILES"  # Replace with your desired download directory
    # This is an array!!!!!!!!!!!!
    study_id = "fc357979-e1b04273-e83fd9fe-db997ff0-8b9ca1fa"  # Replace with the actual study ID 
    Name_of_ZIP_File="Zip file name"
    download_studies(download_dir,Name_of_ZIP_File)
