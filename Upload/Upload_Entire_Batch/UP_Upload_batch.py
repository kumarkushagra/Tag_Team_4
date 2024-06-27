# Provide Batch_Dir_path, anonymize_flag 
# generate a new_CSV (Master.csv) in Data dir, append new uploads from it
# Upload all Studies 
# Anonymize
# Delete orignal Study only
# Update User_CSV


import requests
from ..list_UHIDs import list_subdirectories
from ..generate_series_path import generate_all_series_path
from ..update_master_csv import update_csv
from ..upload_each_series import upload_dicom_files
from ..anonymize_given_study import anonymize_study
from ..append_to_mapping_csv import append_to_csv
from ..delete_study import delete_studies
from ..rename_studyID import rename_patient
from ..new_study_from_array import find_new_element

def Upload_Batch(batch_dir_path, anonymize_flag, User_CSV_path,batch_no):
    
    # By default
    ORTHANC_URL = "http://localhost:8042"

    # generate list containing all the UHIDs  
    uhid_array=list_subdirectories(batch_dir_path)
    
    # Iterate over each UHID
    for uhid in uhid_array:
        # Record all studies present before uploading
        old_studies = requests.get(f"{ORTHANC_URL}/studies").json()
        # print(old_studies)

        # Store full path of all DCM instances in an array
        series_array = generate_all_series_path(batch_dir_path, uhid)

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

        old_studies = requests.get(f"{ORTHANC_URL}/studies").json()
        # Anonymize new_study_id if anonymize flag is true
        # print(str(uploaded_studyID[0]))

        if anonymize_flag==True:
            anonymize_result = anonymize_study(ORTHANC_URL, str(uploaded_studyID[0]))
            print(anonymize_result)
        anonymized_studies = requests.get(f"{ORTHANC_URL}/studies").json()
        # Delete Orignal_study
        delete_studies(uploaded_studyID)
        
        # find studyID of the anonymized function
        anonymized_studyID = find_new_element(old_studies,anonymized_studies)

        # New name for anonymized function
        new_name = "Import Name from Master CSV"


        # Renaming DONE HERE DELETE is also handeled by this function        
        final_study_id=rename_patient(anonymized_studyID[0], new_name)

        append_to_csv(uhid, str(final_study_id),batch_no)

        # Update the Master CSV
        # print(User_CSV_path)
        # change value to "uploaded" == 1 
        update_csv(User_CSV_path,  uhid, 1)

if __name__=="__main__":
    batch_Dir_path="C:/Users/EIOT/Desktop/Unziped_dir"
    anon_flag=True
    User_CSV_path="C:/Users/EIOT/Desktop/Final.csv"
    batch_name="Batch1"
    Upload_Batch(batch_Dir_path, anon_flag, User_CSV_path,batch_name)