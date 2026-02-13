from playwright.sync_api import Page, expect

class FlipkartFooterPage:
    URL = "https://www.flipkart.com/"
    FOOTER_LOCATOR = "//span[normalize-space()='Flipkart.com']"
    EXPECTED_COLOR = "rgba(0, 0, 0, 0)"

    def __init__(self, page: Page):
        self.page = page
        self.footer_element = page.locator(self.FOOTER_LOCATOR)

    def navigate(self):
        self.page.goto(self.URL)

    def scroll_to_bottom(self):
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        self.page.wait_for_timeout(1000)

    def get_footer_background_color(self):
        return self.footer_element.evaluate("el => window.getComputedStyle(el).backgroundColor")

    def verify_footer_color(self):
        bg_color = self.get_footer_background_color()
        print(f"The background color is: {bg_color}")
        
        # Using Playwright's expect for assertion is better, but sticking to the logic in the original test
        if bg_color == self.EXPECTED_COLOR:
            print("Success: Background color matches!")
        else:
            print(f"Failure: Expected {self.EXPECTED_COLOR}, but got {bg_color}")
            # Raising an error to make the test fail if colors don't match
            raise AssertionError(f"Expected {self.EXPECTED_COLOR}, but got {bg_color}")
