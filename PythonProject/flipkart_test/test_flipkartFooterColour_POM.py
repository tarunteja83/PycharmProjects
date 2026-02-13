import pytest
from playwright.sync_api import Page
from pageObjects.flipkartFooterPage import FlipkartFooterPage

@pytest.mark.sanity
def test_flipkart_footer_colour_pom(page: Page):
    # Initialize the Page Object
    flipkart_page = FlipkartFooterPage(page)

    # 1. Load the website
    flipkart_page.navigate()

    # 2. Scroll to the bottom
    flipkart_page.scroll_to_bottom()

    # 3. Verify footer color
    flipkart_page.verify_footer_color()
