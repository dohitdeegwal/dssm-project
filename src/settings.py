import os
from dotenv import load_dotenv
from typing import NamedTuple, List

load_dotenv()

settings_config = {
    "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
    "TEMPERATURE": os.getenv("TEMPERATURE", 0),
    "CHAT_MODEL": os.getenv("CHAT_MODEL", "gpt-3.5-turbo"),
    "MAX_FILES": 20,
    "ORIGINS": os.getenv("ORIGINS").split(","),
}


class SettingsConfig(NamedTuple):
    OPENAI_API_KEY: str
    TEMPERATURE: int
    CHAT_MODEL: str
    MAX_FILES: int
    ORIGINS: List[str]


settings = SettingsConfig(**settings_config)
