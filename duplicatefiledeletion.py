import os
import hashlib

def get_file_checksum(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        buf = file.read()
        hasher.update(buf)
    return hasher.hexdigest()

def find_duplicate_files(directory_path):
    file_checksums = {}
    duplicate_files = []

    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_checksum = get_file_checksum(file_path)
            if file_checksum in file_checksums:
                duplicate_files.append(file_path)
            else:
                file_checksums[file_checksum] = file_path

    return duplicate_files

def remove_duplicate_files(duplicate_files):
    for file_path in duplicate_files:
        os.remove(file_path)
        print(f"Removed duplicate file: {file_path}")

if __name__ == "__main__":
    directory_path = "path/to/your/directory"

    duplicate_files = find_duplicate_files(directory_path)
    if duplicate_files:
        remove_duplicate_files(duplicate_files)
    else:
        print("No duplicate files found")
