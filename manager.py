import os
import json
from fastapi import UploadFile

# Load configuration
with open("config.json", "r") as config_file:
    config = json.load(config_file)

UPLOAD_DIR = config.get("upload_dir", "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

class Manager:
    def __init__(self):
        self.upload_dir = UPLOAD_DIR  # Load from config

    def save_file(self, file: UploadFile) -> str:
        file_path = os.path.join(self.upload_dir, file.filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())  # Read & write file
        return file_path  # Return saved file path

    def get_file_list(self):
        return os.listdir(self.upload_dir)  # Return list of uploaded files
