import requests
import os

def download_study_zip(study_id, download_directory):
    """
    Download a ZIP archive of a medical study from an Orthanc server.

    Parameters:
    - orthanc_url (str): Base URL of the Orthanc server.
    - study_id (str): ID of the study to download.
    - download_directory (str): Directory where the study ZIP file will be saved.

    Returns:
    - bool: True if download was successful, False otherwise.
    """

    # By default
    orthanc_url="http://localhost:8042"
    try:
        # Construct the URL for downloading the study ZIP archive
        print(study_id)
        study_zip_url = f"{orthanc_url}/studies/{study_id}/archive"
        
        # Send a GET request to the URL
        response = requests.get(study_zip_url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Save the study ZIP file to the download directory
            study_file_path = os.path.join(download_directory, f"{study_id}.zip")
            study_file_path=study_file_path.replace('\\','/')
            print(study_file_path)
            with open(study_file_path, 'wb') as study_file:
                study_file.write(response.content)
            return True
        else:
            # print(f"Failed to download study {study_id}. Status code: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return False

# Example usage:
if __name__ == "__main__":
    download_directory = "C:/Users/EIOT/Desktop/sample"  # Replace with your desired download directory
    study_id = "fc357979-e1b04273-e83fd9fe-db997ff0-8b9ca1fa"  # Replace with the actual study ID

    download_study_zip(study_id, download_directory)
