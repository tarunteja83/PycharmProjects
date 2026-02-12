from .login import LoginPage


class LogoutPage:

    def __init__(self, page):
        self.page = page

    def logout(self):
        self.page.locator("//button[normalize-space()='Sign Out']").click()

        login_Page = LoginPage(self.page)
        return login_Page