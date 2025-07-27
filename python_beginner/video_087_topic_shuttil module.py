# Copy "notes.txt" from the "semester1" folder to the "semester2" folder using shutil.copy()

import shutil

shutil.copy('semester1/notes.txt', 'semester2/notes.txt')


# Copy the entire "project_backup" folder to a new folder named "project_backup_copy" using shutil.copytree()

shutil.copytree('project_backup', 'project_backup_copy')


# Move "old_results.csv" from the "downloads" folder to the "processed_data" folder using shutil.move()

shutil.move('downloads/old_results.csv', 'processed_data/old_results.csv')


# Delete the folder "temp_files" and everything inside it using shutil.rmtree()

shutil.rmtree('temp_files')