from playwright.sync_api import expect
from pytest import mark


@mark.home
@mark.odd
def test_url_page_is_working(set_up):
    page = set_up
    # Add 5 tods and check the counts
    items = ['one', 'two', 'three', 'four', 'five']
    for item in items:
        page.click('.new-todo')
        page.fill('.new-todo', item)
        page.locator('.new-todo').press('Enter')
    number = page.locator('.todo-list li').count()
    expect(page.locator('.todo-list li')).to_have_count(number)


"""
Write a test that asserts that the input field
is focused automatically when the app is first loaded.
"""

@mark.home
@mark.even
def test_focus_on_todo_input_field(set_up):
    page = set_up
    expect(page.locator('.new-todo')).to_be_focused()


"""
should clear text input field when an item is added
"""


@mark.home
@mark.odd
def test_clear_input_field_after_add(set_up):
    page = set_up
    page.click('.new-todo')
    page.fill('.new-todo', 'item')
    page.locator('.new-todo').press('Enter')

    expect(page.locator('.new-todo')).to_be_empty()


"""
 Write a test that ensures that a todo can be "completed"
"""


@mark.home
@mark.even
def test_to_check_todo_can_be_completed(set_up):
    page = set_up

    page.click('.new-todo')
    page.fill('.new-todo', 'item')
    page.locator('.new-todo').press('Enter')
    page.click('.toggle')
    expect(page.locator('.todo-list li')).to_have_class('completed')


"""
Write a test that ensures that the "Clear completed" 
removes all completed todos from the app
"""


@mark.home
@mark.odd
def test_clear_all_completed_todos(set_up):
    page = set_up

    page.click('.new-todo')
    page.fill('.new-todo', 'item')
    page.locator('.new-todo').press('Enter')
    page.click('.toggle')

    page.click('.clear-completed')
    number = page.locator('.todo-list li').count()
    expect(page.locator('.todo-list li')).to_have_count(number)


"""
Write a test that ensures that you can edit a todo
"""


@mark.home
@mark.even
def test_can_edit_a_todo(set_up):
    page = set_up

    page.click('.new-todo')
    page.fill('.new-todo', 'item')
    page.locator('.new-todo').press('Enter')

    page.dblclick('.todo-list label')

    page.fill('.edit', 'edited item')
    page.locator('.edit').press('Enter')

    expect(page.locator('.todo-list li')).to_have_text('edited item')


"""
 Write a test that ensures that the app counts the correct number of todos
 left to be completed, i.e "3 items left" in the bottom left corner.
"""


@mark.home
@mark.odd
def test_count_number_of_todo_left_to_complete(set_up):
    page = set_up

    items = ['one', 'two', 'three', 'four', 'five', 'six']
    for item in items:
        page.click('.new-todo')
        page.fill('.new-todo', item)
        page.locator('.new-todo').press('Enter')

    expect(page.locator('.todo-count')).to_have_text('6 items left')


"""
Write a test that ensures that the todos are persisted in the app
after the browser refreshes the page
"""


@mark.home
@mark.even
def test_page_reload_and_persist(set_up):
    page = set_up

    items = ['one', 'two', 'three', 'four', 'five']
    for item in items:
        page.click('.new-todo')
        page.fill('.new-todo', item)
        page.locator('.new-todo').press('Enter')
    number = page.locator('.todo-list li').count()
    expect(page.locator('.todo-list li')).to_have_count(number)

    page.reload()

    expect(page.locator('.todo-list li')).to_have_count(number)


"""
Write a test that ensures that only the completed todos are
displayed when the "Completed" button is clicked at the bottom
"""


@mark.home
@mark.odd
def test_display_only_completed_todos(set_up):
    page = set_up

    page.click('.new-todo')
    page.fill('.new-todo', 'item')
    page.locator('.new-todo').press('Enter')
    page.click('.toggle')

    page.click('.selected')
    number = page.locator('.todo-list li').count()
    expect(page.locator('.todo-list li')).to_have_count(number)
