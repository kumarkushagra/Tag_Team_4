import requests


def get_all_studies(orthanc_url="http://localhost:8042"):
    studies_url = f"{orthanc_url}/studies"
    response = requests.get(studies_url)
    if response.status_code != 200:
        print("Failed to retrieve studies")
        return
    
    return response.json()


if __name__ == "__main__":
    print(get_all_studies())