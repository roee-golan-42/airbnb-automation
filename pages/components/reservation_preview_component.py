from playwright.async_api import Page, Locator


class ReservationPreviewComponent:
    def __init__(self, page: Page):
        self.page = page
        self.translation_popup = self.page.get_by_test_id("translation-announce-modal")
        self.check_in_date = self.page.get_by_test_id("change-dates-checkIn")
        self.check_out_date = self.page.get_by_test_id("change-dates-checkOut")
        self.price_per_night = self.page.locator(
            "[data-section-id='BOOK_IT_SIDEBAR'] [class='_hb913q']"
        )
        self.guests_field = self.page.locator("[aria-labelledby*='guests-label']")
        self.number_of_adults = self.page.get_by_test_id(
            "GuestPicker-book_it-form-adults-stepper-value"
        )
        self.number_of_children = self.page.get_by_test_id(
            "GuestPicker-book_it-form-children-stepper-value"
        )
        self.order_button = self.page.locator(
            "[data-section-id='BOOK_IT_SIDEBAR'] [data-testid='homes-pdp-cta-btn']"
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

    async def wait_for_translate_popup_and_close(self):
        try:
            await self.translation_popup.wait_for(state="visible", timeout=4000)
            await self.page.click("[data-section-id='TITLE_DEFAULT']", force=True)
        except TimeoutError:
            pass
