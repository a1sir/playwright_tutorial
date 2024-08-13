# 4.2 Перехват и изменение сетевых запросов. Mocking, шаг 4
from playwright.sync_api import Page, Route, expect


# Модифицировать ответ

# Для подмены ответа используется метод route.fulfill в котором указывается путь до json с подменными данными
def test_mock_tags(page: Page):
    page.route("**/api/tags", lambda route: route.fulfill(path="data.json"))
    page.goto('https://demo.realworld.io/')


# Метод route.fetch выполняет запрос на сервер и получает результат на данный запрос
# С помощью метода route.fulfill и опции json, отправьте запрос с исправленным телом ответа
# В тестовом примере ниже, для выполнения трех этапов mocking создана функция-обработчик handle_route
def test_intercepted(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        json = response.json()
        json["tags"] = ["open", "solutions"]
        route.fulfill(json=json)

    page.route("**/api/tags", handle_route)

    page.goto("https://demo.realworld.io/")
    sidebar = page.locator('css=div.sidebar')
    expect(sidebar.get_by_role('link')).to_contain_text(["open", "solutions"])
