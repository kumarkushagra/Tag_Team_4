import zipfile
import os 

from .UP_list_UHIDs import *
from .UP_generate_series_path import *
from .UP_upload_each_series import *
from .UP_new_study_from_array import *

def unzip_and_upload_to(zip_file_path, ORTHANC_URL="http://localhost:8042"):
    # Get the directory of the ZIP file
    zip_dir = os.path.dirname(zip_file_path)
    
    # Extracting the ZIP file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(zip_dir)
    
    # Assuming the ZIP file contains only one directory, return its path
    extracted_dir = zip_dir     


    """ UPLOAD FUNCTIONALITY BEGINS HERE"""

    # generate list containing all the UHIDs  
    uhid_array=list_subdirectories(extracted_dir)

    
    # Iterate over each UHID
    for uhid in uhid_array:
        # Record all studies present before uploading
        old_studies = requests.get(f"{ORTHANC_URL}/studies").json()
        # print(old_studies)

        # Store full path of all DCM instances in an array
        series_array = generate_all_series_path(extracted_dir, uhid)

        # iterate over each series
        for series in series_array:
            # will opload each series for a given UHID
            upload_success=upload_dicom_files(ORTHANC_URL,series)
            if not upload_success:
                print(f"Failed to upload series for UHID: {uhid}. Skipping to next UHID.")
                #msg=f"Failed to upload series for UHID: {uhid}. Skipping to next UHID."
                #logs(name,msg)
                continue
        

        # Record all Studies after uploading
        new_studies = requests.get(f"{ORTHANC_URL}/studies").json()
        # print(new_studies)

        # Find the study_ID of new UHID i.e. just uploaded
        uploaded_studyID = find_new_element(old_studies,new_studies)

        