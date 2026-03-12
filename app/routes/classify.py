from fastapi import HTTPException, status, APIRouter, UploadFile
from app.schemas import ClassifyResponse
from app.services.classifier import classify_image

router = APIRouter(prefix="/api/v1/classify", tags=["classify"])

@router.post("/", response_model=ClassifyResponse)
async def send_image(image: UploadFile):
    image_bytes = await image.read()
    return await classify_image(image_bytes)