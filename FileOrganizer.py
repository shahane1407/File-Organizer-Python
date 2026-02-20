import os
import shutil
# Folder paths you want to organize
folder_paths = os.getcwd()  # Current working directory

# File type mappings
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Videos': ['.mp4', '.avi', '.mkv', '.avif'],
    'Archives': ['.zip', '.rar', '.tar.gz']
}

# Create folders if they don't exist
for folder in file_types.keys():
    folder_path = os.path.join(folder_paths, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Organize files
for file in os.listdir(folder_paths):
    file_path = os.path.join(folder_paths, file)

    #skip folders
    if not os.path.isfile(file_path):
        continue

    # get file extension
    # print(os.path.splitext(file))
    file_extension = os.path.splitext(file)[1].lower()

    for folder, extensions in file_types.items():
        if file_extension in extensions:
            shutil.move(file_path, os.path.join(folder_paths, folder, file))
            
print("File Organization Completed!✅")