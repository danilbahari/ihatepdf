from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from tools import compress_pdf
import os
import shutil
from pathlib import Path

app = FastAPI()

# Folder statis (buat file HTML dan hasil download)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Folder upload dan hasil
UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

# Tampilkan halaman utama
@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

# Endpoint untuk kompres PDF
@app.post("/compress")
async def compress(file: UploadFile = File(...)):
    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    output_path = os.path.join(RESULT_FOLDER, "compressed_" + file.filename)

    # Simpan file yang diupload
    with open(input_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # Panggil fungsi kompres dari tools.py
    success, message = compress_pdf(input_path, output_path)

    if success:
        return FileResponse(path=output_path, filename="compressed_" + file.filename, media_type='application/pdf')
    else:
        return {"error": message}
