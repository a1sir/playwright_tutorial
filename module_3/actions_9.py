# 3.2 Действия с элементами (Actions), шаг 10

# Создание скриншотов
# Пример взят из actions_8.py
def test_screen(page):
    page.goto('https://zimaev.github.io/table/')
    row = page.locator("tr")
    print(row.all_inner_texts())
    page.screenshot(path="../screenshot.png")


# Скриншот всей страницы
def test_screen2(page):
    page.goto('https://zimaev.github.io/table/')
    row = page.locator("tr")
    print(row.all_inner_texts())
    page.screenshot(path="../screenshot.png", full_page=True)


# Скриншот web-элемента (заголовка страницы)
def test_screen3(page):
    page.goto('https://zimaev.github.io/table/')
    row = page.locator("tr")
    print(row.all_inner_texts())
    page.locator("caption").screenshot(path="../screenshot.png")


# Аргументы
# full_page (bool): Определяет, следует ли создать скриншот всей страницы (True) или только видимой области (False).
# По умолчанию значение False.
# page.screenshot(path="full_page.png", full_page=True)

# type (str): Задает формат изображения. Доступные варианты включают 'jpeg' и 'png'. По умолчанию 'png'.
# page.screenshot(path="example.jpeg", type="jpeg")

# quality (int): Качество сжатия изображения для формата 'jpeg'. Должно быть число от 0 до 100.
# По умолчанию не определено.
# page.screenshot(path="example.jpeg", type="jpeg", quality=80)

# clip (dict): Задает область для создания скриншота, указав координаты x, y, ширину и высоту. Например:
# page.screenshot(path="clipped_image.png", clip={"x": 50, "y": 0, "width": 400, "height": 300})

# omit_background (bool): Позволяет убрать фон изображения. Если True, фон на скриншоте будет прозрачным,
# что актуально в случае формата 'png'. По умолчанию значение False.
# page.screenshot(path="transparent_background.png", omit_background=True)

# timeout (float | int): Задает максимальное время ожидания (в миллисекундах) перед созданием скриншота.
# Установите значение как "0", чтобы ждать неограниченное время. По умолчанию 30000 миллисекунд (30 секунд).
# page.screenshot(path="timeout_example.png", timeout=10000)
