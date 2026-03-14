from pydantic import BaseModel

class Prediction(BaseModel):
    label: str
    confidence: float

class ClassifyResponse(BaseModel):
    predictions: list[Prediction]
    top_label: str
    top_confidence: float
    needs_review: bool