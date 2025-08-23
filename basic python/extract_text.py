import sys
import pytesseract
from pdf2image import convert_from_path

def extract_text_ocr(input_file, output_txt):
    pages = convert_from_path(input_file)
    with open(output_txt, "w", encoding="utf-8") as f:
        for i, page in enumerate(pages):
            text = pytesseract.image_to_string(page, lang="eng")
            f.write(f"\n--- Halaman {i+1} ---\n")
            f.write(text)
            print(f"[OK] Halaman {i+1} berhasil di-OCR")
    print(f"\n[SUKSES] Teks berhasil diekstraksi ke {output_txt}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Cara pakai: python extract_text_ocr.py input.pdf output.txt")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_txt = sys.argv[2]

    extract_text_ocr(input_pdf, output_txt)
