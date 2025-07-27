# This program renames all PNG files (and other file formats ) in a folder to 1.png, 2.png, ..., n.png using the os module.

import os

def rename_files_in_folder(folder_path, extension):
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(extension.lower())]

    for idx, file in enumerate(files):
        new_name = f"{idx + 1}{extension}"
        old_path = os.path.join(folder_path, file)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed {file} --> {new_name}")


folder_path = "C:/Users/YourUsername/Desktop/test_folder"


rename_files_in_folder(folder_path, ".png")