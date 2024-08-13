# Код со страницы 3.1 Локаторы(Locators), шаг 8
# Поиск элемента по роли ARIA - page.get_by_role(role, **kwargs)

def test_loc(page):
    page.goto('https://zimaev.github.io/text_input/')
    page.get_by_label("Email address").fill("qa@example.com")
    page.get_by_title("username").fill("Anton")
    page.get_by_placeholder('password').fill("secret")
    page.get_by_role('checkbox').click()
