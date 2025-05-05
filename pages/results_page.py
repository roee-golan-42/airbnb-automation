from pages.components.apartment_component import ApartmentComponent
from .base_page import BasePage
from playwright.async_api import Page, Locator


class ResultsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.apartments_locator = page.locator("[data-testid='card-container']")
        self.next_page_button = page.locator("[aria-label='Next']")

    async def wait_for_apartments_to_load(self):
        # if "has next page":
        #     await self.apartments_locator.nth(18).wait_for(state="visible")
        # else:
        #     await self.apartments_locator.nth(1).wait_for(state="visible")
        #     await self.page.wait_for_timeout(1000)
        await self.apartments_locator.nth(17).wait_for(state="visible")

        temp = await self.apartments_locator.all()

        def get_ap(ap_locator: Locator):
            return ApartmentComponent(self.page, ap_locator)

        return list(map(get_ap, temp))
        return await self.apartments_locator.all()

    async def get_apartment_title(self):
        apartments = await self.wait_for_apartments_to_load()
        print(f"Number of apartments: {len(apartments)}")
        print(await apartments[0].get_title())
        print(await apartments[0].get_price_per_night())
