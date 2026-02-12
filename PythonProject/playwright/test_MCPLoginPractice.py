import json
import pytest
from playwright.sync_api import Page
from pageObjects.loginPracticePageMCP import LoginPagePractice

# Load credentials from the existing JSON file
with open('C:/Users/USERSS/PycharmProjects/PythonProject/playwright/testdata/credentials.json') as f:
    test_data = json.load(f)
    user_credentials_list = test_data['user_credentials']

@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_login_application(page: Page, user_credentials):
    # Initialize the Page Object
    login_page = LoginPagePractice(page)

    # 1. Login to url
    login_page.navigate()

    # 2. Login using creds from the JSON file
    user_id = user_credentials["userID"]
    user_pwd = user_credentials["userPassword"]
    
    login_page.login(user_id, user_pwd)

    # 3. Verify it is loging by checking the title
    # Added a timeout of 10 seconds to wait for the title to change
    login_page.verify_successful_login(timeout=10000)
    print("Login Successful")