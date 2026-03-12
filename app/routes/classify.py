import uuid
from fastapi import HTTPException, status, APIRouter

router = APIRouter(prefix="/api/v1/classify", tags=["classify"])

@router.post("/", response_model=ClassifyResponse)
async send_image(paylaod: image):
