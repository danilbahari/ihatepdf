# cli.py (final versi clean)

import argparse
from PyPDF2 import PdfReader, PdfWriter

def compress_pdf(input_path, output_path, quality="high"):
    reader = PdfReader(input_path)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    # catatan: PyPDF2 tidak support kompresi kualitas gambar, ini simulasi saja
    with open(output_path, "wb") as f:
        writer.write(f)

def merge_pdfs(inputs, output):
    writer = PdfWriter()
    for path in inputs:
        reader = PdfReader(path)
        for page in reader.pages:
            writer.add_page(page)
    with open(output, "wb") as f:
        writer.write(f)

def split_pdf(input_path, start, end, output):
    reader = PdfReader(input_path)
    writer = PdfWriter()
    for i in range(start-1, end):
        writer.add_page(reader.pages[i])
    with open(output, "wb") as f:
        writer.write(f)

def extract_text(input_path, output):
    reader = PdfReader(input_path)
    with open(output, "w", encoding="utf-8") as f:
        for page in reader.pages:
            f.write(page.extract_text() or "")

def main():
    parser = argparse.ArgumentParser(description="iHatePDF CLI Tools")
    subparsers = parser.add_subparsers(dest="command")

    # compress
    compress_parser = subparsers.add_parser("compress")
    compress_parser.add_argument("input")
    compress_parser.add_argument("output")
    compress_parser.add_argument("--quality", choices=["high", "low"], default="high")

    # merge
    merge_parser = subparsers.add_parser("merge")
    merge_parser.add_argument("inputs", nargs="+")
    merge_parser.add_argument("output")

    # split
    split_parser = subparsers.add_parser("split")
    split_parser.add_argument("input")
    split_parser.add_argument("start", type=int)
    split_parser.add_argument("end", type=int)
    split_parser.add_argument("output")

    # extract
    extract_parser = subparsers.add_parser("extract")
    extract_parser.add_argument("input")
    extract_parser.add_argument("output")

    args = parser.parse_args()

    if args.command == "compress":
        compress_pdf(args.input, args.output, args.quality)
    elif args.command == "merge":
        merge_pdfs(args.inputs[:-1], args.inputs[-1])
    elif args.command == "split":
        split_pdf(args.input, args.start, args.end, args.output)
    elif args.command == "extract":
        extract_text(args.input, args.output)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
