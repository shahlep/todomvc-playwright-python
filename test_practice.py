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


"""
should clear text input field when an item is added
"""


def test_clear_input_field_after_add(set_up):
    page = set_up
    page.locator('.new-todo').click()
    page.locator('.new-todo').fill('item')
    page.locator('.new-todo').press('Enter')

    expect(page.locator('.new-todo')).to_be_empty()


"""
 Write a test that ensures that a todo can be "completed"
"""


def test_to_check_todo_can_be_completed(set_up):
    page = set_up

    page.locator('.new-todo').click()
    page.locator('.new-todo').fill('item')
    page.locator('.new-todo').press('Enter')
    page.locator('.toggle').click()
    expect(page.locator('.todo-list li')).to_have_class('completed')


"""
Write a test that ensures that the "Clear completed" 
removes all completed todos from the app
"""


def test_clear_all_completed_todos(set_up):
    page = set_up

    page.locator('.new-todo').click()
    page.locator('.new-todo').fill('item')
    page.locator('.new-todo').press('Enter')
    page.locator('.toggle').click()

    page.locator('.clear-completed').click()

    expect(page.locator('.todo-list li')).to_have_count(0)
