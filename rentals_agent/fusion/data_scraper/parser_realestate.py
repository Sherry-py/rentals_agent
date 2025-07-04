from bs4 import BeautifulSoup
from typing import List, Dict
from urllib.parse import urljoin
import logging

logger = logging.getLogger(__name__)

def parse_realestate(html: str, base_url: str) -> List[Dict]:
    """解析realestate.com.au房源列表HTML，返回结构化字典列表"""
    rentals = []
    soup = BeautifulSoup(html, 'html.parser')

    listings = soup.select('div.property-card')
    logger.info(f"Found {len(listings)} property-card listings")

    for listing in listings:
        try:
            address = listing.select_one('span.property-address')
            price = listing.select_one('span.property-price')
            link = listing.select_one('a.property-link')
            image = listing.select_one('img.property-image')
            features = listing.select('span.property-feature')

            bedrooms = bathrooms = area = 'N/A'
            for f in features:
                text = f.text.strip().lower()
                if 'bed' in text:
                    bedrooms = text
                elif 'bath' in text:
                    bathrooms = text
                elif 'm²' in text or 'sqm' in text:
                    area = text

            rental = {
                'address': address.text.strip() if address else 'N/A',
                'price': price.text.strip() if price else 'N/A',
                'bedrooms': bedrooms,
                'bathrooms': bathrooms,
                'area': area,
                'link': urljoin(base_url, link['href']) if link and link.has_attr('href') else 'N/A',
                'image': image['src'] if image and image.has_attr('src') else 'N/A',
            }
            rentals.append(rental)
        except Exception as e:
            logger.warning(f"Error parsing listing: {e}")
            continue

    return rentals