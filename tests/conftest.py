import pytest
from api.user_api import UserAPI
from utils.logger import logger
from api.base_client import BaseClient

@pytest.fixture(scope="session")
def user_context() -> dict:
    """
    Fixture: user_context
    TC_API_001 - Register a New User (Valid)
    TC_API_003 - Login with Valid Credentials
    Returns:
        dict: Contains 'token', 'userId', 'username'
    """
    logger.info(":::Test started: TC_API_001 - Register a New User (Valid)")
    try:
        user_api = UserAPI()
        registered = user_api.register_user()
        assert registered, "User registration failed."
    except Exception as e:
        logger.error(f"TC_API_001 failed: {e}")
        pytest.fail(f"TC_API_001 failed: {e}")

    logger.info(":::Test started: TC_API_003 - Login with Valid Credentials")
    try:
        login_data = user_api.login_user()
        assert login_data, "Login failed after registration."
        assert all(k in login_data for k in ("token", "userId", "username")), \
            f"Login response missing required fields: {login_data}"
        return login_data
    except Exception as e:
        logger.error(f"TC_API_003 failed: {e}")
        pytest.fail(f"TC_API_003 failed: {e}")

@pytest.fixture(scope="session")
def auth_client(user_context) -> BaseClient:
    """
    Fixture: auth_client
    Provides an authorized BaseClient using the registered test user
    """
    return BaseClient(token=user_context["token"])
