# 3.2 Действия с элементами (Actions), шаг 3

# locator.check(**kwargs)
# сценарий, в котором мы по очереди нажимаем на все чекбоксы и радио-кнопки на сайте
def test_checkbox(page):
    page.goto('https://zimaev.github.io/checks-radios/')
    page.locator("text=Default checkbox").check()
    page.locator("text=Checked checkbox").check()
    page.locator("text=Default radio").check()
    page.locator("text=Default checked radio").check()
    page.locator("text=Checked switch checkbox input").check()

# locator.click(**kwargs)
# Второй способ взаимодействия с данным типом веб-элементов - это уже знакомый нам клик
def test_checkbox2(page):
    page.goto('https://zimaev.github.io/checks-radios/')
    page.locator("text=Default checkbox").click()
    page.locator("text=Checked checkbox").click()
    page.locator("text=Default radio").click()
    page.locator("text=Default checked radio").click()
    page.locator("text=Checked switch checkbox input").click()
