# PDF Merger

A Python script that merges all PDF files in a folder into one.

## What It Does

Reads every `.pdf` file from a `pdffiles/` directory, combines their pages
in order, and writes the result to `merged_pdf_file.pdf`.

## Usage

1. Create a folder named `pdffiles` in the same directory as the script
2. Drop all the PDFs you want to merge into that folder
3. Run the script
```bash
python main.py
```

The merged output will appear as `merged_pdf_file.pdf` in the same directory.

## Requirements
```bash
pip install pypdf
```

## Project Structure
```
pdf-merger/
├── main.py
├── pdffiles/
│   ├── document1.pdf
│   ├── document2.pdf
│   └── ...
└── merged_pdf_file.pdf   ← generated after running
```

## What I Learned

- Reading and writing PDF files with `pypdf`
- Walking a directory with `os.listdir()`
- Working with binary file modes (`wb`)