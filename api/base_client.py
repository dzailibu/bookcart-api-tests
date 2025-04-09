import requests
from requests.adapters import HTTPAdapter, Retry
from config.config import Config
from utils.logger import logger

class BaseClient:
    """Base client class to handle common HTTP request methods with error handling,
    timeout, and retry mechanisms for API calls."""
    def __init__(self, token=None, base_url=Config.BASE_URL):
        """Initialize the client with base URL and headers."""
        self.base_url = base_url
        self.token = token
        self.session = requests.Session()
        self.timeout = Config.TIMEOUT
        self.token = token

        if self.token is not None:
            retries = Retry(
                total=Config.RETRY_COUNT,
                backoff_factor=1,
                status_forcelist=[502, 503, 504]
            )
            self.session.mount("https://", HTTPAdapter(max_retries=retries))
            self.session.headers.update({
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json"
            })


    def _full_url(self, path):
        """Provides full URL for appropriate API Endpoint"""
        return f"{self.base_url}{path}"

    def get(self, path, **kwargs):
        """Send a GET request to the specified endpoint with optional query parameters."""
        url = self._full_url(path)
        try:
            logger.debug(f"GET {url}")
            response = self.session.get(url, timeout=self.timeout, **kwargs)
            logger.debug(f"Response: {response.status_code} - {response.text}")
            return response
        except Exception as e:
            logger.error(f"GET failed: {e}")
            raise

    def post(self, path, json=None, **kwargs):
        """Send a POST request with optional data or JSON body."""
        url = self._full_url(path)
        try:
            logger.debug(f"POST {url} | Payload: {json}")
            response = self.session.post(url, json=json, timeout=self.timeout, **kwargs)
            logger.debug(f"Response: {response.status_code} - {response.text}")
            return response
        except Exception as e:
            logger.error(f"POST failed: {e}")
            raise

    def put(self, path, json=None, **kwargs):
        """Send a PUT request with optional data or JSON body."""
        url = self._full_url(path)
        try:
            logger.debug(f"PUT {url} | Payload: {json}")
            response = self.session.put(url, json=json, timeout=self.timeout, **kwargs)
            logger.debug(f"Response: {response.status_code} - {response.text}")
            return response
        except Exception as e:
            logger.error(f"PUT failed: {e}")
            raise

    def delete(self, path, **kwargs):
        """Send a DELETE request to the specified endpoint."""
        url = self._full_url(path)
        try:
            logger.debug(f"DELETE {url}")
            response = self.session.delete(url, timeout=self.timeout, **kwargs)
            logger.debug(f"Response: {response.status_code} - {response.text}")
            return response
        except Exception as e:
            logger.error(f"DELETE failed: {e}")
            raise
