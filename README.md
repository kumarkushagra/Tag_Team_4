# Orthanc PACS Tool

## Introduction
This repository contains source code for a tool to interact with Orthanc PACS, allowing for upload, download, delete, and SCP (under development) operations. The Orthanc server URL is set to `http://localhost:8042`.

## Requirements
1. Orthanc server must be hosted.
2. Python must be installed.
3. All libraries specified in `requirements.txt` must be installed in a virtual environment.

## How to Run
Clone this repository and run the following command in the terminal (ensure requirements are met):

```sh
uvicorn main:app
```

Note: The `static` directory contains HTML files only.

## Functionality of Each Module

### 1. Upload

This module includes functions to:
- Shortlist UHIDs based on "Uploaded" and "LLM" status in `Final.csv`.
- Create new batches by copying directories (batch size is user-defined).
- Upload all studies.
- Anonymize each study after uploading to PACS.
- Rename the study after anonymization.
- Store data in `Database/mapping.csv`.

After successfully uploading a UHID to PACS, the "Uploaded" column in `Final.csv` is updated from '0' to '1' to prevent re-uploading in subsequent runs.

All related functions are in the `Upload` directory. The `upload.py` file orchestrates calling these functions and uploading the batches. Files prefixed with `UP_` are responsible for batch uploads. The redundant `Upload_Entire_Batch` directory contains files called by the `Upload_Batch()` function.

## Directory Structure

- `Upload/`: Contains all functions and scripts for the upload process.
- `Upload_Entire_Batch/`: Contains files used by the `Upload_Batch()` function.
- `static/`: Contains HTML files only.


---

### 2. Download

This module includes functions to:

- Store all study IDs from Orthanc PACS in an array (if not provided by the user).
- Download each study ID from PACS to local storage. Extract the ZIP files immediately after download and delete the ZIP files.
- After all studies are downloaded and extracted, ZIP them into one file.
- Delete all individual study files except the final ZIP file.

All functions are stored in the `Download` directory. The `main_download.py` script calls the helper functions to perform these operations.

**Note:** Ensure the download directory is empty to avoid any errors.

---
