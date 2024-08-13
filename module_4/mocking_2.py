# 4.2 Перехват и изменение сетевых запросов. Mocking, шаг 3

# Модифицировать запрос

# page.route - функция позволяющая обрабатывать сетевые запросы,
# в отличие от page.on, метод route может изменять сетевые запросы и ответы

# Представим, что нам необходимо изменить передаваемый данные.
# Для этого используете метод  route.continue_  и аргументом post_data
def test_network(page):
    page.route("**/register", lambda route: route.continue_(post_data='{"email": "user","password": "secret"}'))
    # page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort()) # вариант прерывания запросов к данным сайта,
    # если это изображения
    page.goto('https://reqres.in/')
    page.get_by_text(' Register - successful ').click()
