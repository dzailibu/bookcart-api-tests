
# Test Plan – Book Cart API

## 1. Objectives
This test plan outlines the strategy for testing the Book Cart API, 
focusing on the REST API functionality and core user functionalities including registration, login, book operations, 
shopping cart, checkout, and order retrieval.  
Testing efforts will be concentrated on realistic user flows combining multiple endpoints.

## 2. Scope
- REST API endpoints testing
- Real user flow simulations
- Smoke, positive and negative testing

## 3. Approach
- Automated API testing using Python + Pytest + Requests
- POM (SOM-based API layers) + OOP structure
- Test data will be dynamically generated via API calls (e.g., user registration, login)
- API authentication using Bearer JWT for security
- Fixtures for dynamic test data and login
- Logger and Allure (optional) for reporting

## 4. User Flows Tested
1. **Register & Login**
2. **Browse books**
3. **Add book to cart**
4. **Checkout**
5. **Fetch order**
6. **Invalid Input Handling** (e.g., invalid login credentials, missing required fields)


## 5. Tools & Frameworks
- **Language:** Python 3.x
- **HTTP Client:** `requests`
- **Test Framework:** `pytest` (version 7.x)
- **Optional Reporting:** `allure-pytest` for test report generation
- **API Documentation:** Swagger UI - https://bookcart.azurewebsites.net/swagger/index.html

## 6. Execution Strategy
- Authentication will be performed via `POST /api/User/Login` to receive a token
- Token will be used in `Authorization` headers for protected endpoints
- Tests can be executed locally via command line
- For continuous integration, tests can be triggered via a CI pipeline (e.g. Jenkins)

## 7. Reporting
- Logs will be saved to `test_run.log` in the directory where pytest is run.
- Allure HTML report can be used. For this, allure-pytest and Allure CLI has to be installed on the system. 

## 8. Deliverables
- `test_plan.md` (this document)
- `test_cases.md` API test cases
- Automated smoke test suite in Python
- `README.md` with instructions for test execution
- `bug_report.md` Bug report (if applicable)
- **Test Automation Framework** for API testing (repo)
