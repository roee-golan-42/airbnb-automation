from .base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.welcome_text = page.locator("text=Welcome")

    def is_logged_in(self):
        return self.welcome_text.is_visible()
