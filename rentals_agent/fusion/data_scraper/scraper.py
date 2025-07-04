from typing import List, Dict
import logging

from .fetcher import fetch_html
from .parser_realestate import parse_realestate

logger = logging.getLogger(__name__)

def fetch_rentals(url: str) -> List[Dict]:
    """统一抓取接口，根据url自动选择对应解析器"""
    html = fetch_html(url)
    if not html:
        logger.error("Empty HTML content, aborting fetch_rentals.")
        return []

    if 'realestate.com.au' in url:
        return parse_realestate(html, url)
    else:
        logger.error(f"Unsupported website: {url}")
        return []