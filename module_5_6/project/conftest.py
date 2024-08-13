# project/conftest.py
import pytest
from login_page import LoginPage
from dashboard_page import DashboardPage

# Эти фикстуры создают экземпляры LoginPage и DashboardPage, которые могут быть использованы в тестах.
@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)
