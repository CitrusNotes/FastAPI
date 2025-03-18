from fastapi import FastAPI, File, UploadFile
from manager import Manager  # Import the Manager class

app = FastAPI()
manager = Manager()  # Create an instance of Manager

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = manager.save_file(file)
    return {"filename": file.filename, "path": file_path, "status": "uploaded successfully"}

@app.get("/files/")
def list_files():
    files = manager.get_file_list()
    return {"files": files}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
