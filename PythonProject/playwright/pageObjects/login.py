import time

from .dashboard import DashboardPage


class LoginPage:
    def __init__(self, page):
        self.page = page

    def openPage(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def login(self , user_id , user_pwd):
        time.sleep(1)
        self.page.get_by_placeholder("email@example.com").fill(user_id)
        time.sleep(1)
        self.page.get_by_placeholder("enter your passsword").fill(user_pwd)
        time.sleep(1)
        self.page.get_by_role("button", name="Login").click()
        time.sleep(1)
        dashboard_page = DashboardPage(self.page)
        return dashboard_page