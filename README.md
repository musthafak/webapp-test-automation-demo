# Trello WebApp Test Automation Demo

## Introduction

This project serves as a demonstration of automating the frontend and backend testing for Trello, a popular online tool used for project management and collaboration. The main goal of this project is to showcase the automation techniques for testing Trello's web application.

To achieve this, we have chosen to utilize the Python Behave framework, which follows the Behavior-Driven Development (BDD) approach. Behave allows us to write test scenarios in a human-readable format using the Gherkin language, making it easier for both technical and non-technical stakeholders to understand the test cases.

We use Selenium, a powerful web automation tool, integrated with the Behave framework for frontend automation. Following the Page Object Model (POM) design pattern, we organize web pages as separate classes. Each class represents a specific page or component, encapsulating elements and actions within methods. This enhances maintainability and reusability of test scripts, allowing efficient automation of Trello's frontend and validation of expected behaviors.

In addition to the frontend testing, we have also implemented backend test cases using Behave and Python. These test cases focus on the Trello Boards REST API, allowing us to programmatically interact with the backend services of Trello. By sending HTTP requests and verifying the responses, we can ensure that the backend functionalities, such as creating boards, viewing board details, updating boards, and deleting boards, are working as expected.

By combining the power of Behave, Selenium, and Python, this project demonstrates an end-to-end approach to automating both frontend and backend testing for a web application like Trello. The code and test cases provided serve as a reference for other QA engineers and test automation engineers looking to automate similar web applications. Additionally, we containerized this project using Docker to ensure easy setup and portability across different environments.

## Test Cases

Trello is a feature-rich application with a wide range of functionalities catering to project management and collaboration needs. Given its extensive feature set, it's essential to thoroughly test both the frontend and backend to ensure the application works as expected and delivers a seamless user experience.

Frontend testing is crucial as it involves verifying how users interact with the application's user interface (UI). It covers a myriad of scenarios, from basic interactions like creating boards and lists to more complex operations like adding cards, archiving items, and validating error messages. As the application evolves and new features are added, the number of frontend test cases can grow significantly, reaching potentially hundreds of test scenarios.

Similarly, backend testing is vital to validate the application's server-side functionality and API interactions. Backend test cases encompass verifying the correctness of data storage, handling data retrieval and updates, authentication mechanisms, and more. Ensuring the integrity and security of data processing requires thorough testing of backend functionalities.

In this project, I have included a subset of Trello boards test cases for demonstration purposes, showcasing the automation of key frontend and backend scenarios. Although the presented test cases provide a glimpse into the testing approach, the actual test suite for a comprehensive Trello application would contain numerous additional scenarios, encompassing the full range of features and user interactions.

### Backend Test Cases

```gherkin
Feature: Trello Boards REST API

  Scenario: Create a Trello board
    Given I have a valid API key and token
    When I send a POST request to "/boards" with the payload:
      """
      {
        "name": "Project A"
      }
      """
    Then the response status code should be 200
    And the response body should contain the board ID
    And the board should be created successfully

  Scenario: View a Trello board
    Given I have a valid API key and token
    And I have a board ID
    When I send a GET request to "/boards/{boardId}"
    Then the response status code should be 200
    And the response body should contain the board details

  Scenario: Update a Trello board
    Given I have a valid API key and token
    And I have a board ID
    When I send a PUT request to "/boards/{boardId}" with the payload:
      """
      {
        "name": "Project A - Updated"
      }
      """
    Then the response status code should be 200
    And the board name should be updated to "Project A - Updated"

  Scenario: Delete a Trello board
    Given I have a valid API key and token
    And I have a board ID
    When I send a DELETE request to "/boards/{boardId}"
    Then the response status code should be 200
    And the board should be deleted successfully

  Scenario: Attempt to create a Trello board without a name
    Given I have a valid API key and token
    When I send a POST request to "/boards" with the payload:
      """
      {
        "name": ""
      }
      """
    Then the response status code should be 400
    And the response body should contain "invalid value"

  Scenario: Attempt to view a non-existing Trello board
    Given I have a non-existing board ID
    When I send a GET request to "/boards/{nonExistingBoardId}"
    Then the response status code should be 400
    And the response body should contain "invalid id"

  Scenario: Attempt to update a non-existing Trello board
    Given I have a non-existing board ID
    When I send a PUT request to "/boards/{nonExistingBoardId}" with the payload:
      """
      {
        "name": "Project A - Updated"
      }
      """
    Then the response status code should be 400
    And the response body should contain "invalid id"

  Scenario: Attempt to delete a non-existing Trello board
    Given I have a non-existing board ID
    When I send a DELETE request to "/boards/{nonExistingBoardId}"
    Then the response status code should be 400
    And the response body should contain "invalid id"
```

### Frontend Test Cases

```gherkin
Feature: Trello Board Management

  Scenario: Create a Trello board
    Given I am on the Trello homepage
    When I click on create button
    And I select the board option
    And I enter the board name as "Project A"
    And I click on create board button
    Then I should see a new board with the name "Project A"
    And I have "3" lists on the board

  Scenario: Archive a list on Trello board
    Given I am on the Trello homepage
    And I create a board with name "Project B"
    And I have "3" lists on the board
    When I archive first list item
    Then I have "2" lists on the board

  Scenario: Delete a board on Trello
    Given I am on the Trello homepage
    And I create a board with name "Project C"
    When I permanently delete the board
    Then I dont have "Project C" board in my workspace
```

## Running the Tests

### Prerequisites

To run the frontend and backend tests written in Python, follow these steps to set up the test environment:

1. **Install Python:**
   Ensure Python 3.8+ is installed on your machine. If you don't have Python installed, download and install it from the official Python website (https://www.python.org/downloads/).
2. **Trello Account:**
   To run the tests against the Trello application, you'll need a Trello account. If you don't have one, you can register for free at https://trello.com/signup (A test account credentials are given in the `configs/test_environment.json` file, feel free to update it).
3. **Trello API Key and Token:**
   Once you have a Trello account, log in, and then access your API key and token from the Trello developer website (https://developers.trello.com/). These credentials will be used to authenticate your test scripts with the Trello API (A test account credentials are given in the `configs/test_environment.json` file, feel free to update it).
4. **Web Driver:**
   Selenium requires a web driver to interact with the browser. Depending on your preferred browser, download the corresponding web driver:
   - Chrome: ChromeDriver (https://sites.google.com/a/chromium.org/chromedriver/downloads)
   - Firefox: GeckoDriver (https://github.com/mozilla/geckodriver/releases)
   Ensure the web driver is in your system's PATH or specify its location in the test scripts.

> You can run the tests inside a docker container, follow instructions in the next session.

### Run the Tests

1. **Clone the Repository:**
   Clone the test automation repository to your local machine using Git. Open a terminal or command prompt and run the following command:
   ```
   git clone https://github.com/musthafak/webapp-test-automation-demo.git
   ```

2. **Install Dependencies:**
   Navigate to the root directory of the cloned repository and install the required dependencies using pip and the `requirements.txt` file. Run the following command:
   ```
   cd webapp-test-automation-demo
   python -m venv .venv && . .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Update Config File:**
   Update the configuration file `configs/test_environment.json` in the test directory to manage test environment settings, such as the Trello email, password, API key, token, base URLs, and browser configurations. Supported browsers are firefox, edge and chrome.

4. **Execute Tests:**
   Execute the automated test scripts by running following commands
   ```
   # Backend tests
   behave features/backend

   # Frontend tests
   behave features/frontend
   ```

### Test Reports

* To generate an HTML test report with screenshots on test failure, use the following command:
  ```
  # Backend tests
  behave features/backend -f behave_html_formatter:HTMLFormatter -o report.html

  # Frontend tests
  behave features/frontend -f behave_html_formatter:HTMLFormatter -o report.html
  ```

> You can also generate [Allure Python](https://github.com/allure-framework/allure-python) reports using Allure Python for attractive and interactive HTML reports with detailed test execution insights.

### Run Inside Docker

To execute these tests within a Docker container, follow these steps:

* **Build Docker Image:**
  Build the Docker image using the provided Dockerfile in the `automation` directory with the following command:
  ```
  docker build -t <image name> -f automation/Dockerfile .
  ```

* **Run Tests:**
  Run the tests inside the Docker container using the following command:
  ```
  docker run --rm -it <image name>
  ```

* **Generate Report:**
  To generate a report, use Docker volume mounting to map a local directory to the container's directory. This allows the report files to be saved on the host machine:
  ```
  docker run --privileged --rm -it -v $(pwd)/reports:/workspace/reports <image name>
  . .venv/bin/activate
  behave features/backend -f behave_html_formatter:HTMLFormatter -o reports/report.html
  ```
  OR
  ```
  docker run --privileged --rm -it -v $(pwd)/reports:/workspace/reports <image name> -c '. .venv/bin/activate; behave features/backend -f behave_html_formatter:HTMLFormatter -o reports/report.html'
  ```

> This Docker image can also be utilized in CI/CD pipelines to automate test execution and report generation for seamless integration into your continuous integration and deployment processes.
