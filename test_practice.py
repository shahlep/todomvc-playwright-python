from playwright.sync_api import Playwright, sync_playwright, expect
import pytest


def test_url_page_is_working(set_up):
    page = set_up
    # Add 5 tods and check the counts
    items = ['one', 'two', 'three', 'four', 'five']
    for item in items:
        page.locator('.new-todo').click()
        page.locator('.new-todo').fill(item)
        page.locator('.new-todo').press('Enter')

    expect(page.locator('.todo-list li')).to_have_count(5)


"""
Write a test that asserts that the input field
is focused automatically when the app is first loaded.
"""


def test_focus_on_todo_input_field(set_up):
    page = set_up
    assert page.locator('.new-todo').is_editable()
