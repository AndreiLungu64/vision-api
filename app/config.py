from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    hf_token: str
    model_name: str = "google/vit-base-patch16-224"
    confidence_threshold: float = 0.85
    model_config = {"env_file": ".env"}

settings = Settings()