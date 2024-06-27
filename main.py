from fastapi import FastAPI, Form, File, UploadFile, HTTPException 
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from typing import List, Optional
import shutil
import os
import requests
import pandas as pd
import paramiko
import datetime

from Upload.upload import *
from Upload.unzip_and_upload_to import *
from Upload.UP_new_study_from_array import *

from Download.main_download import *

from SCP.scp import scp_transfer
from delete_studies.delete_studies import delete_all_studies
from Get_studies.get_studies import get_studies



app = FastAPI()

# Mount static files to serve HTML files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_homepage():
    with open("static/HOMEpage.html") as f:
        return HTMLResponse(content=f.read(), media_type="text/html")

@app.get("/upload", response_class=HTMLResponse)
async def read_upload():
    with open("static/Upload.html") as f:
        return HTMLResponse(content=f.read(), media_type="text/html")

@app.post("/upload")
async def handle_upload(
    dir_path: str = Form(...),
    # target_dir: str = Form(...),
    # csv_file: UploadFile = File(...),
    anonymization_flag: Optional[bool] = Form(False),
    batch_size: int = Form(...)
):
    ORTHANC_URL="http://localhost:8042"
    csv_file_path = "Final.csv"
    # Record studies stored
    old_studies = requests.get(f"http://localhost:8042/studies").json()

    # Call the Upload function (assuming it's defined elsewhere)
    Upload(dir_path, anonymization_flag, csv_file_path, batch_size)
    
    # Record All studies after upload
    new_studies = requests.get(f"{ORTHANC_URL}/studies").json()
    
    download_these_studies=find_new_element(old_studies, new_studies)

    '''Download Functionality begins '''

    # Get today's date in DDMMYYYY format
    formatted_date = datetime.datetime.today().strftime('%d_%m_%Y')
    formatted_datetime = datetime.datetime.today().strftime('%H_%M_%S___%d_%m_%Y')

    # Define the directory path
    directory_path = os.path.join("ZIP_FILES", formatted_date)

    # Create the directory
    os.makedirs(directory_path)

    # Download all these functoins in new directory
    
    zip_file_path=download_studies(directory_path,formatted_datetime,download_these_studies)

    unzip_and_upload_to(zip_file_path)

    with open("static/Download.html") as f:
        return HTMLResponse(content=f.read(), media_type="text/html")

        
@app.get("/download", response_class=HTMLResponse)
async def read_download():
    with open("static/Download.html") as f:
        return HTMLResponse(content=f.read(), media_type="text/html")

@app.post("/download")
async def handle_download(
    name: str = Form(...),
    download_dir_path: str = Form(...),
    study_ids: str = Form([])
):  
    print(study_ids)
    if study_ids =="all":
        download_studies(download_dir_path,name)
    else:
        download_studies(download_dir_path,name,study_ids)
    return {"message": "Download data received"}

@app.get("/scp-transfer", response_class=HTMLResponse)
async def read_scp_transfer():
    with open("static/SCP Transfer.html") as f:
        return HTMLResponse(content=f.read(), media_type="text/html")

@app.post("/scp-transfer")
async def handle_scp_transfer(
    source_host: str = Form(...),
    source_user: str = Form(...),
    source_file_path: str = Form(...),
    dest_host: str = Form(...),
    dest_user: str = Form(...),
    dest_file_path: str = Form(...),
    port: int = Form(...)
):
    scp_transfer(source_host,source_user,source_file_path,dest_host,dest_user,dest_file_path,port)


@app.get("/reprocess", response_class=HTMLResponse)
async def read_reprocess():
    with open("static/Reprocess.html") as f:
        return HTMLResponse(content=f.read(), media_type="text/html")

@app.post("/reprocess")
async def handle_reprocess(
    uhid: str = Form(...)
):
    print(f"Received reprocess data: uhid={uhid}")
    return {"message": "Reprocess data received"}

@app.get("/delete-studies", response_class=HTMLResponse)
async def read_delete_studies():
    with open("static/Delete.html") as f:
        return HTMLResponse(content=f.read(), media_type="text/html")

@app.post("/delete-studies")
async def handle_delete_studies(uhids=None):
    print(uhids)
    if uhids is not None:
        delete_all_studies([uhids])
    else: 
        delete_all_studies()
    return {"message": "Delete studies request received"}

@app.get("/get-studies-page", response_class=HTMLResponse)
async def read_get_studies_page():
    with open("static/GetStudies.html") as f:
        return HTMLResponse(content=f.read(), media_type="text/html")

@app.get("/get-studies", response_class=JSONResponse)
async def get_studies_endpoint():
    # Mock data for demonstration purposes
    studies = get_studies()
    return {"studies": studies}

# To run the server, use the command: uvicorn main:app --reload
