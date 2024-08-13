import pytest
import allure

# @allure.feature группирует тесты по проверяемому функционалу.
# @allure.story группирует тесты по User story
# @allure.severity: Аннотация указывает на уровень важности теста.
# Это может дать представление о том, как расставить приоритеты при расследовании различных сбоев в тестировании.

# @allure.title Задает название теста. Понятное для человека название теста.
# Если данная аннотация не передана, вместо названия используется название тестовой функции.


@allure.feature('Авторизация')
@allure.story('Авторизации недействительные учетные данные')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Авторизаиця с недействительными учетными данными')
# Оригинальный тест без allure в файле test_login.py - test_login_failure2
def test_login_failure(login_page):
    with allure.step('Открыть страницу авторизации'):
        login_page.navigate()
    with allure.step('Ввести в форму авторизации недействительные учетные данные'):
        login_page.login('invalid_user', 'invalid_password')
    with allure.step('Отображается ошибка - Invalid credentials. Please try again.'):
        assert login_page.get_error_message() == 'Invalid credentials. Please try again.'


@allure.feature('Login')
@allure.story('Login with valid credentials')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Авторизация с корректными учетными данными')
@pytest.mark.parametrize('username, password', [
    ('user', 'user'),
    ('admin', 'admin')
])
# Оригинальный тест без allure в файле test_login.py - test_login_success2
def test_login_success(login_page, dashboard_page, username, password):
    with allure.step('Открыть страницу авторизации'):
        login_page.navigate()
    with allure.step('Ввести в форму авторизации недействительные учетные данные'):
        login_page.login(username, password)
    with allure.step('Отображается приветственное сообщение с именем пользователя'):
        dashboard_page.assert_welcome_message(f"Welcome {username}")
