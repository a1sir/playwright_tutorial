# Код со страницы 2.2 Первый тест, шаг 2, pytest-playwright
# с релизованной фикстурой

# Запуск теста с параметром --headed отобразит окно браузера и выполняемые в нем действия
# pytest --headed test_todo_2.py

def test_add_todo(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")
