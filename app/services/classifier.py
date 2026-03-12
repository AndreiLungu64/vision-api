from app.config import settings
import httpx

API_URL = f"https://api-inference.huggingface.co/models/{settings.model_name}"

async def classify_image(image_bytes: bytes) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            API_URL,
            content=image_bytes,
            headers={"Authorization": f"Bearer {settings.hf_token}"},
        )

        results = response.json()

        predictions = [{"label" : r["label"], "confidence": round(r["score"], 4)} for r in results]
        top = predictions[0]
        return {
            "predictions": predictions,
            "top_label": top["label"],
            "top_confidence": top["confidence"],
            "needs_review": top["confidence"] < settings.confidence_threshold,
        }