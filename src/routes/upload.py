from fastapi import APIRouter , File , UploadFile
import os 

router = APIRouter()

@router.post("/upload")
async def upload_files(file : UploadFile):
    return {"nom de fichier" : file.filename,
            "extensions" : os.path.splitext(file.filename)[1]
    }
