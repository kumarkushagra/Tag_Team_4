import requests

def find_new_element(old_studies, new_studies):
    # Convert studies to a set for faster lookup
    # studies_set = set(old_studies)
    
    # Find elements in new_studies that are not in studies
    new_elements = [study for study in new_studies if study not in old_studies]
    
    return new_elements


def delete_studies(study_ids:list):
    '''
    Input: List StudyID ENSURE THAT STUDYiD are present in this array
    Output: Delete all studies with the given StudyID
    '''
    # Endpoint to retrieve all studies

    # by default
    ORTHANC_URL="http://localhost:8042"
    
    studies_url = f'{ORTHANC_URL}/studies'
    
    try:
        # print(type(study_ids))
        # Delete each study
        for study_id in study_ids:
            study_delete_url = f'{ORTHANC_URL}/studies/{study_id}'
            delete_response = requests.delete(study_delete_url)
            delete_response.raise_for_status()
            print(f'Successfully deleted study: {study_id}')
          #  msg=f'Successfully deleted study: {study_id}'
         #   logs(name,msg)
    
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
        #msg=f'An error occurred: {e}'
        #logs(name,msg)

def rename_patient(study_id, new_name):
    url = "http://localhost:8042"

    studies = requests.get(f"{url}/studies").json()
    def fetch_json(endpoint):
        response = requests.get(f"{url}{endpoint}")
        return response.json() if response.status_code == 200 else None

    if (studies := fetch_json(f"/studies/{study_id}")):
        patient_id = studies['ParentPatient']
        print(f"Patient ID: {patient_id}")

        update_url = f"{url}/patients/{patient_id}/modify"
        payload = {
            #'Keep' : [ 'SOPInstanceUID' ],
            "Replace": {
                "PatientID" : patient_id,
                "PatientName": new_name
            },
            'Force':True
        }

        ols_studies = requests.get(f"{url}/studies").json()

        # renameing 
        response = requests.post(update_url, json=payload)

        # get new studies
        new_studies = requests.get(f"{url}/studies").json()

        # Storing new (renamed) StudyID in a variable
        renamed_studyID = find_new_element(ols_studies,new_studies)
        
        # deleting previous study 
        delete_studies([study_id])


        if response.status_code == 200:
            print(f"Patient name successfully updated to {new_name}")
            return renamed_studyID

        else:
            print(f"Failed to update patient name. Status code: {response.status_code}")
            return renamed_studyID

    else:
        print(f"No study found or error fetching data for study_id: {study_id}")
        return renamed_studyID

# Example usage
if __name__ == "__main__":
    study_id ="94a10c91-83981b79-bde64949-fd87a2f4-142a4263"
    new_name = "naya naam"
    print(rename_patient(study_id, new_name))
