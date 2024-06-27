import requests

# Base URL for the Orthanc instance
ORTHANC_URL = 'http://localhost:8042'

def delete_all_studies(specific_study_ids=None):
    # Endpoint to retrieve all studies
    studies_url = f'{ORTHANC_URL}/studies'
    
    try:
        # Get all studies
        response = requests.get(studies_url)
        response.raise_for_status()
        study_ids = response.json()
        
        # If specific_study_ids are provided, delete only those studies
        if specific_study_ids:
            not_found_studies = [study_id for study_id in specific_study_ids if study_id not in study_ids]
            if not_found_studies:
                print(f'Studies with IDs {not_found_studies} not found.')
                return
            
            study_ids = specific_study_ids  # Process only the specific study IDs
        
        # Delete each study
        for study_id in study_ids:
            study_delete_url = f'{ORTHANC_URL}/studies/{study_id}'
            delete_response = requests.delete(study_delete_url)
            delete_response.raise_for_status()
            print(f'Successfully deleted study: {study_id}')
    
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
        
if __name__ == '__main__':
    # Example usage to delete specific studies by their Study Instance UIDs
    specific_study_ids = [
    ] # Replace with the actual Study Instance UIDs

    if not specific_study_ids:
        delete_all_studies()
    else:
        delete_all_studies(specific_study_ids)
