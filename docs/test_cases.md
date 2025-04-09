
# API Test Cases for Book Cart Application

This document lists all identified test cases for the BookCart API, including both positive and negative scenarios.

---

## Authentication

### TC_API_001 - Register a New User (Valid)
- **Method:** POST /api/User
- **Body:** `{ valid user registration payload }`
- **Expected:** 200 OK or 201 Created
- **Type:** Positive

### TC_API_002 - Register a New User (Missing Required Fields)
- **Method:** POST /api/User
- **Body:** `{ missing username and password }`
- **Expected:** 400 Bad Request
- **Type:** Negative

### TC_API_003 - Login with Valid Credentials
- **Method:** POST /api/Login
- **Body:** `{ valid credentials }`
- **Expected:** 200 OK, JWT token returned
- **Type:** Positive

### TC_API_004 - Login with Invalid Password
- **Method:** POST /api/Login
- **Body:** `{ "username": "autotest", "password": "wrongpass" }`
- **Expected:** 401 Unauthorized
- **Type:** Negative

---

## Book

### TC_API_005 - Get All Books
- **Method:** GET /api/Book
- **Expected:** 200 OK, List of books returned
- **Type:** Positive

### TC_API_006 - Get Book by ID (Valid)
- **Method:** GET /api/Book/{id}
- **Expected:** 200 OK, Book details returned
- **Type:** Positive

### TC_API_007 - Get Book by ID (Invalid ID)
- **Method:** GET /api/Book/0
- **Expected:** 404 Not Found or error response
- **Type:** Negative

### TC_API_008 - Get Categories List
- **Method:** GET /api/Book/GetCategoriesList
- **Expected:** 200 OK, List of categories
- **Type:** Positive

### TC_API_009 - Get Similar Books (Valid Book ID)
- **Method:** GET /api/Book/GetSimilarBooks/{bookId}
- **Expected:** 200 OK, List of similar books
- **Type:** Positive

---

## Shopping Cart

### TC_API_010 - Add Book to Cart (Valid)
- **Method:** POST /api/ShoppingCart/AddToCart/{userId}/{bookId}
- **Expected:** 200 OK or 201 Created
- **Type:** Positive

### TC_API_011 - Add Book to Cart (Invalid User ID)
- **Method:** POST /api/ShoppingCart/AddToCart/0/{bookId}
- **Expected:** 404 Not Found or 400 Bad Request
- **Type:** Negative

### TC_API_012 - Get Cart Contents
- **Method:** GET /api/ShoppingCart/{userId}
- **Expected:** 200 OK, List of cart items
- **Type:** Positive

### TC_API_013 - Delete Book from Cart
- **Method:** DELETE /api/ShoppingCart/{userId}/{bookId}
- **Expected:** 200 OK or 204 No Content
- **Type:** Positive

### TC_API_014 - Update Quantity in Cart
- **Method:** PUT /api/ShoppingCart/{userId}/{bookId}
- **Expected:** 200 OK
- **Type:** Positive

---

## Checkout & Orders

### TC_API_015 - Perform Checkout (Valid)
- **Method:** POST /api/CheckOut/{userId}
- **Expected:** 200 OK, Order placed
- **Type:** Positive

### TC_API_016 - Fetch Orders for User
- **Method:** GET /api/Order/{userId}
- **Expected:** 200 OK, List of past orders
- **Type:** Positive

---

## Wishlist

### TC_API_017 - Get Wishlist Items
- **Method:** GET /api/Wishlist/{userId}
- **Expected:** 200 OK, List of items
- **Type:** Positive

### TC_API_018 - Add or Remove Book in Wishlist
- **Method:** POST /api/Wishlist/ToggleWishlist/{userId}/{bookId}
- **Expected:** 200 OK
- **Type:** Positive

### TC_API_019 - Delete Wishlist
- **Method:** DELETE /api/Wishlist/{userId}
- **Expected:** 204 No Content
- **Type:** Positive

---

## User Details

### TC_API_020 - Get User by ID
- **Method:** GET /api/User/{userId}
- **Expected:** 200 OK, User info returned
- **Type:** Positive

### TC_API_021 - Validate Existing Username
- **Method:** GET /api/User/validateUserName/{username}
- **Expected:** 200 OK with a response `true` or `false`
- **Type:** Positive