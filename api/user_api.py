import random
import string
import jwt
from api.base_client import BaseClient
from utils.logger import logger

class UserAPI(BaseClient):
    """Handles API interactions related to User operations such as login, registration, etc."""
    def __init__(self):
        """Initialize with a BaseClient instance for sending requests."""
        super().__init__()
        self.username = self._generate_username()
        self.password = "Password123"  # Matches backend pattern

    def _generate_username(self):
        """Generates temporary random username"""
        suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        return f"autotest_{suffix}"

    def register_user(self):
        """Register a new user using the given payload."""
        data = {
            "firstName": "Auto",
            "lastName": "Tester",
            "username": self.username,
            "password": self.password,
            "confirmPassword": self.password,
            "gender": "Male"
        }
        try:
            response = self.post("/User", json=data)
            if response.status_code == 200:
                logger.info(f"User registered: {self.username}")
                return True
            elif response.status_code == 400:
                logger.warning("User may already exist or invalid payload")
            else:
                logger.error(f"Unexpected response: {response.status_code}")
        except Exception as e:
            logger.error(f"Error registering user: {e}")
        return False

    def login_user(self):
        """
        Login with username and password to retrieve and set Bearer token.
        Returns: dict with token, userId, username
        """
        data = {
            "username": self.username,
            "password": self.password
        }
        try:
            response = self.post("/Login", json=data)
            if response.status_code == 200:
                token = response.json().get("token")
                logger.info(f"Login success. Token received.")
                decoded_token = jwt.decode(token, options={"verify_signature": False})
                userId = decoded_token.get("userId")
                return {
                    "token": token,
                    "userId": userId,
                    "username": self.username
                }
            else:
                logger.error(f"Login failed: {response.status_code}")
        except Exception as e:
            logger.error(f"Login error: {e}")
        return None
