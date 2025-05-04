from .base_page import BasePage
from playwright.sync_api import Page


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.destination_field = self.page.get_by_test_id(
            "structured-search-input-field-query"
        )
        self.check_in_button = self.page.get_by_test_id(
            "structured-search-input-field-split-dates-0"
        )
        self.guests_button = self.page.get_by_test_id(
            "structured-search-input-field-guests-button"
        )
        self.search_button = self.page.get_by_test_id(
            "structured-search-input-search-button"
        )
        self.choose_amount_of_adults_component = self.page.locator(
            "[data-testid='search-block-filter-stepper-row-adults']"
        )

    def get_date_button(self, month: str, day: str):
        return self.page.locator(f"[data-state--date-string='2025-{month}-{day}']")

    def increase_amount_of_gusts(self, number_of_gusts: int):
        self.choose_amount_of_adults_component.locator(
            "[data-testid*='increase-button']"
        ).click()

    def search_apartment(
        self,
        destination_name: str,
        check_in_month: str,
        check_in_day: str,
        check_out_month: str,
        check_out_day: str,
    ):
        self.destination_field.fill(destination_name)
        self.check_in_button.click()
        self.get_date_button(check_in_month, check_in_day).click(force=True)
        self.get_date_button(check_in_month, check_out_day).click(force=True)
        self.guests_button.click()
        self.increase_amount_of_gusts(2)
