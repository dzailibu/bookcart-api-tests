
# Smoke Test Cases – Book Cart API

These test cases cover the most essential user flows and are automated in the smoke test suite.

---

### SMOKE_001 – User End-to-End Purchase Flow

1. Register new user
2. Login and get token
3. View books
4. Add book to cart
5. Checkout
6. Fetch order history

**Expected:** 
No errors, valid status codes, token used successfully.


### TC_API_001 - Register a New User (Valid)
- **Method:** POST /api/User
- **Body:**  
```json
{
  "firstName": "Auto",
  "lastName": "Tester",
  "username": "autotest_<random_suffix>",
  "password": "Password123",
  "confirmPassword": "Password123",
  "gender": "Male"
}
```
- **Expected:** 200 OK or 201 Created, User is registered successfully
- **Type:** Positive

---

### TC_API_003 - Login with Valid Credentials
- **Method:** POST /api/Login
- **Body:**  
```json
{
  "username": "autotest_<random_suffix>",
  "password": "Password123"
}
```
- **Expected:** 200 OK, JWT token returned in response
- **Type:** Positive

---

### TC_API_005 - Get All Books (Simulate Browsing)
- **Method:** GET /api/Book
- **Expected:** 200 OK, List of books returned
- **Type:** Positive

---

### TC_API_010 - Add Book to Cart (Random, Valid)
- **Method:** POST /api/ShoppingCart/AddToCart/{userId}/{bookId}
- **Expected:** 200 OK or 201 Created, Book is added to user's shopping cart
- **Notes:** `book_id` is selected using a random book from `/api/Book` response
- **Type:** Positive

---

### TC_API_012 - Get Cart Contents
- **Method:** GET /api/ShoppingCart/{userId}
- **Expected:** 200 OK, Cart items returned including previously added book
- **Type:** Positive

---

### TC_API_015 - Perform Checkout (Valid)
- **Method:** POST /api/CheckOut/{userId}
- **Body:**  
```json
{
  "orderDetails": [
    {
      "book": {
        "bookId": <book_id>,
        "title": "<title>",
        "author": "<author>",
        "category": "<category>",
        "price": <price>,
        "coverFileName": "<coverFileName>"
      },
      "quantity": 1
    }
  ],
  "cartTotal": <price>
}
```
- **Expected:** 200 OK, Checkout successful and order is placed
- **Type:** Positive

---

### TC_API_016 - Fetch Orders History
- **Method:** GET /api/Order/{userId}
- **Expected:** 200 OK, Returns orders made by the user
- **Type:** Positive