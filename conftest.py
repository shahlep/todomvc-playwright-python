import pytest
from playwright.sync_api import Playwright, expect


@pytest.fixture(scope='function')
def set_up(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://demo.playwright.dev/todomvc/#/
    page.goto("https://demo.playwright.dev/todomvc/#/")

    yield page
    page.close()

