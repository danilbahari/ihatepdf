Struktur Folder Awal
ihatepdf/
├── main.py               # Entry point FastAPI
├── tools.py              # Fungsi kompres, dll
├── templates/            # HTML frontend (pakai Jinja2)
│   └── index.html
├── static/               # CSS, JS, gambar, dll
│   └── style.css
└── uploads/              # Tempat simpan file PDF yg diupload

Install FastAPI dan Uvicorn
pip install fastapi[all] python-multipart
