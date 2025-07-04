import asyncio
from playwright.async_api import async_playwright
import pandas as pd

async def scrape_rosebery_rentals():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        # URL for Rosebery, NSW 2018 rental listings
        url = "https://www.realestate.com.au/rent/in-rosebery,+nsw+2018/list-1"
        await page.goto(url)
        await page.wait_for_timeout(5000)  # wait for JS to load listings

        listings = []

        # Grab the first 5 listings
        cards = await page.query_selector_all('div[data-testid="listing-card-wrapper"]')
        for idx, card in enumerate(cards[:5]):
            title_el = await card.query_selector('a[data-testid="listing-title"]')
            price_el = await card.query_selector('p[data-testid="listing-price"]')
            link_el = await card.query_selector('a[data-testid="listing-title"]')

            title = await title_el.inner_text() if title_el else "N/A"
            price = await price_el.inner_text() if price_el else "N/A"
            link = await link_el.get_attribute("href") if link_el else ""

            listings.append({
                "Index": idx + 1,
                "Title": title.strip(),
                "Price": price.strip(),
                "Link": "https://www.realestate.com.au" + link if link else ""
            })

        # Close browser
        await browser.close()

        # Save to CSV
        df = pd.DataFrame(listings)
        df.to_csv("rosebery_rentals_top5.csv", index=False)
        print(df)

if __name__ == '__main__':
    asyncio.run(scrape_rosebery_rentals())