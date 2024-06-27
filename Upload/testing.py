import os
import zipfile

def unzip_and_upload_to(zip_file_path, Orthanc_url, userID, password):
    # Get the directory of the ZIP file
    zip_dir = os.path.dirname(zip_file_path)
    
    # Extracting the ZIP file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(zip_dir)
    
    # Assuming the ZIP file contains only one directory, return its path
    extracted_dir = os.path.splitext(zip_file_path)[0]  # Remove .zip extension
    
    # Start you modifications from here
    upload(Orthanc_url, userID, password, extracted_dir)


zip_file_path="D:/PROJECT/Tag_Team_1/ZIP_FILES/26_06_2024/26_06_2024.zip"
unzip_file(zip_file_path)


# def find_new_element(old_studies, new_studies):
#     # Convert studies to a set for faster lookup
#     # studies_set = set(old_studies)
    
#     # Find elements in new_studies that are not in studies
#     new_elements = [study for study in new_studies if study not in old_studies]
    
#     return new_elements

# def return_uhid_array(csv_file_path: str, num_uhid: int, column_name1: str, value1:int, column_name2: str, value2:int, id_column_name: str):
#     """
#     Reads a CSV file and returns an array of specified 'id_column_name' values where two specified columns match given values.
    
#     Parameters:
#     csv_file_path (str): The path to the CSV file.
#     num_uhid (int): The number of 'id_column_name' values to return.
#     column_name1 (str): The first column to check for the value.
#     value1: The value to check for in the first specified column.
#     column_name2 (str): The second column to check for the value.
#     value2: The value to check for in the second specified column.
#     id_column_name (str): The name of the ID column whose values are to be returned.
    
#     Returns:
#     list: A list of values from the 'id_column_name' column.
#     """
#     # Read the CSV file into a DataFrame
#     df = pd.read_csv(csv_file_path)
    
#     # Check if the specified columns exist in the DataFrame
#     if column_name1 not in df.columns:
#         raise KeyError(f"Column '{column_name1}' does not exist in the CSV file.")
#     if column_name2 not in df.columns:
#         raise KeyError(f"Column '{column_name2}' does not exist in the CSV file.")
#     if id_column_name not in df.columns:
#         raise KeyError(f"Column '{id_column_name}' does not exist in the CSV file.")
    
#     # Filter the DataFrame where the specified columns match the given values
#     filtered_df = df[(df[column_name1] == value1) & (df[column_name2] == value2)]
    
#     # Select the desired number of values from the specified ID column
#     idnumbers = filtered_df[id_column_name].head(num_uhid).tolist()
    
#     return idnumbers


# def join_paths(parent_dir, subdirs_array):
#     """
#     Create an array of full paths by joining parent directory
#     with each item in the subdirectories array.
    
#     Args:
#     - parent_dir (str): Parent directory path.
#     - subdirs_array (list): List of subdirectory names.
    
#     Returns:
#     - list: List of full paths formed by joining parent_dir with each subdirectory.
#     """
#     full_paths = []
#     for subdir in subdirs_array:
#         full_path = os.path.join(parent_dir, subdir)
#         full_path = full_path.replace("\\", "/")  # Replace backslashes with forward slashes
#         full_paths.append(full_path)
#     return full_paths


# def create_subdirectory(parent_path, subdirectory_name):
#     """
#     Creates a new subdirectory inside a specified parent directory.

#     Args:
#     - parent_path (str): Path of the parent directory where the new subdirectory will be created.
#     - subdirectory_name (str): Name of the new subdirectory to be created.

#     Returns:
#     - str: Full path of the newly created subdirectory if successful, None otherwise.
#     """
#     # Combine parent path and subdirectory name to get full path of the new directory
#     new_directory_path = os.path.join(parent_path, subdirectory_name)
#     new_directory_path.replace("\\", "/")

#     try:
#         # Create the directory if it does not exist
#         os.makedirs(new_directory_path, exist_ok=True)
#         print(f"Directory '{subdirectory_name}' created successfully.")
#         return new_directory_path
#     except OSError as e:
#         print(f"Error creating directory '{subdirectory_name}' in {parent_path}: {e}")
#         return None


# def latest_batch_number():
#     csv_file_path = 'Database/mapping.csv'

#     try:
#         # Open the CSV file
#         with open(csv_file_path, mode='r') as file:
#             reader = csv.DictReader(file)
            
#             # Initialize variables to track the latest batch and time
#             latest_time = datetime.datetime.min
#             latest_batch = None
            
#             # Flag to check if there are any data rows
#             has_data = False
            
#             for row in reader:
#                 has_data = True
#                 # Combine date and time into a single datetime object
#                 timestamp = f"{row['date']} {row['Time']}"
#                 current_time = latest_time.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
                
#                 # Compare current time with the latest time
#                 if current_time > latest_time:
#                     latest_time = current_time
#                     latest_batch = row['batch_no']
#                     latest_normal_name= row['name_of_StudyID']
            
#             # If there were no data rows, return 0
#             if not has_data:
#                 return 0
            
#             # Extract the integer part of the batch number
#             latest_batch_number = int(''.join(filter(str.isdigit, latest_batch)))
#             latest_normal_number = int(''.join(filter(str.isdigit, latest_normal_name)))
#             return latest_batch_number,latest_normal_number
    
#     except FileNotFoundError:
#         # Return 0 if the file is not found
#         return 0



# def copy_directories_to_Batch_dir(target_dir, directory_paths_array):
#     """
#     Copies directories specified in directory_paths to the target directory.

#     Parameters:
#     - target_dir (str): Path to the target directory where directories will be copied.
#     - directory_paths (list): List of paths to the directories that need to be copied.

#     Returns:
#     - None
#     """
#     for dir_path in directory_paths_array:
#         if os.path.exists(dir_path) and os.path.isdir(dir_path):
#             dir_name = os.path.basename(dir_path)
#             target_path = os.path.join(target_dir, dir_name)

#             # Check if the directory already exists in the target location
#             # if os.path.exists(target_path):
#             #     print(f"Directory '{dir_name}' already exists in the target directory.")
        
#             try:
#                 shutil.copytree(dir_path, target_path)
#                 print(f"Directory '{dir_name}' successfully copied to '{target_dir}'.")
#             except Exception as e:
#                 print(f"Failed to copy directory '{dir_name}': {str(e)}")
#         else:
#             print(f"Directory '{dir_path}' does not exist or is not a valid directory.")


# def Upload_Batch(batch_dir_path, anonymize_flag, User_CSV_path,batch_no,latest_normal_number):
    
#     # By default
#     ORTHANC_URL = "http://localhost:8042"

#     # generate list containing all the UHIDs  
#     uhid_array=list_subdirectories(batch_dir_path)

    
#     # Iterate over each UHID
#     for uhid in uhid_array:
#         # Record all studies present before uploading
#         old_studies = requests.get(f"{ORTHANC_URL}/studies").json()
#         # print(old_studies)

#         # Store full path of all DCM instances in an array
#         series_array = generate_all_series_path(batch_dir_path, uhid)

#         # iterate over each series
#         for series in series_array:
#             # will opload each series for a given UHID
#             upload_success=upload_dicom_files(ORTHANC_URL,series)
#             if not upload_success:
#                 print(f"Failed to upload series for UHID: {uhid}. Skipping to next UHID.")
#                 #msg=f"Failed to upload series for UHID: {uhid}. Skipping to next UHID."
#                 #logs(name,msg)
#                 continue
        
#         # Record all Studies after uploading

#         new_studies = requests.get(f"{ORTHANC_URL}/studies").json()
#         # print(new_studies)

#         # Find the study_ID of new UHID i.e. just uploaded
#         uploaded_studyID = find_new_element(old_studies,new_studies)

#         old_studies = requests.get(f"{ORTHANC_URL}/studies").json()
#         # Anonymize new_study_id if anonymize flag is true
#         # print(str(uploaded_studyID[0]))

#         if anonymize_flag==True:
#             anonymize_result = anonymize_study(ORTHANC_URL, str(uploaded_studyID[0]))
#             print(anonymize_result)
#             anonymized_studies = requests.get(f"{ORTHANC_URL}/studies").json()
#             # Delete Orignal_study
#             delete_studies(uploaded_studyID)
        
#             # find studyID of the anonymized function
        
#             uploaded_studyID = find_new_element(old_studies,anonymized_studies)

#             # New name for anonymized function
#             latest_normal_number+=1
#             new_name = "Normal_" + str(latest_normal_number)

#             # Renaming DONE HERE DELETE is also handeled by this function        
#             final_study_id=rename_patient(uploaded_studyID[0], new_name)
#         else:
#             final_study_id =uploaded_studyID[0]

#         append_to_csv(uhid, str(final_study_id),batch_no,new_name)

#         # Update the Master CSV
#         # print(User_CSV_path)
#         # change value to "uploaded" == 1 
#         update_csv(User_CSV_path,  uhid, 1)


# def generate_all_series_path(batch_dir_path, uhid):
#     """
#     Returns a list of directories containing DICOM series for a given UHID.
    
#     Parameters:
#     unzip_dir_path (str): The path to the base directory containing UHID subdirectories.
#     uhid (str): The UHID for which to return series directories.
    
#     Returns:
#     list: A list of paths to DICOM series directories.
#     """
#     series_dirs = []
#     uhid_path = os.path.join(batch_dir_path, uhid)
#     uhid_path = uhid_path.replace("\\", "/")

#     # Check if the UHID directory exists
#     if os.path.isdir(uhid_path):
#         # Iterate over date directories
#         for date_dir in os.listdir(uhid_path):
#             date_path = os.path.join(uhid_path, date_dir)
#             date_path = date_path.replace("\\", "/")

#             if os.path.isdir(date_path):
#                 # Iterate over series directories
#                 for series_dir in os.listdir(date_path):
#                     series_path = os.path.join(date_path, series_dir)
#                     series_path = series_path.replace("\\", "/")

#                     if os.path.isdir(series_path):
#                         series_dirs.append(series_path)
    
#     return series_dirs


# def update_csv(file_path,  uhid_value,  change_value):
#     """
#     Updates a CSV file by changing a specified column value for a given UHID.
    
#     Parameters:
#     file_path (str): The path to the CSV file.
#     uhid_column (str): The name of the column containing UHID values.
#     uhid_value (str): The UHID value to find in the CSV file.
#     change_column (str): The name of the column to update.
#     change_value: The new value to set in the change column.
    
#     Returns:
#     str: A confirmation message indicating the update was successful.
#     """
#     # Load the CSV file into a DataFrame
#     df = pd.read_csv(file_path)
    
#     # Find the index of the row with the specified UHID value
#     row_index = df.index[df['Patient ID (UHID)'] == uhid_value].tolist()
    
#     if not row_index:
#         raise ValueError(f"UHID value {uhid_value} not found in column {uhid_column}.")
    
#     # Update the specified column in the located row
#     df.at[row_index[0], 'Uploaded'] = change_value
    
#     # Save the updated DataFrame back to the CSV file
#     df.to_csv(file_path, index=False)

#     return f"Updated {'Uploaded'} for UHID {uhid_value} to {change_value}."


# def upload_dicom_files(orthanc_url, dir_path: str):
#     """
#     Uploads DICOM files to Orthanc.
    
#     Parameters:
#     orthanc_url (str): The URL of the Orthanc server.
#     dir_path (str): The path to the DICOM series directory.
    
#     Returns:
#     dict: A dictionary with a status message.
#     """
#     # Check if the directory exists
#     if not os.path.isdir(dir_path):
#         raise Exception("Directory does not exist")

#     # Iterate over all files in the specified directory
#     for file_name in os.listdir(dir_path):
#         # Check if the file has a .dcm extension
#         if file_name.lower().endswith('.dcm'):
#             # Path to the DICOM file
#             dicom_file_path = os.path.join(dir_path, file_name)
#             dicom_file_path = dicom_file_path.replace("\\", "/")



#             # UPLOADING BEGINS

#             # Read the DICOM file in binary mode
#             with open(dicom_file_path, 'rb') as f:
#                 dicom_data = f.read()

#             # Upload the DICOM file
#             orthanc_url_with_instances = orthanc_url.rstrip('/') + '/instances'
#             response = requests.post(orthanc_url_with_instances, data=dicom_data, headers={'Content-Type': 'application/dicom'})



#             # Check for Exceptions
#             if response.status_code == 200:
#                 print(f'DICOM file {file_name} uploaded successfully')
#                 #msg=f'DICOM file {file_name} uploaded successfully'
#                 #logs(name,msg)
#             else:
#                 print(f'Failed to upload DICOM file {file_name}. Status code: {response.status_code}')
#                 #msg=f'Failed to upload DICOM file {file_name}. Status code: {response.status_code}'
#                 #logs(name,msg)
#                 print('Response content:', response.content.decode('utf-8'))
#                 #msg='Response content:', response.content.decode('utf-8')
#                 #logs(name,msg)
#     return {"detail": "DICOM files upload process completed"}



# def anonymize_study(orthanc_url, study_id):
#     """
#     Anonymizes a specific study in Orthanc.
    
#     Parameters:
#     orthanc_url (str): The URL of the Orthanc server.
#     study_id (str): The ID of the study to be anonymized.
    
#     Returns:
#     str: Success or error message.
#     """
#     anonymize_response = requests.post(
#         f"{orthanc_url}/tools/bulk-anonymize",
#         json={"Resources": [study_id]}
#     )
    
#     if anonymize_response.status_code == 200:
#         return f"Anonymized study {study_id} successfully"
#     else:
#         return f"Failed to anonymize study {study_id}: {anonymize_response.json()}"



# def append_to_csv(uhid, new_study_id,batch_no,study_name):
#     current_datetime = datetime.datetime.now()

#     # Store date and time in separate variables
#     date = current_datetime.date()
#     time = current_datetime.time()
#     # by default, mapping.csv will be stored in Database dir
#     user_csv_path = 'Database/mapping.csv'
#     # Check if the CSV file exists
#     csv_exists = os.path.exists(user_csv_path)
    
#     # Define headers for the CSV file
#     headers = ['uhid','date','Time', 'new_study_id','batch_no','name_of_StudyID']
    
#     # Open the CSV file in append mode
#     with open('Database/mapping.csv', 'a', newline='') as csvfile:
#         writer = csv.writer(csvfile)
        
#         # Write headers only if the file was just created
#         if not csv_exists:
#             writer.writerow(headers)
        
#         # Write the new data
#         writer.writerow([uhid,date,time, new_study_id,batch_no,study_name])


# def delete_studies(study_ids:list):
#     '''
#     Input: List StudyID ENSURE THAT STUDYiD are present in this array
#     Output: Delete all studies with the given StudyID
#     '''
#     # Endpoint to retrieve all studies

#     # by default
#     ORTHANC_URL="http://localhost:8042"
    
#     studies_url = f'{ORTHANC_URL}/studies'
    
#     try:
#         # print(type(study_ids))
#         # Delete each study
#         for study_id in study_ids:
#             study_delete_url = f'{ORTHANC_URL}/studies/{study_id}'
#             delete_response = requests.delete(study_delete_url)
#             delete_response.raise_for_status()
#             print(f'Successfully deleted study: {study_id}')
#           #  msg=f'Successfully deleted study: {study_id}'
#          #   logs(name,msg)
    
#     except requests.exceptions.RequestException as e:
#         print(f'An error occurred: {e}')
#         #msg=f'An error occurred: {e}'
#         #logs(name,msg)


# def rename_patient(study_id, new_name):
#     url = "http://localhost:8042"

#     studies = requests.get(f"{url}/studies").json()
#     def fetch_json(endpoint):
#         response = requests.get(f"{url}{endpoint}")
#         return response.json() if response.status_code == 200 else None

#     if (studies := fetch_json(f"/studies/{study_id}")):
#         patient_id = studies['ParentPatient']
#         print(f"Patient ID: {patient_id}")

#         update_url = f"{url}/patients/{patient_id}/modify"
#         payload = {
#             #'Keep' : [ 'SOPInstanceUID' ],
#             "Replace": {
#                 "PatientID" : patient_id,
#                 "PatientName": new_name
#             },
#             'Force':True
#         }

#         ols_studies = requests.get(f"{url}/studies").json()

#         # renameing 
#         response = requests.post(update_url, json=payload)

#         # get new studies
#         new_studies = requests.get(f"{url}/studies").json()

#         # Storing new (renamed) StudyID in a variable
#         renamed_studyID = find_new_element(ols_studies,new_studies)
        
#         # deleting previous study 
#         delete_studies([study_id])


#         if response.status_code == 200:
#             print(f"Patient name successfully updated to {new_name}")
#             return renamed_studyID

#         else:
#             print(f"Failed to update patient name. Status code: {response.status_code}")
#             return renamed_studyID

#     else:
#         print(f"No study found or error fetching data for study_id: {study_id}")
#         return renamed_studyID


# def list_subdirectories(parent_directory):
#     subdirectories = []
#     # Iterate over all entries (files and directories) in the parent_directory
#     for entry in os.listdir(parent_directory):
#         # Create the full path to the entry
#         entry_path = os.path.join(parent_directory, entry)
#         # Check if the entry is a directory and not a file
#         if os.path.isdir(entry_path):
#             subdirectories.append(entry)
#     return subdirectories
