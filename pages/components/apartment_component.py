import re
from playwright.async_api import Page, Locator


class ApartmentComponent:
    def __init__(self, page: Page, father_element: Locator):
        self.page = page
        self.father_element = father_element
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
        print("apartment price not found.")

    async def get_rating(self):
        text = await self.father_element.inner_text()
        match = re.search(r"(\d\.\d{1,2})\s*out of 5", text)
        if match:
            rating = float(match.group(1))
            return rating
        else:
            print("Rating not found. (either 'new' or not exist)")

    async def get_link(self):
        pass
