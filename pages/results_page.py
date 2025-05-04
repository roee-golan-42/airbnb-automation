from .base_page import BasePage
from playwright.async_api import Page


class ResultsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.apartments = page.locator("[data-testid='card-container']")

    async def get_apartment_title(self):
        # await self.page.wait_for_load_state("load")
        # await self.page.wait_for_timeout(5000)
        await self.apartments.nth(18).wait_for(state="visible")
        apartment_elements = await self.apartments.all()
        print(f"Number of apartments: {len(apartment_elements)}")

        # for apartment in apartment_elements:
        #     title = await apartment.inner_text()
        #     print(f"Apartment Title: {title}")
        return None
