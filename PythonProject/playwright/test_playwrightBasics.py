import time

import pytest
from playwright.sync_api import Page, expect, Playwright


def test_playwrightBasics(playwright):
    browse = playwright.chromium.launch(headless=False)
    context = browse.new_context()
    page  = context.new_page()
    page.goto("https://www.google.com/")
    page.title = "Google"
    page.close()


#Page fixture defaults to chromium with headless mode and 1 single context
def test_playwrightShortcut(page:Page):
    page.goto("https://www.google.com/")
    print("Google Page opened")
    page.title = "Google"
    print("Page title Acquired")
    page.close()
    print("Page Closed")

# CSS selector syntax
#--from id-- #id
#--from Class -- .class
def test_coreLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    print("URL opened")
    page.title()
    print(page.title())
    page.get_by_label("Username:").fill("rahulshettyacademy")
    print("Provided user name by getting the field using label")
    page.get_by_label("Password:").fill("learning")
    print("Provided password by getting the field using label")
    page.get_by_role("combobox").select_option("teach")
    print("Selected combobox option by getting the field using role and select option")
    page.get_by_role("link",name="terms and conditions").click()
    print("Selected terms and conditions by clicking the link")
    page.locator("#terms").check()
    print("Checked terms and conditions by clicking the checkbox")
    page.get_by_role("button",name="Sign In").click()
    print("Clicked on sign in button")
    time.sleep(5)
    page.close()
    print("Test ended")

@pytest.mark.sanity
def test_coreLocators1(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    print("URL opened")
    page.title()
    print(page.title())
    page.get_by_label("Username:").fill("rahulshettyacademy")
    print("Provided user name by getting the field using label")
    page.get_by_label("Password:").fill("learning1")
    print("Provided incorrect password by getting the field using label")
    page.get_by_role("combobox").select_option("teach")
    print("Selected combobox option by getting the field using role and select option")
    page.get_by_role("link",name="terms and conditions").click()
    print("Selected terms and conditions by clicking the link")
    page.locator("#terms").check()
    print("Checked terms and conditions by clicking the checkbox")
    page.get_by_role("button",name="Sign In").click()
    print("Clicked on sign in button")
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    print("Error message from screen is Captured")
    time.sleep(5)
    page.close()
    print("Test ended")

def test_firefox_browser(playwright: Playwright):
    firefoxBrowser = playwright.firefox
    browser = firefoxBrowser.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    print("URL opened")
    page.title()
    print(page.title())
    page.get_by_label("Username:").fill("rahulshettyacademy")
    print("Provided user name by getting the field using label")
    page.get_by_label("Password:").fill("learning1")
    print("Provided incorrect password by getting the field using label")
    page.get_by_role("combobox").select_option("teach")
    print("Selected combobox option by getting the field using role and select option")
    page.get_by_role("link", name="terms and conditions").click()
    print("Selected terms and conditions by clicking the link")
    page.locator("#terms").check()
    print("Checked terms and conditions by clicking the checkbox")
    page.get_by_role("button", name="Sign In").click()
    print("Clicked on sign in button")
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    print("Error message from screen is Captured")
    time.sleep(5)
    page.close()
    print("Test ended")