# 🚀 API Test Automation Hero

API Test Automation Hero is a **BDD-based API test automation framework** built using **pytest + pytest-bdd**. This project is an extension of AI-generated BDD test cases that have been finalized and enhanced by QA Engineers.

## 🧪 Tech Stack

This project is built using:

- 🐍 Python
- 🧪 pytest
- 🥒 pytest-bdd
- 🌐 requests
- 📊 allure-pytest

## 🔄 Workflow

The QA automation workflow in this project follows these steps:

1. QA prepares the final **BDD test cases**
2. Writes feature files into the `features/` directory
3. Prepares **test data** inside `fixtures/`
4. Builds API fixtures and assertion logic
5. Implements step definitions and automated execution inside `tests/`
6. Executes tests using `pytest`
7. Generates test reports using **Allure Report**

## ▶️ How to Run Tests

### 1. Install dependencies
`pip install -r requirements.txt`

### 2. Run test execution
`pytest -v`

### 3. Serve Allure Report
`allure serve tests/reports/allure`

## 🎬 Sample Execution
<img width="1920" height="1032" alt="api_automation_demo" src="https://github.com/user-attachments/assets/e320481b-3430-4e87-b091-9e64215ad263" />
