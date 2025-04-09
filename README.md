# Book Cart API Automation

This repo contains API automation for the Book Cart system.  
[Book Cart API Swagger Documentation](https://bookcart.azurewebsites.net/swagger/index.html)

---

## Tech Stack

- **Python 3.x**
- **Pytest** for testing
- **Requests** for HTTP requests
- **Python Dotenv** for managing `.env` configuration
- **Logging** for test result and status tracking
- **Page Object Model (SOM-based API)** based API layers for better maintainability
- **Object-Oriented Programming (OOP)** principles for code structure and reusability

---

## Folder Structure

```
book_cart_automation/ 
│ 
├── api/             # API wrapper classes (UserAPI, BookAPI, etc.) 
├── config/          # config.py and .env file 
├── docs/            # Documentation: test_plan.md, test_cases.md, etc. 
├── tests/           # Test files and conftest.py 
├── utils/           # Logging utility, retry mechanism 
├── requirements.txt # Dependencies 
└── README.md        # This file
```

---

## Auth Details

- **Authentication**: Bearer token (JWT) is used for authorization.
- The token is dynamically generated by registering and logging in a test user via the `/api/User` and `/api/Login` endpoints.
- Sensitive data, such as the base URL and token (if needed), are managed via the `.env` file.

---

## Setup Instructions

### 1. Clone the Repo & Navigate

```bash
git clone https://github.com/dzailibu/book_cart_automation.git
cd book_cart_automation
```

### 2. Create Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## How to Run Tests

Run all tests:

```bash
pytest -v tests/
```

### Run Smoke Tests Only

```bash
pytest -v -m smoke
```

---

## Test Logs

Logs are saved to `test_run.log` in the directory where pytest is run.

---

## Test Types

- **Smoke Tests**: Core user journey (Login → Add to cart → Checkout → View Orders).
- **Positive Tests**: Valid input expected to succeed.
- **Negative Tests**: Invalid input, missing fields, or incorrect auth.

---

## Documentation Included

- `docs/test_plan.md`
- `docs/test_cases.md`
- `docs/smoke_test_cases.md`
- `README.md` (you’re reading it 😊)

---

## Limitations

Currently, the API does not support user deletion, so the registered test users will remain in the system after test completion.

---

## To-Do

- **Request an endpoint from the API team** for user deactivation or deletion, allowing us to clean up test data after each test run (teardown).
- **Implement better user management**: e.g., reuse or create unique test users to reduce potential clutter in the system.
- **Implement `pytest_runtest_makereport`**: Capture and log the status (pass/fail) for each individual test.
- **Implement `pytest_sessionfinish`**: Capture and log a summary of the entire test session’s outcome.
- **Update Logging Configuration**: Ensure the logs contain enough information (test name, outcome, failure reason) for easy analysis and reporting.

---

### Additional Notes

- **Test Strategy**: The tests are designed to validate core API functionality and ensure smooth operation in key user flows.
- **User Management**: Due to API limitations, user deletion is not supported. We plan to address this in future iterations.
