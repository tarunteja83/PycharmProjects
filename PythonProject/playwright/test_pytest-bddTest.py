import time

import pytest
from pytest_bdd import given, when, then, parsers, scenarios

from pageObjects.login import LoginPage
from pageObjects.logout import LogoutPage
from utils.apiBaseFramework import APIUtils

# To execute from terminal
# pytest test_pytest-bddTest.py --browser_name chrome --tracing on --html=report.html

scenarios('features/orderTransaction.feature')

@pytest.fixture
def shared_data():
    return{}

@given(parsers.parse('place the item order with {username} and {password}'))
def place_item_order(playwright, username, password, shared_data):
    user_credentials = {}
    user_credentials['userID'] = username
    user_credentials['userPassword'] = password
    # api_utils = APIUtils()
    # getToken = api_utils.getToken(playwright, user_credentials)
    # shared_data['getToken'] = getToken

@given('the user is on landing page')
def user_in_landing_page(browserInstance, shared_data):
    login_page = LoginPage(browserInstance)
    login_page.openPage()
    shared_data['login_page'] = login_page
    time.sleep(1)

@when (parsers.parse('I login to the application {username} and {password}'))
def login_to_application(username, password, shared_data):
    login_page = shared_data['login_page']
    dashboard_page = login_page.login(username, password)
    shared_data['dashboard_page'] = dashboard_page
    time.sleep(1)

@when ('navigate to orders page')
def navigate_to_orders_page(shared_data):
    dashboard_page = shared_data['dashboard_page']
    orderhistory_page = dashboard_page.clickOrders()
    shared_data['orderhistory_page'] = orderhistory_page
    time.sleep(1)

@when ('select the orderid')
def select_order_id(shared_data):
    orderhistory_page = shared_data['orderhistory_page']
    orderhistory_page.selectOrders()
    time.sleep(1)

@then ('Signout the user')
def user_signout(browserInstance,shared_data):
    logout_page = LogoutPage(browserInstance)
    logout_page.logout()
    shared_data['logout_page'] = logout_page
    time.sleep(1)
