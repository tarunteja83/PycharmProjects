import pytest
from playwright.sync_api import sync_playwright, Playwright, Page


@pytest.mark.sanity
def test_flipkartFooterColour(playwright):
        browsers = playwright.chromium.launch(headless=False)
        context = browsers.new_context()
        page = context.new_page()
        page.goto("https://www.flipkart.com/")

        pageTitle = page.title()
        print(pageTitle)

        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

        page.wait_for_timeout(1000)

        footerElement = page.locator("//span[normalize-space()='Flipkart.com']")

        bgg_colour = footerElement.evaluate("el => window.getComputedStyle(el).backgroundColor")

        print(f"The background color is: {bgg_colour}")

        expected_colors = "rgba(0, 0, 0, 0)"

        if bgg_colour == expected_colors:
            print("Success: Background color matches!")
        else:
            print(f"Failure: Expected {expected_colors}, but got {bgg_colour}")

        page.close()

@pytest.mark.sanity
def test_flipRun(playwright):
    # Launch browser
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # 1. Load the website
    page.goto("https://www.flipkart.com")

    # 2. Scroll to the bottom
    # window.scrollTo(0, document.body.scrollHeight) ensures we hit the floor
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    # Give a tiny buffer for any lazy-loading elements
    page.wait_for_timeout(1000)

    # 3. Target the last component
    # We'll assume the last component is a <footer> tag or has a specific ID
    last_element = page.locator("//span[normalize-space()='Flipkart.com']")

    # 4. Extract the background color
    # Note: Browsers usually return color in 'rgb(r, g, b)' or 'rgba' format
    bg_color = last_element.evaluate(
        "el => window.getComputedStyle(el).backgroundColor"
    )

    print(f"The background color is: {bg_color}")

    # 5. Assertion (Checking if it matches expected color)
    expected_color = "rgba(0, 0, 0, 0)"
    if bg_color == expected_color:
        print("Success: Background color matches!")
    else:
        print(f"Failure: Expected {expected_color}, but got {bg_color}")

    browser.close()


with sync_playwright() as playwright:
    test_flipRun(playwright)

