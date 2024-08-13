# 3.2 Действия с элементами (Actions), шаг 4

# locator.select_option(**kwargs)
# Рассмотрим пример кода, который использует все три стратегии поиска (index, value, label)
def test_select(page):
    page.goto('https://zimaev.github.io/select/')
    page.select_option('#floatingSelect', value="3")
    page.select_option('#floatingSelect', index=1)
    page.select_option('#floatingSelect', label="Нашел и завел bug")

# синтаксис, без явного указания стратегии поиска
def test_select2(page):
    page.goto('https://zimaev.github.io/select/')
    page.select_option('#floatingSelect', "3")

# Множественный выбор
def test_select_multiple(page):
    page.goto('https://zimaev.github.io/select/')
    page.select_option('#skills', value=["playwright", "python"])
