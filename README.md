# FastAPI File Upload System

This repository contains a FastAPI-based file upload system. It allows users to upload files via a React frontend and store them in a local directory.

## Features
- Upload files to the FastAPI backend.
- Store files in a designated local directory.
- Integration with a React frontend.

## Setup Instructions

### 1. Install Dependencies
Ensure you have Python 3 installed. Then, install FastAPI and Uvicorn:
```sh
pip install fastapi uvicorn python-multipart
```

### 2. Run the FastAPI Server
```sh
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000/`.

### 3. Test the API
Navigate to:
- [Swagger UI](http://127.0.0.1:8000/docs) – Test the `/upload/` endpoint.

### 4. File Storage
Uploaded files are saved in the `uploads/` directory. Ensure this folder exists before running the server:
```sh
mkdir -p uploads
```

## API Endpoints

### **Upload File**
- **Endpoint:** `POST /upload/`
- **Request:** Multipart form data with a file.
- **Response:** JSON containing the filename and status.

Example:
```json
{
    "filename": "example.txt",
    "status": "uploaded successfully"
}
```

## Connecting to the React Frontend
To integrate with React:
1. Implement a frontend file upload form.
2. Use `fetch()` to send files to `http://127.0.0.1:8000/upload/`.
3. Display success/error messages.

## Next Steps
- Implement file listing and retrieval.
- Improve error handling.
- Enhance UI for better user experience.

## License
This project is open-source. Modify as needed
