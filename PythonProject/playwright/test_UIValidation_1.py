import logging
import time

import pytest
from playwright.sync_api import Page, expect

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# if not logger.handlers:
#     console = logging.StreamHandler()
#     formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
#     console.setFormatter(formatter)
#     logger.addHandler(console)

logger.info("Automation started")

@pytest.mark.sanity
def test_UIValidationDynamicScript(page:Page):
    logger.info("Automation started")

    #Opening a Browser to open specific website
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    logger.info("Browser Opened with Provided URL")

    #To get the page title
    page.title()
    logger.info("Title has been fetched : " + page.title())

    #To get the fields using labels to provide user creds
    page.get_by_label("Username:").fill("rahulshettyacademy")
    logger.info("Username field has been fetched and Provided value in it")

    page.get_by_label("Password:").fill("Learning@830$3mK2")
    logger.info("Password field has been fetched and Provided value in it")

    #To get the fields using roles to perform actions
    page.get_by_role("combobox").select_option("teach")
    logger.info("Combobox field has been fetched and Provided value in it")

    page.get_by_role("link",name="terms and conditions").click()
    logger.info("Link field has been fetched and selected")

    #To find a fields using locators to perform actions or to enter testdata
    page.locator("#terms").check()
    logger.info("Checkbox field has been fetched and selected")

    page.get_by_role("button",name="Sign In").click()
    logger.info("Button for Signin has been Fetched & clicked")

    product1 = page.locator("app-card").filter(has_text="iphone X")
    logger.info(product1)

    product1.get_by_role("button").click()
    logger.info("Product1 have been added to cart")

    product2 = page.locator("app-card").filter(has_text="Blackberry")
    logger.info(product2)

    product2.get_by_role("button").click()
    logger.info("Product2 have been added to cart")

    page.get_by_text("Checkout").click()
    logger.info("Checkout button has been Fetched & clicked")


    # To perform validations for expected conditions
    expect(page.get_by_text("iphone X")).to_have_count(1)
    logger.info("IPhone X is now checked")

    expect(page.get_by_text("Blackberry")).to_have_count(1)
    logger.info("Blackberry is now checked")

    expect(page.locator(".media-body")).to_have_count(2)
    logger.info("Media body is now checked")

    expect(page.get_by_text("₹. 150000")).to_be_visible()
    logger.info("Amount has been checked")

    expect(page.locator("(//button[normalize-space()='Checkout'])[1]")).to_be_visible()
    logger.info("Checkout button has been clicked")

    page.locator("(//button[normalize-space()='Checkout'])[1]").click()
    logger.info("Checkout button has been clicked")

    expect(page.get_by_text("Please choose your delivery location. ")).to_be_visible()
    logger.info("Please choose your delivery location. ")

    country_input = page.locator("#country")
    logger.info(country_input)

    expect(country_input).to_be_visible()
    logger.info("Country is now checked")

    country_input.type("India")
    logger.info("Value provided to Country field")

    time.sleep(3)
    logger.info("Hard Stopped to load country")

    expect(page.locator("div[class ='suggestions'] ul li a")).to_be_visible()
    logger.info("Country fetched with value provided in Country field")

    page.locator("div[class ='suggestions'] ul li a").click()
    logger.info("Country value populated is selected")

    expect(page.locator("//input[@value='Purchase']")).to_be_visible()
    logger.info("Purchase button is available for selection")

    page.locator("//input[@value='Purchase']").click()
    logger.info("Purchase button is clicked")

    expect(page.locator(".alert.alert-success.alert-dismissible")).to_be_visible()
    logger.info("Product Purchased response received")

    #To provide wait in hardcode
    time.sleep(5)
    logger.info("Hard Stopped to load country")

    # To close the page
    page.close()
    logger.info("Browser Closed")

def test_childTabTest(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as newPage_Info:
        page.locator(".blinkingText").click()
        childtab = newPage_Info.value
        childtab.title()
        print(childtab.title())
        text = childtab.locator(".im-para.red").text_content()
        print(text)
        # Please email us at mentor@rahulshettyacademy.com with below template to receive response
        words = text.split("at")
        print(words)
        email = words[1].strip().split(" ")[0]
        print(email)
        mailid = childtab.locator("a[href='mailto:mentor@rahulshettyacademy.com']").text_content()
        print(mailid)
        assert email == "mentor@rahulshettyacademy.com"
        assert email == mailid


        page.close()

