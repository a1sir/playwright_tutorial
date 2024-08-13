# 3.2 Действия с элементами (Actions), шаг 7

# Загрузка файла
def test_select_multiple(page):
    page.goto('https://zimaev.github.io/upload/')
    page.set_input_files("#formFile", "hello.txt")
    page.locator("#file-submit").click()


# Вы можете зарегистрировать обработчик события "filechooser" и получить тот-же результат
def test_select_multiple2(page):
    page.goto('https://zimaev.github.io/upload/')
    page.on("filechooser", lambda file_chooser: file_chooser.set_files("hello.txt"))
    page.locator("#formFile").click()

# Или вы можете использовать другой вариант записи.
def test_select_multiple3(page):
    page.goto('https://zimaev.github.io/upload/')
    with page.expect_file_chooser() as fc_info:
        page.locator("#formFile").click()
    file_chooser = fc_info.value
    file_chooser.set_files("hello.txt")
