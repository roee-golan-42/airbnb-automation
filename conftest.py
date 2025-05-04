import asyncio
import pytest
import os
from playwright.async_api import async_playwright


@pytest.fixture(scope="function")
async def page(request):
    loop = asyncio.get_running_loop()
    trace_name = f"trace_{request.node.name}.zip"
    trace_path = os.path.join("traces", trace_name)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()

        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
        yield page

        await context.tracing.stop(path=trace_path)
        await browser.close()
