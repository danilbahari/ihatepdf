# cli.py (percobaan awal)

import argparse
from PyPDF2 import PdfReader, PdfWriter

def compress_pdf(input_path, output_path):
    reader = PdfReader(input_path)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    with open(output_path, "wb") as f:
        writer.write(f)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PDF Tools CLI")
    parser.add_argument("command", help="Command: compress")
    parser.add_argument("input", help="Input PDF")
    parser.add_argument("output", help="Output PDF")

    args = parser.parse_args()

    if args.command == "compress":
        compress_pdf(args.input, args.output)
