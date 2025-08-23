# iHatePDF (Offline Tools)

Project ini adalah perjalanan membangun aplikasi PDF offline (seperti iLovePDF, tapi internal dan open source).

## 🚀 Progress
- [x] Step 01: Basic compress PDF
- [X] Step 02: Merge PDF
- [ ] Step 03: CLI tools
- [ ] Step 04: Web app (FastAPI)
- [ ] Step 05: UI + TailwindCSS
- [ ] Step 06: Authentication + Deployment

## 📌 Cara Pakai (sementara)
-> Run Bash atau CMD

### Compress PDF
python compress_pdf.py input.pdf output.pdf

### Merge PDF
python merge_pdf.py hasil.pdf file1.pdf file2.pdf file3.pdf

### SPlit PDF
python split_pdf.py dokumen.pdf hasil_split

### Extract PDF
python extract_text.py contoh.pdf

*Stuck di tahap ekstraksi teks karena PyPDF2 tidak selalu bisa membaca semua PDF (terutama PDF hasil scan).