import pytest
from utils.logger import logger
from helper.helper import Helper as helper

@pytest.mark.smoke
def test_user_smoke_flow(auth_client, user_context):
    """
    Smoke Test Flow:
    - TC_API_001: Register a New User (Valid)  [handled in conftest.py]
    - TC_API_003: Login with Valid Credentials [handled in conftest.py]
    - TC_API_005: Get All Books (Simulate Browsing)
    - TC_API_010: Add Book to Cart (Random, Valid)
    - TC_API_012: Get Cart Contents
    - TC_API_015: Perform Checkout (Valid)
    - TC_API_016: Fetch Orders History
    """
    user_id = user_context["userId"]
    logger.info("Starting smoke test: add to cart, checkout, get orders")

    # TC_API_005 - Get All Books
    logger.info(":::Test started: TC_API_005 - Get All Books (Simulate Browsing)")
    try:
        books_resp = auth_client.get("/Book")
        assert books_resp.status_code == 200, f"Expected 200, got {books_resp.status_code}. Response: {books_resp.text}"
        books = books_resp.json()
        assert isinstance(books, list), f"Expected list, got {type(books).__name__}"
        assert all("bookId" in book and "title" in book for book in books), "Some books missing required fields"
        logger.info(f"Found {len(books)} books.")
        BOOK_ID_TO_TEST = helper.get_random_book(books)
    except Exception as e:
        logger.error(f"Exception in TC_API_005 - Get All Books: {e}")
        pytest.fail(f"TC_API_005 failed: {e}")

    # TC_API_010 - Add Book to Cart
    logger.info(":::Test started: TC_API_010 - Add Book to Cart (Random, Valid)")
    try:
        add_cart_resp = auth_client.post(f"/ShoppingCart/AddToCart/{user_id}/{BOOK_ID_TO_TEST}")
        assert add_cart_resp.status_code in [200, 204], f"Unexpected status code: {add_cart_resp.status_code}. Response: {add_cart_resp.text}"
        logger.info(f"Book added to cart. Book ID: {BOOK_ID_TO_TEST}")
    except Exception as e:
        logger.error(f"Exception in TC_API_010 - Add to Cart: {e}")
        pytest.fail(f"TC_API_010 failed: {e}")

    # TC_API_012 - Get Cart Contents
    logger.info(":::Test started: TC_API_012 - Get Cart Contents")
    try:
        cart_resp = auth_client.get(f"/ShoppingCart/{user_id}")
        assert cart_resp.status_code == 200, f"Expected 200, got {cart_resp.status_code}. Response: {cart_resp.text}"
        cart_items = cart_resp.json()
        assert isinstance(cart_items, list), f"Expected list, got {type(cart_items).__name__}"
        matching_items = [item for item in cart_items if item["book"]["bookId"] == BOOK_ID_TO_TEST]
        assert matching_items, f"Book ID {BOOK_ID_TO_TEST} not found in cart. Cart: {[item['book']['bookId'] for item in cart_items]}"
        logger.info("Verified book is in cart.")
    except Exception as e:
        logger.error(f"Exception in TC_API_012 - Get Cart Contents: {e}")
        pytest.fail(f"TC_API_012 failed: {e}")

    # TC_API_015 - Perform Checkout
    logger.info(":::Test started: TC_API_015 - Perform Checkout (Valid)")
    try:
        cart_total = sum(int(item["book"]["price"]) * int(item["quantity"]) for item in cart_items)
        checkout_data = {
            "orderDetails": cart_items,
            "cartTotal": cart_total
        }
        checkout_resp = auth_client.post(f"/CheckOut/{user_id}", json=checkout_data)
        assert checkout_resp.status_code == 200, f"Expected 200, got {checkout_resp.status_code}. Response: {checkout_resp.text}"
        logger.info(f"Checkout successful. Total sum in cart: {cart_total}")
    except Exception as e:
        logger.error(f"Exception in TC_API_015 - Checkout: {e}")
        pytest.fail(f"TC_API_015 failed: {e}")

    # TC_API_016 - Fetch Orders History
    logger.info(":::Test started: TC_API_016 - Fetch Orders History")
    try:
        orders_resp = auth_client.get(f"/Order/{user_id}")
        assert orders_resp.status_code == 200, f"Expected 200, got {orders_resp.status_code}. Response: {orders_resp.text}"
        orders = orders_resp.json()
        assert isinstance(orders, list), f"Expected list, got {type(orders).__name__}"
        assert len(orders) > 0, "Order list is empty after checkout"
        logger.info(f"Orders fetched and verified. Total orders: {len(orders)}")
    except Exception as e:
        logger.error(f"Exception in TC_API_016 - Fetch Orders: {e}")
        pytest.fail(f"TC_API_016 failed: {e}")
