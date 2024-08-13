# 3.3 Проверки (Assertions), шаги 3 - 6
from playwright.sync_api import expect


# Тест проверки заполнения формы
# 1. открыть https://demo.playwright.dev/todomvc/#/
# 2. проверить что открыт корректный url
# 3. найти поле ввода задачи
# 4. проверить что оно пустое
# 5. ввести задачу номер один
# 6. ввести задачу номер два
# 7. проверить что количество задач в списке равно двум
# 8. отметить одну задачу выполненной
# 9. проверить что эта задача отмечена выполненной

def test_todo(page):
    page.goto('https://demo.playwright.dev/todomvc/#/')
    expect(page).to_have_url("https://demo.playwright.dev/todomvc/#/")
    input_field = page.get_by_placeholder('What needs to be done?')
    expect(input_field).to_be_empty()
    input_field.fill("Закончить курс по playwright")
    input_field.press('Enter')
    input_field.fill("Добавить в резюме, что умею автоматизировать")
    input_field.press('Enter')
    todo_item = page.get_by_test_id('todo-item')
    expect(todo_item).to_have_count(2)
    todo_item.get_by_role('checkbox').nth(0).click()
    expect(todo_item.nth(0)).to_have_class('completed')
