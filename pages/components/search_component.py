from playwright.async_api import Page, Locator


class SearchComponent:
    def __init__(self, page: Page):
        self.page = page
        self.destination_field = self.page.get_by_test_id(
            "structured-search-input-field-query"
        )
        self.check_in_button = self.page.get_by_test_id(
            "structured-search-input-field-split-dates-0"
        )
        self.check_out_button = self.page.get_by_test_id(
            "structured-search-input-field-split-dates-1"
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
        self.choose_amount_of_children_component = self.page.locator(
            "[data-testid='search-block-filter-stepper-row-children']"
        )

    def get_date_button(self, year: str, month: str, day: str):
        return self.page.locator(f"[data-state--date-string='2025-{month}-{day}']")

    async def increase_amount_of_guests(
        self, choose_amount_of_guests_component: Locator, number_of_guests: int
    ):
        increase_button = choose_amount_of_guests_component.locator(
            "[data-testid*='increase-button']"
        )

        for _ in range(number_of_guests):
            await increase_button.click()

    async def enter_destination(self, destination_name: str):
        await self.destination_field.click()
        await self.destination_field.fill(destination_name)
        await self.destination_field.click()

    async def choose_dates(self, check_in_date: str, check_out_date: str):
        year, month, day = check_in_date.split("-")
        await self.check_in_button.click()
        await self.get_date_button(year, month, day).click()

        year, month, day = check_out_date.split("-")
        await self.get_date_button(year, month, day).click()
        await self.check_out_button.click()

    async def set_amount_of_adults(self, amount_of_adults: int):
        await self.guests_button.click()
        await self.increase_amount_of_guests(
            self.choose_amount_of_adults_component, amount_of_adults
        )

    async def set_number_of_children(self, amount_of_adults: int):
        await self.guests_button.click()
        await self.increase_amount_of_guests(
            self.choose_amount_of_adults_component, amount_of_adults
        )
