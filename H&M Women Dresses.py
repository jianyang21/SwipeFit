from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 🔁 Set your ChromeDriver path here
CHROMEDRIVER_PATH = "C:/WebDrivers/chromedriver.exe"  # Update this path

# 🧭 Set up Chrome browser (no headless)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)

base_url = "https://www2.hm.com/en_in/women/shop-by-product/dresses.html"

for page in range(1, 30):  # Pages 1 to 29
    print(f"\n--- Scraping Page {page} ---")
    url = f"{base_url}?page={page}"
    driver.get(url)
    time.sleep(2)  # Let page load

    # 🎯 Extract product names and prices using class selectors
    titles = driver.find_elements(By.CSS_SELECTOR, 'h2.da7fd3.fcf345.c2f341.bfa3ef')
    prices = driver.find_elements(By.CSS_SELECTOR, 'span.c2de6d.f1c5a4')

    for i in range(min(len(titles), len(prices))):
        name = titles[i].text.strip()
        price = prices[i].text.strip()
        print(f"{name} | {price}")

driver.quit()
