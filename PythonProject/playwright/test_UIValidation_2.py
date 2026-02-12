import time

import pytest
from playwright.sync_api import Page, expect

@pytest.mark.sanity
def test_UIChecks(page : Page):

    #Hide/Display using placeholder
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name = "Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    page.get_by_role("button", name="Show").click()
    expect(page.get_by_placeholder("Hide/Show Example")).not_to_be_hidden()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()


    #Alert Boxes which is not part of HTML
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button", name = "Confirm").click()
    # time.sleep(5)

    # Mouse Hover
    page.locator("#mousehover").hover()
    page.get_by_role("link", name = "Top").click()

    # #Frames Handling
    # page.get_by_role("link", name="Free Access to InterviewQues/ResumeAssistance/Material").click()
    # page.wait_for_load_state("networkidle")
    # pageFrame = page.frame_locator("#google_esf")
    # newLink = pageFrame.locator("//a[@class='new-navbar-highlighter'][normalize-space()='All Access plan']")
    # expect(newLink).to_be_visible(timeout=10000)
    # newLink.click()
    # # expect(pageFrame.locator(".relative.container.mx-auto.px-6.py-20.text-center")).to_contain_text("one Single Subscription")
    # expect(pageFrame.locator("text=one Single Subscription")).to_be_visible()

    #Check the price of rice is equal to 37
    #Identify the price column
    #Identify the Rice row

@pytest.mark.sanity
def test_handleTable(page : Page):
    with page.expect_popup() as newtab_Info:
        page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")
        page.locator(".cart-header-navlink[href='#/offers']").click()
        newtab = newtab_Info.value

        header_locator = newtab.locator("th")
        header_locator.first.wait_for(state="visible")

        priceColVal = None  # Initialize to avoid UnboundLocalError

        # Loop to find the index
        for index in range(header_locator.count()):
            if "Price" in (header_locator.nth(index).text_content() or ""):
                priceColVal = index
                print(f"Column value is {priceColVal}")
                break
        #Safeguard against the column not being found
        if priceColVal is None:
            pytest.fail("Could not find the 'Price' column header")

        #Wait for the specific row to be visible
        itemRow = newtab.locator("tr").filter(has_text="Rice")
        expect(itemRow.locator("td").nth(priceColVal)).to_have_text("37")






