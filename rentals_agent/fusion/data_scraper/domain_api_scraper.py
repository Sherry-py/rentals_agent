import requests
from requests.adapters import HTTPAdapter, Retry

def fetch_domain_listings():
    url = "https://www.domain.com.au/phoenix/api/property-gallery"
    params = {
        "listingCategory": "Rent",
        "suburbIds": "rosebery-nsw-2018"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.domain.com.au/rent/rosebery-nsw-2018/",
        "X-Requested-With": "XMLHttpRequest",
        # "Cookie": "your_cookie_here",  # 如有需要，填写浏览器登录后的Cookie
    }

    session = requests.Session()
    retries = Retry(total=10, backoff_factor=2,
                    status_forcelist=[429, 500, 502, 503, 504])
    session.mount('https://', HTTPAdapter(max_retries=retries))

    try:
        print(f"请求: {url}  参数: {params}")
        response = session.get(url, params=params, headers=headers, timeout=60)
        response.raise_for_status()
        data = response.json()
        print(f"成功获取数据，共{len(data.get('properties', []))}条房源")
        return data
    except requests.exceptions.RequestException as e:
        print(f"请求异常: {e}")
        return None

if __name__ == "__main__":
    fetch_domain_listings()

