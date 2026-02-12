from playwright.sync_api import Page, expect

class LoginPagePractice:
    URL = "https://rahulshettyacademy.com/loginpagePractise/"
    USERNAME_FIELD = "Username:"
    PASSWORD_FIELD = "Password:"
    TERMS_CHECKBOX = "#terms"
    SIGNIN_BUTTON = "Sign In"
    EXPECTED_SUCCESS_TITLE = "ProtoCommerce"

    def __init__(self, page: Page):
        self.page = page
        self.username_locator = page.get_by_label(self.USERNAME_FIELD)
        self.password_locator = page.get_by_label(self.PASSWORD_FIELD)
        self.terms_locator = page.locator(self.TERMS_CHECKBOX)
        self.signin_locator = page.get_by_role("button", name=self.SIGNIN_BUTTON)

    def navigate(self):
        self.page.goto(self.URL)

    def login(self, username, password):
        self.username_locator.fill(username)
        self.password_locator.fill(password)
        self.terms_locator.check()
        self.signin_locator.click()

    def verify_successful_login(self, timeout=10000):
        expect(self.page).to_have_title(self.EXPECTED_SUCCESS_TITLE, timeout=timeout)