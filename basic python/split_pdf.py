from PyPDF2 import PdfReader, PdfWriter
import sys
import os

def split_pdf(input_file, output_folder):
    try:
        reader = PdfReader(input_file)
        total_pages = len(reader.pages)

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for i in range(total_pages):
            writer = PdfWriter()
            writer.add_page(reader.pages[i])

            output_path = os.path.join(output_folder, f"page_{i+1}.pdf")
            with open(output_path, "wb") as output_pdf:
                writer.write(output_pdf)
            
            print(f"[OK] Halaman {i+1} berhasil disimpan ke {output_path}")

        print(f"\n[SUKSES] {total_pages} halaman berhasil dipisah ke folder: {output_folder}")

    except Exception as e:
        print(f"[ERROR] Gagal split PDF: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("❌ Cara pakai: python split_pdf.py input.pdf output_folder")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_dir = sys.argv[2]

    split_pdf(input_pdf, output_dir)
