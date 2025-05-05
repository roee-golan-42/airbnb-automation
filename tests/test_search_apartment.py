import pytest
from pages.base_page import BasePage
from pages.components.search_component import SearchComponent
from pages.main_page import MainPage
from playwright.async_api import Page

from pages.results_page import ResultsPage


@pytest.mark.asyncio
async def test_search_apartment(page: Page):
    DESTINATION_NAME = "Tel Aviv"
    CHECK_IN_DATE = "2025-06-01"
    CHECK_OUT_DATE = "2025-06-03"
    NUMBER_OF_ADULTS = 2

    main_page = MainPage(page)
    search_component = SearchComponent(page)
    results_page = ResultsPage(page)

    # await main_page.goto("https://airbnb.com")

    # await search_component.enter_destination(DESTINATION_NAME)
    # await search_component.choose_dates(CHECK_IN_DATE, CHECK_OUT_DATE)
    # await search_component.set_amount_of_adults(2)
    # await search_component.search_button.click()

    await main_page.goto(
        "https://www.airbnb.com/s/tel-aviv/homes?place_id=ChIJH3w7GaZMHRURkD-WwKJy-8E&refinement_paths%5B%5D=%2Fhomes&checkin=2025-06-01&checkout=2025-06-02&date_picker_type=calendar&adults=2&guests=1&search_type=filter_change&query=tel%20aviv&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2025-06-01&monthly_length=3&monthly_end_date=2025-09-01&search_mode=regular_search&price_filter_input_type=0&price_filter_num_nights=1&channel=EXPLORE&source=structured_search_input_header",
    )
    # await main_page.page.wait_for_timeout(1000000)
    await results_page.analyze_results()

    # await page.wait_for_timeout(100000)
