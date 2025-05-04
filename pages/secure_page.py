from .base_page import BasePage


class SecurePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.flash = page.locator("#flash")

    def is_login_successful(self):
        return (
            self.flash.is_visible()
            and "You logged into a secure area!" in self.flash.inner_text()
        )
