from fastapi import FastAPI, Request, File, UploadFile, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from tools import kompres_pdf  # Import fungsi dari tools.py

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/kompres")
async def kompres(request: Request, file: UploadFile = File(...)):
    file_location = f"{UPLOAD_FOLDER}/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())

    output_path = f"{UPLOAD_FOLDER}/compressed_{file.filename}"
    kompres_pdf(file_location, output_path)

    return FileResponse(output_path, media_type='application/pdf', filename=f"compressed_{file.filename}")
