# 3.2 Действия с элементами (Actions), шаг 2

# locator.fill(текст, **kwargs)
# ввод данных в поле ввода
def test_login(page):
    page.goto('https://exaltedplushadware.antonzimaiev.repl.co/?') # страница не открывается
    page.locator("#exampleInputEmail1").fill("admin@example.com")


# locator.type(текст, **kwargs)
#  отправка события keydown, keypress/input и keyup для каждого символа в тексте
def test_login2(page):
    page.goto('https://exaltedplushadware.antonzimaiev.repl.co/?') # страница не открывается
    page.locator("#exampleInputEmail1").type("admin@example.com")


# locator.press_sequentially(текст, **kwargs)
# метод последовательной отправки нажатия клавиш по элементу (с задержкой в 100)
locator.press_sequentially("world", delay=100)


# locator.press(key, **kwargs)
# Функциональные клавиши(F1 - F12, Backspace, Tab, Delete, Escape, ArrowDown, End, Enter, Home, Insert, PageDown,
# PageUp, ArrowRight, ArrowUp и так далее.) могут быть отправлены с помощью метода locator.press(key, **kwargs)


