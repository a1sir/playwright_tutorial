# Фикстуры со страницы 2.2 Первый тест, шаг 3, Редактирование контекста браузера

import pytest


# Фикстура изменения окна браузера (2.2 Первый тест, шаг 3, Редактирование контекста браузера)
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {

        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }

# Фикстура изменения окна браузера (2.2 Первый тест, шаг 3, Редактирование контекста браузера)
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "storage_state": {
            "cookies": [
                {
                    "name": "stepik",
                    "value": "sd4fFfv!x_cfcstepik",
                    "url": "https://example.com"  # Замените на нужный URL
                },
            ]
        },
    }

# Фикстура пропуска теста браузером (2.3 Работа с CLI и pytest-playwright, шаг 2, Пропустить тест браузером)
@pytest.mark.skip_browser("firefox")
def test_visit_example(page):
    page.goto("https://example.com")
    # ...


# Фикстура запуска в определенном браузере (2.3 Работа с CLI и pytest-playwright, шаг 2, Запуск в определенном браузере)
@pytest.mark.only_browser("chromium")
def test_visit_example(page):
    page.goto("https://example.com")
    # ...


