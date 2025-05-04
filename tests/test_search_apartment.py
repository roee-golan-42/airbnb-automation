from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.secure_page import SecurePage
from playwright.sync_api import Page


def test_search_apartment(page: Page):
    main_page = MainPage(page)
    main_page.goto("https://airbnb.com")
    main_page.search_apartment("tel aviv", "06", "01", "06", "03")
    page.wait_for_timeout(10000)
