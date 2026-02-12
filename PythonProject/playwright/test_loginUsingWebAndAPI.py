import json
import time

import pytest

from pageObjects.login import LoginPage

# file = open('testData.txt')
# second_line = file.readlines()[1]
# print(second_line)
# pytest --browser_name chrome -m sanity -n 3 --tracing on --html=report.html
# pytest -m sanity -n 3 --tracing on --html=report.html
# pytest --browser_name chrome -m sanity -n 3 --tracing retain-on-failure --html=report.html
#Jenkins -- pytest --browser_name "$browser" -m sanity -n 3 --tracing on --html=report.html

# Json file -> util -> Access into test.
with open('C:/Users/USERSS/PycharmProjects/PythonProject/playwright/testdata/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data['user_credentials']

@pytest.mark.sanity
@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_login_data(playwright: Playwright, browserInstance, user_credentials):
    user_id = user_credentials["userID"]
    user_pwd = user_credentials["userPassword"]

    print(user_credentials)
    print(user_credentials_list)
    # Login Page objects
    login_page = LoginPage(browserInstance)
    login_page.openPage()
    dashboard_page = login_page.login(user_id , user_pwd)
    # Dashboard Page objects accessing from login
    orderhistory_page = dashboard_page.clickOrders()
    orderhistory_page.selectOrders()

    browserInstance.locator("//button[normalize-space()='Sign Out']").click()
    time.sleep(1)


from playwright.sync_api import Playwright, expect
from utils.apiBaseFramework import APIUtils

@pytest.mark.sanity
@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_session_storage(playwright: Playwright, user_credentials):
    api_utils = APIUtils()
    getToken = api_utils.getToken(playwright)
    # getToken = api_utils.getToken(playwright, user_credentials)
    browserLaunch = playwright.chromium.launch(headless=False)
    context = browserLaunch.new_context()
    # Script to inject token in session local storage
    context.add_init_script(f"""localStorage.setItem('token','{getToken}')""")
    page = context.new_page()
    ##To add API clause using before classes
    time.sleep(5)
    page.goto("https://rahulshettyacademy.com/client")
    time.sleep(5)
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()

# file.close()
