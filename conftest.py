import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope='function')
def set_up(playwright: Playwright) -> None:
    browser = playwright.webkit.launch(headless=True)
    sizes = [{'width': 375, 'height': 630}, {'width': 1024, 'height': 860}, {'width': 760, 'height': 630}]
    for size in sizes:
        context = browser.new_context(viewport=size)
        page = context.new_page()
        page.goto("https://demo.playwright.dev/todomvc/#/")

    return page
    page.close()
