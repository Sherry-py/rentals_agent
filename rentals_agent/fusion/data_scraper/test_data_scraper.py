import unittest
from .scraper import fetch_rentals

class TestDataScraper(unittest.TestCase):
    def test_realestate_fetch(self):
        url = "https://www.realestate.com.au/rent/in-kensington,+nsw+2033/list-1"
        rentals = fetch_rentals(url)
        print(f"抓取到 {len(rentals)} 条房源")
        if rentals:
            print("示例房源：", rentals[0])
        self.assertIsInstance(rentals, list)
        if rentals:
            rental = rentals[0]
            self.assertIn('address', rental)
            self.assertIn('price', rental)
            self.assertIn('link', rental)

if __name__ == "__main__":
    unittest.main()