import asyncio
from playwright.async_api import async_playwright

async def test_rosebery_listings_v2():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        url = "https://www.realestate.com.au/rent/in-rosebery,+nsw+2018/list-1"
        await page.goto(url)
        await page.wait_for_timeout(7000)  # 等7秒，确保加载

        # 尝试多种选择器抓取
        selectors = [
            'div[data-testid="listing-card-wrapper"]',
            'article',
            'li',
            'div[class*="listing"]',
        ]

        for sel in selectors:
            cards = await page.query_selector_all(sel)
            print(f'选择器 {sel} 找到元素数量: {len(cards)}')

        await browser.close()

if __name__ == '__main__':
    asyncio.run(test_rosebery_listings_v2())