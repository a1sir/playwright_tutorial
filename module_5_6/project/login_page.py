# project/pages/login_page.py
from playwright.sync_api import Page


# page: Page — это аннотация типа, указывающая, что параметр page должен быть объектом типа Page из Playwright
# self.page = page — сохраняет переданный объект страницы в атрибуте экземпляра класса для дальнейшего использования.
class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator('#username')
        self.password_input = page.locator('#password')
        self.login_button = page.locator('#login')
        self.error_message = page.locator('#errorAlert')

# Этот метод открывает страницу логина. Он использует метод goto из Playwright для перехода по URL.
    def navigate(self):
        """Открывает страницу логина."""
        self.page.goto('https://zimaev.github.io/pom/')

# Этот метод выполняет вход с заданными учетными данными. Он заполняет поля имени пользователя и пароля
    # и нажимает кнопку входа.
    def login(self, username: str, password: str):
        """Выполняет вход с заданными учетными данными."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

# Этот метод возвращает текст сообщения об ошибке, если вход не удался.
    def get_error_message(self):
        """Возвращает текст сообщения об ошибке."""
        return self.error_message.inner_text()
