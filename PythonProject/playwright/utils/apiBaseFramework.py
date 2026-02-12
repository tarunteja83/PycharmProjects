from playwright.sync_api import Playwright

ordersPayload = {"orders": [{"country": "India", "productOrderedId": "68a961459320a140fe1ca57a"}]}

class APIUtils:

    def getToken(self,playwright: Playwright):

        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/auth/login",
                                 data={"userEmail": "ramu.ramana@gmail.com", "userPassword": "Iamking@000"})
        assert response.ok
        print(response.json())
        responseBody = response.json()
        print(responseBody)
        return responseBody["token"]



    def createOrder(self,playwright: Playwright):
        token = self.getToken(playwright)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                 data=ordersPayload,
                                 headers={"Content-Type": "application/json",
                                          "Authorization": token})
        print(response.json())
