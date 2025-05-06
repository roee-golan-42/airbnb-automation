import re
from pages.components.apartment_component import ApartmentComponent
from .base_page import BasePage
from playwright.async_api import Page


class ResultsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.dates = page.locator("[data-section-id='DATE_PICKER']")
        self.number_of_guests = page.locator("[data-section-id='GUEST_PICKER'']")
        self.price_per_night = self.page.get_by_test_id("pd-title-ACCOMMODATION")

    async def get_dates(self):
        return (await self.dates.inner_text()).split("\n")[1].strip()

    async def get_number_of_total_guests(self):
        guests_line = (await self.number_of_guests.inner_text()).split("\n")[1].strip()
        return int(guests_line.split()[0])

    async def get_price(self):
        match = re.search(r"\d+", await self.price_per_night.inner_text())
        return int(match.group()) if match else print("Failed parse price")
