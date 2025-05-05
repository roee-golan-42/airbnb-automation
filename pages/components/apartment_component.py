import re
from playwright.async_api import Page, Locator


class ApartmentComponent:
    def __init__(self, page: Page, father_element: Locator):
        self.page = page
        self.apartment_title = father_element.locator(
            "[data-testid='listing-card-title']"
        )
        self.apartment_price = father_element.locator(
            "[data-testid='price-availability-row']"
        )

    async def get_title(self):
        return await self.apartment_title.inner_text()

    async def get_price_per_night(self):
        text = (await self.apartment_price.inner_text()).split(" ")[0]
        match = re.search(r"₪([\d,]+)", text)
        if match:
            return int(match.group(1).replace(",", ""))
        return 3
