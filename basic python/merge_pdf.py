from PyPDF2 import PdfMerger
import sys

def merge_pdfs(input_files, output_file):
    merger = PdfMerger()
    for pdf in input_files:
        try:
            merger.append(pdf)
            print(f"[OK] {pdf} ditambahkan")
        except Exception as e:
            print(f"[ERROR] Gagal menambahkan {pdf}: {e}")
    merger.write(output_file)
    merger.close()
    print(f"\n[SUKSES] File berhasil digabungkan jadi: {output_file}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("❌ Cara pakai: python merge_pdf.py output.pdf file1.pdf file2.pdf [file3.pdf ...]")
        sys.exit(1)

    output = sys.argv[1]
    inputs = sys.argv[2:]
    merge_pdfs(inputs, output)
