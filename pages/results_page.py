from typing import List
from pages.components.apartment_component import ApartmentComponent
from utils.helpers import print_analyze_results
from .base_page import BasePage
from playwright.async_api import Page, Locator


class ResultsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.apartments_locator = page.locator("[data-testid='card-container']")
        self.next_page_button = page.locator(
            "[aria-label='Search results pagination'] [aria-label='Next']"
        )

    async def has_next_page(self):
        return await self.next_page_button.is_enabled()

    async def wait_for_apartments_to_load(self):
        # must wait to
        if await self.has_next_page():
            await self.apartments_locator.nth(17).wait_for(state="visible")
        else:
            await self.apartments_locator.nth(1).wait_for(state="visible")
            await self.page.wait_for_timeout(1000)

        apartments = await self.apartments_locator.all()

        def get_apartment_component(apartment_locator: Locator):
            return ApartmentComponent(self.page, apartment_locator)

        return list(map(get_apartment_component, apartments))

    async def analyze_results(self):
        apartments = await self.wait_for_apartments_to_load()
        accumulated_apartment_data = []
        page_count = 1

        while await self.has_next_page():
            apartments = await self.wait_for_apartments_to_load()
            print(
                f"Analyzing page number {page_count}. Number of apartments in page: {len(apartments)}"
            )

            for apartment in apartments:
                price = await apartment.get_price_per_night()
                title = await apartment.get_title()
                rating = await apartment.get_rating()
                link = await apartment.get_link()
                if price and rating:
                    accumulated_apartment_data.append(
                        {"title": title, "price": price, "rating": rating, "link": link}
                    )

            await self.next_page_button.click()
            page_count += 1

        print_analyze_results(accumulated_apartment_data)
