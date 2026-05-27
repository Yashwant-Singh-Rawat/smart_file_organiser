import os
import shutil
import hashlib
import logging
from pathlib import Path

# -----------------------------
# CONFIGURATION
# -----------------------------

SOURCE_FOLDER = "test_folder"

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Archives": [".zip", ".rar"]
}

# -----------------------------
# LOGGING SETUP
# -----------------------------

logging.basicConfig(
    filename="organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# -----------------------------
# HASH FUNCTION
# -----------------------------

def get_file_hash(filepath):
    hasher = hashlib.md5()

    with open(filepath, "rb") as file:
        while chunk := file.read(4096):
            hasher.update(chunk)

    return hasher.hexdigest()

# -----------------------------
# MAIN ORGANIZER FUNCTION
# -----------------------------

def organize_files():

    hashes = {}

    source_path = Path(SOURCE_FOLDER)

    duplicate_folder = source_path / "Duplicates"
    duplicate_folder.mkdir(exist_ok=True)

    moved_count = 0
    duplicate_count = 0

    for file in source_path.iterdir():

        if file.is_dir():
            continue

        try:
            file_hash = get_file_hash(file)

            # DUPLICATE DETECTION
            if file_hash in hashes:
                shutil.move(str(file), duplicate_folder / file.name)

                logging.info(f"Duplicate moved: {file.name}")

                duplicate_count += 1
                continue

            hashes[file_hash] = file.name

            # FILE ORGANIZATION
            moved = False

            for folder_name, extensions in FILE_TYPES.items():

                if file.suffix.lower() in extensions:

                    target_folder = source_path / folder_name
                    target_folder.mkdir(exist_ok=True)

                    target_path = target_folder / file.name

                    # HANDLE NAME CONFLICTS
                    counter = 1

                    while target_path.exists():
                        target_path = target_folder / f"{file.stem}_{counter}{file.suffix}"
                        counter += 1

                    shutil.move(str(file), target_path)

                    logging.info(f"Moved: {file.name} -> {folder_name}")

                    moved_count += 1
                    moved = True
                    break

            if not moved:
                logging.info(f"Skipped: {file.name}")

        except Exception as e:
            logging.error(f"Error processing {file.name}: {e}")

    # FINAL REPORT
    print("\n===== ORGANIZATION COMPLETE =====")
    print(f"Files moved: {moved_count}")
    print(f"Duplicates found: {duplicate_count}")
    print("Log saved to organizer.log")

# -----------------------------
# RUN PROGRAM
# -----------------------------

if __name__ == "__main__":
    organize_files()
