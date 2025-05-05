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
    NUMBER_OF_CHILDREN = 1

    main_page = MainPage(page)
    search_component = SearchComponent(page)
    results_page = ResultsPage(page)

    await main_page.goto("https://airbnb.com")

    await search_component.enter_destination(DESTINATION_NAME)
    await search_component.choose_dates(CHECK_IN_DATE, CHECK_OUT_DATE)
    await search_component.set_amount_of_adults(NUMBER_OF_ADULTS)
    await search_component.set_number_of_children(NUMBER_OF_CHILDREN)
    await search_component.search_button.click()

    search_params_to_exist_in_apartments_link = [
        f"adults={NUMBER_OF_ADULTS}",
    ]
    # search_params_to_exist_in_apartments_link.append(
    #     CHECK_IN_DATE
    # )
    #  search_params_to_exist_in_apartments_link.append(
    #     CHECK_OUT_DATE
    # )

    await results_page.map_results()
    await results_page.validate_apartments_links_matches_search_params(
        search_params_to_exist_in_apartments_link
    )
    await results_page.analyze_results()
