# 3.2 Действия с элементами (Actions), шаг 5

# Drag and Drop
def test_drag_and_drop(page):
    page.goto('https://zimaev.github.io/draganddrop/')
    page.drag_and_drop("#drag", "#drop")
