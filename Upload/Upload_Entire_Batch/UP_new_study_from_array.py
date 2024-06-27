import requests


def find_new_element(old_studies, new_studies):
    # Convert studies to a set for faster lookup
    # studies_set = set(old_studies)
    
    # Find elements in new_studies that are not in studies
    new_elements = [study for study in new_studies if study not in old_studies]
    
    return new_elements



if __name__ == "__main__":
    url = "http://localhost:8042"

    # update_url = f"{url}/patients/{patient_id}/modify"
    studies = requests.get(f"{url}/studies").json()
    print(studies)

    new_studies = studies+["euwcmi"]
    print(new_studies)
    new_elements = find_new_element(studies, new_studies)
    print(new_elements)  # Output: [{"id": 3, "name": "Study3"}]
