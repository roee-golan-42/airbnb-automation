import pytest
from pages.base_page import BasePage
from pages.components.search_component import SearchComponent
from pages.main_page import MainPage
from pages.secure_page import SecurePage
from playwright.async_api import Page


@pytest.mark.asyncio
async def test_search_apartment(page: Page):
    DESTINATION_NAME = "Tel Aviv"
    CHECK_IN_DATE = "2025-06-01"
    CHECK_OUT_DATE = "2025-06-03"

    main_page = MainPage(page)
    search_component = SearchComponent(page)

    await main_page.goto("https://airbnb.com")

    await search_component.enter_destination(DESTINATION_NAME)
    await search_component.choose_dates(CHECK_IN_DATE, CHECK_OUT_DATE)
    await search_component.set_amount_of_adults(2)
    await search_component.search_button.click()
    await page.wait_for_timeout(100000)
