from PyPDF2 import PdfReader
import sys

def extract_text(input_file):
    reader = PdfReader(input_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Cara pakai: python extract_text.py input.pdf")
        sys.exit(1)

    input_pdf = sys.argv[1]
    result = extract_text(input_pdf)

    print(result)
