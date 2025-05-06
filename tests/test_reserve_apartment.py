import pytest
from pages.base_page import BasePage
from pages.components.reservation_preview_component import ReservationPreviewComponent
from pages.components.search_component import SearchComponent
from pages.main_page import MainPage
from playwright.async_api import Page

from pages.reservation_page import ReservationPage
from pages.results_page import ResultsPage


@pytest.mark.asyncio
async def test_search_apartment(page: Page):
    DESTINATION_NAME = "Tel Aviv"
    CHECK_IN_DATE = "2025-06-01"
    CHECK_OUT_DATE = "2025-06-03"
    NUMBER_OF_ADULTS = 2
    NUMBER_OF_CHILDREN = 1
    PHONE_NUMBER = "123456789"

    main_page = MainPage(page)
    search_component = SearchComponent(page)
    results_page = ResultsPage(page)
    reservation_preview_component = ReservationPreviewComponent(page)
    reservation_page = ReservationPage(page)

    # await main_page.goto("https://airbnb.com")

    # await search_component.enter_destination(DESTINATION_NAME)
    # await search_component.choose_dates(CHECK_IN_DATE, CHECK_OUT_DATE)
    # await search_component.set_amount_of_adults(NUMBER_OF_ADULTS)
    # await search_component.set_number_of_children(NUMBER_OF_CHILDREN)
    # await search_component.search_button.click()

    # search_params_to_exist_in_apartments_link = [
    #     f"adults={NUMBER_OF_ADULTS}",
    #     f"children={NUMBER_OF_CHILDREN}",
    # ]

    # await results_page.map_results()
    # await results_page.validate_apartments_links_matches_search_params(
    #     search_params_to_exist_in_apartments_link
    # )

    apartment_link = results_page.get_max_rated_apartment_link()
    await main_page.goto(apartment_link)

    # Reservation preview in apartment page

    await reservation_preview_component.guests_field.click(force=True)
    reservation_preview_data = {
        "price": await reservation_preview_component.get_price(),
        "check_in_date": await reservation_preview_component.get_check_in_date(),
        "check_out_date": await reservation_preview_component.get_check_out_date(),
        "number_of_adults": await reservation_preview_component.get_number_of_adults(),
        "number_of_children": await reservation_preview_component.get_number_of_children(),
    }
    await reservation_preview_component.guests_field.click(force=True)
    print(f"Reservation preview details: {reservation_preview_data}")

    assert (
        reservation_preview_data["number_of_adults"] == NUMBER_OF_ADULTS
    ), "Number of adults not matching the search param"
    assert (
        reservation_preview_data["number_of_children"] == NUMBER_OF_CHILDREN
    ), "Number of children not matching the search param"

    await reservation_preview_component.order_button.click(force=True)

    # Reservation page

    reservation_page_data = {
        "price": await reservation_page.get_price(),
        "dates": await reservation_page.get_dates(),
        "total_number_of_guests": await reservation_page.get_number_of_total_guests(),
    }
    print(f"Reservation preview details: {reservation_page_data}")

    # Validate reservation details again

    await reservation_page.phone_number_field.fill(PHONE_NUMBER)
