from PyPDF2 import PdfReader, PdfWriter
import os

def compress_pdf(input_path, output_path):
    try:
        reader = PdfReader(input_path)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        # Kompres dengan menghilangkan metadata & optimisasi
        writer.remove_links()
        writer.add_metadata({})

        with open(output_path, 'wb') as f:
            writer.write(f)

        return True, "Kompresi berhasil"
    except Exception as e:
        return False, f"Terjadi kesalahan: {str(e)}"
