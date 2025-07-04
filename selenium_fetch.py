from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('/opt/homebrew/bin/chromedriver')  # 这个路径是brew安装后的软链路径，或者你也可以用完整路径
driver = webdriver.Chrome(service=service)

driver.get('https://www.realestate.com.au/')
print(driver.title)

driver.quit()