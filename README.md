# Project info

## Purpose

I'm enroled in Canadian College of Technology and Business (CCTB) as Software Quality and Test Automation, one of the tools that we learned as part of this course is Selenium.

Recently as effort to learn ReactJs I have developed small application that aggregates and lists products that are on discounts, users can search product by categories filter by price, seller and name to help them find the product that they are looking for. This project was missing autmated UI tests, and this project adds them using Selenium WebDriver. This helps me learn how automated tests are done, help me learn what is required for an app to be QA automatable.
More details on ReactJs application can be found on https://github.com/tanjag88/discounts-aggregator-ui.

# Technology Stack

### Application Environment

React application is deployed to Heroku
https://discaunts-aggregator-ui.herokuapp.com/

### Automation Environment

(Tools, Technologies Used to develop automated tests)

- _IDE:_ PyCharm
- _Automation Framework:_ Selenium Webdriver
- _Language:_ Python 3.9
- _Browser:_ Chrome
- _Source Control:_ Git/GitHub

### Execution Environment

- Jenkins on AWS EC2 Linix instance with SSH-Key based secure connection to GitHub repository to pull and run the selenium scripts
- Local running the tests in PyCharm

### Project Structure

- `baseDiscountAggreagator.py` base class that setup and teardown Selinium WebDriver that is used in aos_tests.py
- `discountAggregatorMethods.py` helper methods used in tests so we do not duplicate them, like navigation to certain part of my app.
- `filtersTestCases.py` all test cases for filters
- `navigationTestCases.py` all test cases for navigation
- `websiteURLs.py` holds url static variables
- `productsData.json` holds information about proructs that I use in tests
