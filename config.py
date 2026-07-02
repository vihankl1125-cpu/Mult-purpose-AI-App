import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(), override=True)


def _strip_env(value: str) -> str:
    if not isinstance(value, str):
        return ""
    return value.strip().strip('"').strip("'")


DEFAULT_HF_IMAGE_MODELS = [
    "black-forest-labs/FLUX.1-schnell",
    "stabilityai/stable-diffusion-3-medium",
]

HF_API_KEY = _strip_env(os.getenv("HF_API_KEY", ""))
GROQ_API_KEY = _strip_env(os.getenv("GROQ_API_KEY", ""))


def get_hf_image_models() -> list[str]:
    env_value = _strip_env(os.getenv("HF_IMAGE_MODEL", ""))
    if env_value:
        return [env_value]
    return DEFAULT_HF_IMAGE_MODELS


def get_hf_image_model() -> str:
    models = get_hf_image_models()
    return models[0] if models else ""
