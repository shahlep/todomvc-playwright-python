import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope='function')
def set_up(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/#/")

    return page
    page.close()

