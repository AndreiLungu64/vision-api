from app.config import settings
import httpx

async def classify_image(image_bytes: bytes) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=f"{settings.api_url}",
            content=image_bytes,
            headers={
            "Authorization": f"Bearer {settings.hf_token}",
            "Content-Type": "application/octet-stream",
        },
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