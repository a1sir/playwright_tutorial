# 4.2 Перехват и изменение сетевых запросов. Mocking, шаг 2

# Мониторинг сетевых запросов

# Playwright позволяет перехватывать сетевой трафик с помощью метода page.on
def test_listen_network(page):
    page.on("request", lambda request: print(">>", request.method, request.url))
    page.on("response", lambda response: print("<<", response.status, response.url))
    page.goto('https://osinit.ru/')
