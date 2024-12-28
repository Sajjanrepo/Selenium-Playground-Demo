Selenium Playground Search Functionality Automation

Overview
---------

This project involves creating Selenium automation scripts in Python to validate the search functionality on the Selenium Playground website. The objective is to ensure that the website's search feature works as expected under different scenarios.


Approach
---------

Understanding Requirements:

Reviewed the detailed instructions provided in the assessment link.

Focused on validating the search functionality with positive, negative, and edge test cases.

Setup:
---------

1) Utilized Selenium WebDriver with Python.

2) Structured the tests using the Pytest framework for easy scalability and maintainability.

3) Followed the Page Object Model (POM) design pattern to separate locators and actions from test scripts.

Test Scenarios: (Total 5 Test cases)
------------------------------------

**** Positive Test Cases ****:

1) Verify that a valid search term returns the expected results.

**** Negative Test Cases ****:

1) Check the behavior for invalid or random search terms.

**** Edge Test Cases ****:

1) Validate search with empty input.

2) Validate search with special characters and extremely long strings.

Prerequisites
----------------
1) Python (version 3.7 or above)

2) Selenium (version 4.x)

3) Pytest (version 7.x)    

4) Latest version of GeckoDriver installed and that it matches your Firefox browser version.

5) Install pytest-html (for html report generation)

6) Pycharm Editor

Practices Followed:
----------------------

1) Used descriptive and modular functions for readability and reusability.

2) Implemented assertions to validate search results accurately.

3) Added explicit waits to ensure stability and avoid flaky tests.

4) Maintained logs for better debugging and tracking of test execution.

5) Included parameterized test cases for varied inputs.

6) Followed PEP8 coding standards for Python.

Setup Instructions
-----------------------
1) Clone the repository:   git clone https://github.com/Sajjanrepo/Selenium-Playground-Demo.git
2) cd repository_folder
3) Install the dependencies: pip install -r requirements.txt

Running the Script:
----------------------
1) run test cases using Pytest:
   pytest -s -v .\testcases\qa_selenium_test.py

