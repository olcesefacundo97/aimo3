from dataclasses import dataclass
import os

@dataclass
class Settings:
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
    num_attempts: int = int(os.getenv("NUM_ATTEMPTS", 5))
    temperature: float = float(os.getenv("TEMPERATURE", 0.2))

settings = Settings()
