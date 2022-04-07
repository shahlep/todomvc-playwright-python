from playwright.sync_api import Playwright, sync_playwright, expect
import pytest


def test_url_page_is_working(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://demo.playwright.dev/todomvc/#/
    page.goto("https://demo.playwright.dev/todomvc/#/")

    # ---------------------
    # Add 5 tods and check the counts
    page.locator('.new-todo').click()
    page.locator('.new-todo').fill('one')
    page.locator('.new-todo').press('Enter')
    page.locator('.new-todo').fill('two')
    page.locator('.new-todo').press('Enter')
    page.locator('.new-todo').fill('three')
    page.locator('.new-todo').press('Enter')
    page.locator('.new-todo').fill('four')
    page.locator('.new-todo').press('Enter')
    page.locator('.new-todo').fill('five')
    page.locator('.new-todo').press('Enter')

    expect(page.locator('.todo-list li')).to_have_count(5)

    context.close()
    browser.close()
