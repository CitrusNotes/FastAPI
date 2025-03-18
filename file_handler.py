import os
from fastapi import UploadFile

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

class FileHandler:
    @staticmethod
    def save_file(file: UploadFile) -> str:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())  # Read & write file
        return file_path  # Return the saved file path

    @staticmethod
    def get_file_list():
        return os.listdir(UPLOAD_DIR)  # Return list of uploaded files
