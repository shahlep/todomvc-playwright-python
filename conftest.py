import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope='function')
def set_up(playwright: Playwright) -> None:
    browser = playwright.webkit.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/#/")

    yield page
    page.close()

