import json
import time

import pytest
# file = open('testData.txt')
# second_line = file.readlines()[1]
# print(second_line)

from playwright.sync_api import Playwright, expect
# Gemini commented
# from pytest_playwright.pytest_playwright import new_context

from utils.apiBase import APIUtils

# Gemini added: Load credentials
with open('C:/Users/USERSS/PycharmProjects/PythonProject/playwright/testdata/credentials.json') as f:
    test_data = json.load(f)
    user_credentials_list = test_data['user_credentials']

@pytest.mark.sanity
# Gemini added: Parametrize the test
@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_session_storage(playwright: Playwright, user_credentials):
    api_utils = APIUtils()
    # Gemini commented
    # token = api_utils.getToken(playwright)
    token = api_utils.getToken(playwright, user_credentials)
    browserLaunch = playwright.chromium.launch(headless=True)
    context = browserLaunch.new_context()
    # Script to inject token in session local storage
    context.add_init_script(f"""localStorage.setItem('token','{token}')""")
    time.sleep(5)
    print(token)
    page = context.new_page()

    ##To add API clause using before classes
    page.goto("https://rahulshettyacademy.com/client")
    time.sleep(5)
    page.get_by_role("button", name="ORDERS").click()
    time.sleep(3)
    expect(page.get_by_text("Your Orders")).to_be_visible()
    time.sleep(3)

# file.close()