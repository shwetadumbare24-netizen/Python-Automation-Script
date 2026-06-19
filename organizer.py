import os
import shutil
from datetime import datetime

# Log Function
def write_log(message):
    with open("logs.txt", "a") as log:
        log.write(f"{datetime.now()} - {message}\n")

try:
    folder_path = input("Enter folder path: ").strip()

    # Remove quotes if pasted
    folder_path = folder_path.replace('"', '')
    print("\nChecking Path:", folder_path)
    if not os.path.isdir(folder_path):
        raise FileNotFoundError(f"Folder not found: {folder_path}")
    files = os.listdir(folder_path)

    for file in files:
        file_path = os.path.join(folder_path, file)

        # Skip folders
        if not os.path.isfile(file_path):
            continue
        
        # Get extension
        extension = os.path.splitext(file)[1][1:].upper()

        if extension == "":
            extension = "OTHERS"

        target_folder = os.path.join(folder_path, extension)

        # Create folder if not exists
        os.makedirs(target_folder, exist_ok=True)

        destination = os.path.join(target_folder, file)
        shutil.move(file_path, destination)
        print(f"Moved: {file} -> {extension}")
        write_log(f"Moved {file} to {extension}")

    print("\nFiles Organized Successfully!")
except Exception as e:
    write_log(f"ERROR: {str(e)}")
    print("\nError:", e)