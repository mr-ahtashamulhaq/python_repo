# Research Text Cleaner

A command-line script that strips formatting noise from research documents before further processing.

## What It Removes

- Asterisks (`*`) and hashes (`#`) — usually leftover markdown formatting
- Bracketed citations like `[1]`, `[2, 3]`, `[10–12]`

Everything else stays as-is, including original newlines and paragraph structure.

## Usage
```bash
# For .txt files
python clean_research.py input.txt output.txt

# For .docx files
python clean_research.py input.docx output.docx
```

## Requirements

Python 3.7+

For `.docx` support:
```bash
pip install python-docx
```

## How It Works

The script runs regex over each line individually, so newline characters are never touched. For `.docx` files, it walks through every paragraph and table cell and applies the same cleaning logic before saving a new file.

Three operations per line:
1. Strip `[...]` blocks (citations, ranges, anything inside brackets)
2. Remove `*` and `#`
3. Collapse multiple spaces/tabs into one

## What I Learned

- Using `argparse` for clean CLI interfaces
- Processing `.docx` files with `python-docx`
- Writing reusable regex patterns
- Handling both `.txt` and `.docx` with a single entry point