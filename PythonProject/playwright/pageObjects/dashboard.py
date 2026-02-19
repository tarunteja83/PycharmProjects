from .orderHistory import OrderHistoryPage


class DashboardPage:
    def __init__(self, page):
        self.page = page

    def clickOrders(self):
        self.page.get_by_role("button", name="ORDERS").click()

        Order_History_Page = OrderHistoryPage(self.page)
        return Order_History_Page
