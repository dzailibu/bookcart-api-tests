import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

class Config:
    """Stores configuration values and loads environment variables."""
    BASE_URL = os.getenv("BASE_URL")
    TIMEOUT = 10  # seconds
    RETRY_COUNT = 3
