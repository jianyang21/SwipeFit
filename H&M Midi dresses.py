from selenium import webdriver
from selenium.webdriver.common.by import By
from pymongo import MongoClient
import time
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["H&M"]
collection = db["tops_Small_Size"]

def scrape_divided_dresses():
    driver = webdriver.Chrome()
    base_url = "https://www2.hm.com/en_in/women/shop-by-product/dresses/midi-dresses.html?page="
    pages = range(1, 8)
    for page in pages:
        url = base_url + str(page)
        driver.get(url)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Scraping Page {page}: {url}")
        time.sleep(5)
        titles = driver.find_elements(By.CSS_SELECTOR, 'h2.da7fd3.fcf345.c2f341.bfa3ef')
        prices = driver.find_elements(By.CSS_SELECTOR, 'span.c2de6d.f1c5a4')
        for i in range(min(len(titles), len(prices))):
            name = titles[i].text.strip()
            price =
 prices[i].text.strip()

