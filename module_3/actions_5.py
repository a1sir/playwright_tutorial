# 3.2 Действия с элементами (Actions), шаг 6

# Диалоговые окна
def test_dialogs(page):
    page.goto("https://zimaev.github.io/dialog/")
    page.get_by_text("Диалог Alert").click()
    page.get_by_text("Диалог Confirmation").click()
    page.get_by_text("Диалог Prompt").click()

# После того как вы нажмете кнопку «Диалог Confirmation», вы увидите диалоговое окно с вопросом
# - Вы хотите сохранить изменения?
# Если вы нажмете кнопку OK, выше кнопок вы увидите сообщение - "Изменения сохранены!" .
# Однако если вы нажмете кнопку Отмена, вы увидите сообщение - "Изменения не сохранены!".
# Реализуем сценарий в котором необходимо нажать кнопку "OK"
def test_dialogs2(page):
    page.goto("https://zimaev.github.io/dialog/")
    page.on("dialog", lambda dialog: dialog.accept()) # анонимная функция обрабатывающая событие
    # dialog.accept() - закрыть диалоговое окно нажав кнопку «OK»
    page.get_by_text("Диалог Confirmation").click()