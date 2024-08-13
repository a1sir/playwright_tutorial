# 3.2 Действия с элементами (Actions), шаг 9

# Получение значений элемента

# innerText умеет считывать стили и не возвращает содержимое скрытых элементов, тогда как textContent этого не делает.
def test(page):
    page.goto('https://zimaev.github.io/table/')
    row = page.locator("tr")
    print(row.all_inner_texts())


# textContent получает содержимое всех элементов, включая <script> и <style>, тогда как innerText этого не делает.
def test2(page):
    page.goto('https://zimaev.github.io/table/')
    row = page.locator("tr")
    print(row.all_text_contents())
