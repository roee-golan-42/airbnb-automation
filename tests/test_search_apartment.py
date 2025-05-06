# import os
# from dotenv import load_dotenv
# import pytest
# from pages.base_page import BasePage
# from pages.components.search_component import SearchComponent
# from pages.main_page import MainPage
# from playwright.async_api import Page

# from pages.results_page import ResultsPage

# load_dotenv()


# @pytest.mark.asyncio
# async def test_search_apartment(page: Page):
#     BASE_URL = str(os.getenv("AIRBNB_URL"))
#     DESTINATION_NAME = "tel aviv"
#     CHECK_IN_DATE = "2025-06-01"
#     CHECK_OUT_DATE = "2025-06-03"
#     NUMBER_OF_ADULTS = 2

#     main_page = MainPage(page)
#     search_component = SearchComponent(page)
#     results_page = ResultsPage(page)

#     await main_page.goto(BASE_URL)

#     await search_component.enter_destination(DESTINATION_NAME)
#     await search_component.choose_dates(CHECK_IN_DATE, CHECK_OUT_DATE)
#     await search_component.set_amount_of_adults(NUMBER_OF_ADULTS)
#     await search_component.search_button.click()

#     search_params_to_exist_in_results_page_link = [
#         *DESTINATION_NAME.split(" "),
#         CHECK_IN_DATE,
#         CHECK_OUT_DATE,
#         f"adults={NUMBER_OF_ADULTS}",
#     ]
#     await results_page.validate_page_link_matches_search_params(
#         search_params_to_exist_in_results_page_link
#     )

#     await results_page.map_results()

#     # due to recommended apartments in flexible dates that sometime appear and some times not, cannot assert check-in and check-out dates
#     search_params_to_exist_in_apartments_link = [
#         # CHECK_IN_DATE,
#         # CHECK_OUT_DATE,
#         f"adults={NUMBER_OF_ADULTS}",
#     ]
#     await results_page.validate_apartments_links_matches_search_params(
#         search_params_to_exist_in_apartments_link
#     )

#     results_page.analyze_results()
