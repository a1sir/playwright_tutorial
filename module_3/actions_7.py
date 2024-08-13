# 3.2 Действия с элементами (Actions), шаг 8
from playwright.sync_api import  sync_playwright
import os


# Скачать файл
# ! Тест не проходит
def test_download(page):

    page.goto("https://demoqa.com/upload-download")

    with page.expect_download() as download_info:
        page.locator("a:has-text(\"Download\")").click()

    download = download_info.value
    file_name = download.suggested_filename
    destination_folder_path = "/home/"
    download.save_as(os.path.join(destination_folder_path, file_name))


# Вариант кода из комментария от автора также не срабатывает
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demoqa.com/upload-download")
    with page.expect_download() as download_info:
        page.locator("a:has-text(\"Download\")").click()
    download = download_info.value
    file_name = download.suggested_filename
    destination_folder_path = "./data/"
    download.save_as(os.path.join(destination_folder_path, file_name))

