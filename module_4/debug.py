# 4.1 Инструменты отладки(Debug), шаг 4
from playwright.sync_api import expect


def test_todo(page):
    page.goto('https://demo.playwright.dev/todomvc/#/')
    expect(page).to_have_url("https://demo.playwright.dev/todomvc/#/")
    input_field = page.get_by_placeholder('What needs to be done?')
    expect(input_field).to_be_empty()
    input_field.fill("Закончить курс по playwright")
    input_field.press('Enter')
    page.pause()
