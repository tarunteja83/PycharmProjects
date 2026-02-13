import pytest


@pytest.fixture(scope='session')
def browserInstance(playwright, request):
    browser_name = (request.config.getoption('browser_name') or "chrome").lower()

    browserLaunch = None

    if browser_name == 'chrome':
        browserLaunch = playwright.chromium.launch(headless=True)
    elif browser_name == 'firefox':
        browserLaunch = playwright.firefox.launch(headless=True)
    else:
        # Default fallback so the test doesn't crash
        browserLaunch = playwright.chromium.launch(headless=True)

    context = browserLaunch.new_context()
    page = context.new_page()
    yield page
    context.close()
    browserLaunch.close()