from playwright.sync_api import Playwright

ordersPayload = {"orders": [{"country": "India", "productOrderedId": "68a961459320a140fe1ca57a"}]}

class APIUtils:

    def getToken(self,playwright: Playwright, user_credentials):
        user_id = user_credentials['userID']
        user_pwd = user_credentials['userPassword']
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/auth/login",
                                 data={"userEmail": user_id, "userPassword": user_pwd})
        assert response.ok
        print(response.json())
        responseBody = response.json()
        print(responseBody)
        return responseBody["token"]



    def createOrder(self,playwright: Playwright, user_credentials):
        token = self.getToken(playwright,user_credentials)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                 data=ordersPayload,
                                 headers={"Content-Type": "application/json",
                                          "Authorization": token})
        print(response.json())
