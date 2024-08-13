# Код со страницы 3.1 Локаторы(Locators), шаг 10

# Цепочка локаторов
# Вариант 1
def test_chain(page):
    page.goto("https://zimaev.github.io/navbar/")
    page.locator("#navbarNavDropdown >> li:has-text('Company')").click()

# Вариант 2
def test_chain2(page):
    page.goto("https://zimaev.github.io/navbar/")
    nav_bar = page.locator('div#navbarNavDropdown')
    nav_bar.locator("li:has-text('Company')").click()


# Фильтрация
# Поиск эл-ов, не соответствующих локатору
def test_chain3(page):
    page.goto("https://zimaev.github.io/filter/")
    row_locator = page.locator("tr")
    row_locator.filter(has_not=page.get_by_role("button")).count()

# Поиск эл-ов, не содержащих определенный текст
def test_chain4(page):
    page.goto("https://zimaev.github.io/filter/")
    row_locator = page.locator("tr")
    row_locator.filter(has_not_text="helicopter")

# Комбинация
# def test_chain5(page):
#     page.goto("https://zimaev.github.io/filter/")
#     row_locator = page.locator("tr")
#     row_locator.filter(has_text="text in column 1")
#     row_locator.filter(has=page.get_by_role("button", name="column 2 button"))
#     row_locator.click()
# ? Нерабочий пример




