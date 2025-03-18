from fastapi import FastAPI, File, UploadFile
from file_handler import FileHandler  # Import the wrapper class

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = FileHandler.save_file(file)
    return {"filename": file.filename, "path": file_path, "status": "uploaded successfully"}

@app.get("/files/")
def list_files():
    files = FileHandler.get_file_list()
    return {"files": files}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
