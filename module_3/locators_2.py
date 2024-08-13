# Код со страницы 3.1 Локаторы(Locators), шаг 9
# Локатор locator.and_

from playwright.sync_api import Playwright, sync_playwright

def test_locator_and(page):
    page.goto("https://zimaev.github.io/locatorand/")
    selector = page.get_by_role("button", name="Sing up").and_(page.get_by_title("Sing up today"))
    selector.click()