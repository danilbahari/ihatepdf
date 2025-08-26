from fastapi import FastAPI, UploadFile, File
import shutil
import os
from tools import compress_pdf

app = FastAPI()

UPLOAD_DIR = "uploaded"
OUTPUT_DIR = "output"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.get("/")
async def root():
    return {"message": "Aplikasi PDF Offline Siap Digunakan!"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_location = f"{UPLOAD_DIR}/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"message": "File uploaded successfully", "filename": file.filename}

@app.post("/compressed")
async def compress_uploaded_pdf(file: UploadFile = File(...)):
    input_path = f"{UPLOAD_DIR}/{file.filename}"
    output_path = f"{OUTPUT_DIR}/compressed_{file.filename}"

    with open(input_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # Kompres PDF
    compress_pdf(input_path, output_path)

    return {"message": "File berhasil dikompres", "output_file": output_path}
