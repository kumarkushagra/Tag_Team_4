import requests
from ..delete_study import delete_studies 
from ..new_study_from_array import find_new_element



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
            "Replace": {
                "PatientName": new_name
            }
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

        return renamed_studyID

        if response.status_code == 200:
            print(f"Patient name successfully updated to {new_name}")
        else:
            print(f"Failed to update patient name. Status code: {response.status_code}")
    else:
        print(f"No study found or error fetching data for study_id: {study_id}")

# Example usage
if __name__ == "__main__":
    study_id ="94a10c91-83981b79-bde64949-fd87a2f4-142a4263"
    new_name = "naya naam"
    print(rename_patient(study_id, new_name))
