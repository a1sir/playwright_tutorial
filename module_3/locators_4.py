# Код со страницы 3.1 Локаторы(Locators), шаг 11
# Работа с несколькими элементами


# вариант перебора нужных элементов в цикле
def test1(page):
    page.goto('https://zimaev.github.io/checks-radios/')
    checkbox = page.locator("input")
    for i in range(checkbox.count()):
        checkbox.nth(i).click()

# вариант с методом playwright locator.all() для перебора всех совпадающих элементов
def test2(page):
    page.goto('https://zimaev.github.io/checks-radios/')
    checkboxes = page.locator("input")
    for checkbox in checkboxes.all():
        checkbox.check()
