import requests

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

if __name__=="__main__":
    ORTHANC_URL = "http://localhost:8042"
    delete_studies(["1971163a-26b23f46-66a62f33-229e6a17-9fddfee0"])