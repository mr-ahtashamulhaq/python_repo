# Bulk File Renamer

A Python script that renames all files of a given type in a folder to
sequential numbers — `1.png`, `2.png`, `3.png`, and so on.

## Usage

Open the script and set your folder path and target extension:
```python
folder_path = "C:/Users/YourUsername/Desktop/your_folder"
rename_files_in_folder(folder_path, ".png")
```

Then run:
```bash
python bulk_file_renamer.py
```

The script prints each rename operation as it runs:
```
Renamed photo_abc.png --> 1.png
Renamed img_final.png --> 2.png
Renamed screenshot.png --> 3.png
```

## Changing the File Type

The second argument controls which extension gets renamed. You can point it
at any format:
```python
rename_files_in_folder(folder_path, ".jpg")
rename_files_in_folder(folder_path, ".mp4")
rename_files_in_folder(folder_path, ".txt")
```

## Requirements

No external libraries. Just Python 3.

## ⚠️ Warning

This operation is irreversible. The original filenames are gone once the
script runs. Test it on a copy of your folder first.

## What I Learned

- Listing and filtering files with `os.listdir()`
- Renaming files with `os.rename()`
- Building file paths correctly with `os.path.join()`
- Using `enumerate()` for index-based naming