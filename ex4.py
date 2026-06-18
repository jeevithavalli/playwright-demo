import asyncio
import time

from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as pw:
        browser=await pw.chromium.launch()
        page=await browser.new_page()
        await page.goto("https://www.amazon.in/")
        await page.wait_for_timeout(3000)
        print(await page.title())
        await browser.close()

asyncio.run(main())
