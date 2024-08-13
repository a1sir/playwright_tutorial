# 4.2 Перехват и изменение сетевых запросов. Mocking, шаг 5
from playwright.sync_api import Page, Route, expect

# Имя Alex Sirotin из файла example.har подставляется, но тест почему-то падает
def test_replace_from_har(page):
    page.goto("https://reqres.in/")
    page.route_from_har("example.har")
    users_single = page.locator('li[data-id="users-single"]')
    users_single.click()
    response = page.locator('[data-key="output-response"]')
    expect(response).to_contain_text("Open Solutions")
