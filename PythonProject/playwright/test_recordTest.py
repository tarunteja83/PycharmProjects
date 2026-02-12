import time

import pytest
from playwright.sync_api import Playwright

@pytest.mark.sanity
def test_recordPlayTest(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")
    time.sleep(1)
    page.locator("div:nth-child(11) > .stepper-input > .increment").click()
    time.sleep(1)
    page.locator("div:nth-child(11) > .stepper-input > .increment").click()
    time.sleep(1)
    page.locator("div:nth-child(11) > .product-action > button").click()
    time.sleep(1)
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Top Deals").click()
        time.sleep(1)
    page1 = page1_info.value
    time.sleep(1)
    page1.get_by_role("cell", name="37").nth(1).click()
    time.sleep(1)
    page1.get_by_role("button", name="4").click()
    time.sleep(1)
    page1.get_by_role("button", name="First").click()
    time.sleep(1)
    page.get_by_role("button", name="ADD TO CART").nth(1).click()
    time.sleep(1)
    page.locator("div:nth-child(8) > .product-action > button").click()
    time.sleep(1)
    page.get_by_role("link", name="Cart").click()
    time.sleep(1)
    page.get_by_role("list").click()
    time.sleep(1)
    page.get_by_role("button", name="PROCEED TO CHECKOUT").click()
    time.sleep(1)
    page.get_by_role("button", name="Place Order").click()
    time.sleep(1)
    page.get_by_role("combobox").select_option("India")
    time.sleep(1)
    page.get_by_role("checkbox").check()
    time.sleep(1)
    page.get_by_role("button", name="Proceed").click()
    time.sleep(3)
    page.get_by_role("link", name="Home").click()
    time.sleep(1)

    # ---------------------
    context.close()
    browser.close()