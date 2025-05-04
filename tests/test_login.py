from pages.login_page import LoginPage
from pages.secure_page import SecurePage


def test_valid_login(page):
    login_page = LoginPage(page)
    secure_page = SecurePage(page)

    login_page.goto("https://the-internet.herokuapp.com/login")
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert secure_page.is_login_successful()


def test_invalid_login(page):
    login_page = LoginPage(page)
    secure_page = SecurePage(page)

    login_page.goto("https://the-internet.herokuapp.com/login")
    login_page.login("tomsmith", "SuperSecret")
    assert secure_page.is_login_successful()
