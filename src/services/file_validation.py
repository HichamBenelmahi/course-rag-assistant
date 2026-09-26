from src.helpers import get_settings
import os
from fastapi import UploadFile , HTTPException

def validation_upload_file(file:UploadFile):
    extension_fichier = os.path.splitext(file.filename)[1]
    settings = get_settings
    if extension_fichier != settings.FILE_ALLOWED_TYPES.value:
        return 'erreur de fichier type'
    elif file.size !=  settings.FILE_MAX_SIZE_MB.value * 1000000 :