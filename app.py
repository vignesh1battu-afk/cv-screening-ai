from fastapi import FastAPI, UploadFile, File
import shutil
import os

from aws.queue import send_to_queue

app = FastAPI()

# ensure uploads folder exists
if not os.path.exists("uploads"):
    os.makedirs("uploads")


@app.get("/")
def home():
    return {"message": "CV Screening API Running"}


@app.post("/upload-cv/")
async def upload_cv(file: UploadFile = File(...)):
    
    file_path = f"C:/Users/vigne/Desktop/cv screening/uploads/{file.filename}"

    # save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # send file name to queue
    send_to_queue(file.filename)

    return {"message": "File uploaded and sent to queue"}