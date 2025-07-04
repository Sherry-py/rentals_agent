import asyncio
from playwright.async_api import async_playwright

async def test_rosebery_listings():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        url = "https://www.realestate.com.au/rent/in-rosebery,+nsw+2018/list-1"
        await page.goto(url)
        await page.wait_for_selector('div[data-testid="listing-card-wrapper"]', timeout=10000)
        cards = await page.query_selector_all('div[data-testid="listing-card-wrapper"]')
        print(f"找到的房源卡片数：{len(cards)}")
        await browser.close()

if __name__ == '__main__':
    asyncio.run(test_rosebery_listings())