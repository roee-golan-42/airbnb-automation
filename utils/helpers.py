from typing import List


def print_analyze_results(accumulated_apartment_data: List):
    cheapest_apartment = min(accumulated_apartment_data, key=lambda apt: apt["price"])
    highest_rated_apartment = max(
        accumulated_apartment_data, key=lambda apt: apt["rating"]
    )
    print(
        f"""Total amount of apartments: {len(accumulated_apartment_data)}
Cheapest apartment: {cheapest_apartment}
Highest rated apartment: {highest_rated_apartment}"""
    )
