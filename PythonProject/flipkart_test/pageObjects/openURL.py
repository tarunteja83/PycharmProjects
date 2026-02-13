

class OpenURL:
    def __init__(self, page):
        self.page = page

    def openURL(self, playwright):
        browsers = playwright.chromium.launch(headless=False)
        self.page.goto("https://rahulshettyacademy.com/client")
        pageTitle = self.page.title()
        print(f"Your Page title is: {pageTitle}")


