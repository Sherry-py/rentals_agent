from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_domain_rent():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    url = 'https://www.domain.com.au/rent/'
    driver.get(url)

    # 等待并点击 Cookie 弹窗的 Accept 按钮
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='privacy-accept']"))
        ).click()
        print("✅ 已点击接受 Cookie")
    except:
        print("⚠️ 未检测到 Cookie 弹窗或点击失败，继续执行")

    # 滚动加载页面
    for i in range(3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    # 等待房源加载
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='listing-card-link']"))
        )
    except:
        print("⚠️ 页面未加载出房源，请检查网络或页面结构")
        driver.quit()
        return []

    results = []

    listings = driver.find_elements(By.CSS_SELECTOR, "a[data-testid='listing-card-link']")
    print(f"抓取到 {len(listings)} 个房源卡片节点")

    for listing in listings:
        try:
            address = listing.find_element(By.CSS_SELECTOR, ".css-164r41r").text
            price = listing.find_element(By.CSS_SELECTOR, ".css-1h76c5j").text
            description = listing.find_element(By.CSS_SELECTOR, ".css-1rzse3v").text
            results.append({
                'address': address,
                'price': price,
                'description': description
            })
        except Exception as e:
            continue

    driver.quit()
    return results

if __name__ == '__main__':
    data = scrape_domain_rent()
    print(f"✅ 抓取完成，共获取 {len(data)} 条房源")
    for item in data:
        print(item)