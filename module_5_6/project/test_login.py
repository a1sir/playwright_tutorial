# project/tests/test_login.py
import pytest
import allure
from login_page import LoginPage
from dashboard_page import DashboardPage


def test_login_failure(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login('invalid_user', 'invalid_password')
    assert login_page.get_error_message() == 'Invalid credentials. Please try again.'


# Создается объект DashboardPage.
# Проверяется, что на странице отображается корректное приветственное сообщение.
def test_login_success(page):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    login_page.navigate()
    login_page.login('admin', 'admin')

    dashboard_page.assert_welcome_message("Welcome admin")


# Используется декоратор pytest.mark.parametrize для задания нескольких наборов данных.
# Тест запускается для каждой пары username и password (т.е. тест будет выполнен дважды для каждой пары логин-пароль).
@pytest.mark.parametrize('username, password', [
    ('user', 'user'),
    ('admin', 'admin')
])
def test_login_success(page, username, password):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    login_page.navigate()
    login_page.login(username, password)

    dashboard_page.assert_welcome_message(f"Welcome {username}")


# Используем фикстуры для упрощения тестов:
# Удалены импорты классов страниц
# Фикстура page не передается в теста
# Фикстуры login_page и dashboard_page используются для инициализации соответствующих объектов.
# Тесты становятся более лаконичными и легко читаемыми.
def test_login_failure2(login_page):
    login_page.navigate()
    login_page.login('user', 'password')

    assert login_page.get_error_message() == 'Invalid credentials. Please try again.'


@pytest.mark.parametrize('username, password', [
    ('user', 'user'),
    ('admin', 'admin')
])
def test_login_success2(login_page, dashboard_page, username, password):
    login_page.navigate()
    login_page.login(username,password)
    dashboard_page.assert_welcome_message(f"Welcome {username}")




