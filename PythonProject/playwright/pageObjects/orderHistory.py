class OrderHistoryPage():

    def __init__(self, page):
        self.page = page

    def selectOrders(self):
        self.page.get_by_role("button", name="ORDERS").click()