import requests

def get_studies(): 
    url = "http://localhost:8042"
    
    # Fetch all patients
    response = requests.get(f"{url}/patients")
    if response.status_code != 200:
        print(f"Error fetching patients: {response.status_code} - {response.text}")
        exit()
    
    patients = response.json()
    
    # Process each patient
    for patient_id in patients:
        # print(f"Patient ID: {patient_id}")
    
        # Fetch studies for the patient
        response = requests.get(f"{url}/patients/{patient_id}/studies")
        if response.status_code != 200:
            print(f"Error fetching studies for patient ID {patient_id}: {response.status_code} - {response.text}")
            continue
    
        studies = response.json()
        return studies

        # Temperory Termination of code (using return statement)
    
        # Process each study for the patient
        if isinstance(studies, list) and len(studies) > 0:
            for study in studies:
                study_instance_uid = study['MainDicomTags']['StudyInstanceUID']
                print("Study Instance UID:", study_instance_uid)
                # Add your processing logic here for each study if needed
        else:
            print(f"No studies found for patient ID: {patient_id}")


if __name__=="__main__":
    print(get_studies())
