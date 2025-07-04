import asyncio
from playwright.async_api import async_playwright
import pandas as pd


async def scrape_rentcomau_rosebery():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # 设置为 False 以打开浏览器窗口
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 800},
        )
        page = await context.new_page()

        # 使用您提供的最新有效链接
        url = "https://www.rent.com.au/properties/rosebery-nsw-2018"
        await page.goto(url)
        await page.wait_for_timeout(7000)  # 等待页面加载

        listings = []

        # 根据页面结构选择房源卡片
        cards = await page.query_selector_all('div[data-testid="listing-card-wrapper"]')

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

        await browser.close()

        # 将数据保存为 CSV 文件
        df = pd.DataFrame(listings)
        df.to_csv("rentcomau_rosebery_top5.csv", index=False)
        print(df)


if __name__ == '__main__':
    asyncio.run(scrape_rentcomau_rosebery())