from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    base_url: str = "https://router.huggingface.co/hf-inference/models/"
    hf_token: str
    model_name: str
    confidence_threshold: float = 0.85

    @property
    def api_url(self) -> str:
        return f"{self.base_url}{self.model_name}"
    
    model_config = {"env_file": ".env"}

settings = Settings()