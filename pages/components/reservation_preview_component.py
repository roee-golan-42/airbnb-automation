from playwright.async_api import Page, Locator


class ReservationPreviewComponent:
    def __init__(self, page: Page):
        self.page = page
        self.check_in_date = self.page.get_by_test_id("change-dates-checkIn")
        self.check_out_date = self.page.get_by_test_id("change-dates-checkOut")
        self.price_per_night = self.page.locator(
            " [data-section-id='BOOK_IT_SIDEBAR'] [class='_hb913q']"
        )
        self.guests_field = self.page.locator("[aria-labelledby*='guests-label']")
        self.number_of_adults = self.page.get_by_test_id(
            "GuestPicker-book_it-form-adults-stepper-value"
        )
        self.number_of_children = self.page.get_by_test_id(
            "GuestPicker-book_it-form-children-stepper-value"
        )

    async def get_check_in_date(self):
        return await self.check_in_date.inner_text()

    async def get_check_out_date(self):
        return await self.check_out_date.inner_text()

    async def get_price(self):
        price = await self.price_per_night.inner_text()
        return int("".join(char for char in price if char.isdigit()))

    async def get_number_of_adults(self):
        return int(await self.number_of_adults.inner_text())

    async def get_number_of_children(self):
        return int(await self.number_of_children.inner_text())
