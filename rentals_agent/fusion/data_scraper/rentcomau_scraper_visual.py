import asyncio
from playwright.async_api import async_playwright
import pandas as pd


async def scrape_rentcomau_rosebery_visual():
    async with async_playwright() as p:
        # 这里改成headless=False，打开可见浏览器窗口
        browser = await p.chromium.launch(headless=False)

        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/115.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 800},
        )
        page = await context.new_page()

        url = "https://www.rent.com.au/nsw/rosebery-2018/apartments?listing_type=rental"
        await page.goto(url)
        await page.wait_for_timeout(7000)  # 等待页面加载

        listings = []

        cards = await page.query_selector_all('article[data-testid="listing-card"]')

        for idx, card in enumerate(cards[:5]):
            title_el = await card.query_selector('a[data-testid="listing-link"]')
            title = await title_el.inner_text() if title_el else "N/A"

            price_el = await card.query_selector('span[data-testid="price"]')
            price = await price_el.inner_text() if price_el else "N/A"

            address_el = await card.query_selector('span[data-testid="address"]')
            address = await address_el.inner_text() if address_el else "N/A"

            link = await title_el.get_attribute("href") if title_el else ""
            full_link = f"https://www.rent.com.au{link}" if link else ""

            listings.append({
                "Index": idx + 1,
                "Title": title.strip(),
                "Price": price.strip(),
                "Address": address.strip(),
                "Link": full_link,
            })

        print(listings)

        await browser.close()


if __name__ == '__main__':
    asyncio.run(scrape_rentcomau_rosebery_visual())