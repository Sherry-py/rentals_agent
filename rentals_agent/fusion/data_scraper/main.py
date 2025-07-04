from domain_scraper import scrape_domain_rent
from storage import save_to_json, save_to_sqlite

if __name__ == '__main__':
    results = scrape_domain_rent()
    save_to_json(results)
    save_to_sqlite(results)