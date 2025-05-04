from playwright.async_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    async def goto(self, url: str):
        await self.page.goto(url)

    async def get_title(self):
        return await self.page.title()
