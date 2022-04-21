import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope='function')
def set_up(playwright: Playwright) -> None:
    browser = playwright.webkit.launch(headless=True)
    context = browser.new_context(viewport={'width': 375, 'height': 630})
    page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/#/")

    return page
    page.close()
