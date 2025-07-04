import asyncio
from playwright.async_api import async_playwright

async def open_page_visual():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://www.rent.com.au/properties/rosebery-nsw-2018")
        await page.wait_for_timeout(10000)  # 多等几秒，确保页面加载
        # 截图保存，方便观察
        await page.screenshot(path="rentcomau_rosebery_page.png")
        print("截图已保存: rentcomau_rosebery_page.png")
        await browser.close()

if __name__ == '__main__':
    asyncio.run(open_page_visual())