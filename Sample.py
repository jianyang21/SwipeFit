from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from pymongo import MongoClient

# === MongoDB Setup ===
client = MongoClient("mongodb://localhost:27017/")
db = client["H&M"]
collection = db["Shirt Dresses"]

driver = webdriver.Chrome()

# === Scraping Pages ===
base_url = "https://www2.hm.com/en_in/women/shop-by-product/dresses/shirt-dresses.html?page="
pages = range(1, 3)  # 1 to 29 inclusive

all_products = []

for page in pages:
    url = base_url + str(page)
    driver.get(url)
    time.sleep(5)  # Wait for the page to fully load

    # Use XPath to select based on exact class structure
    product_names = driver.find_elements(By.XPATH, '//h2[contains(@class,"da7fd3")]')
    prices = driver.find_elements(By.XPATH, '//span[contains(@class,"c2de6d")]')

    for name, price in zip(product_names, prices):
        item = {
            "Product Name": name.text.strip(),
            "Price": price.text.strip(),
            "Source URL": url
        }
        all_products.append(item)

driver.quit()

# === Insert into MongoDB ===
if all_products:
    collection.insert_many(all_products)
    print(f"Inserted {len(all_products)} products into MongoDB.")
else:
    print("No products found.")
