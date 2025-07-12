from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from pymongo import MongoClient

# === MongoDB Setup ===
client = MongoClient("mongodb://localhost:27017/")
db = client["H&M"]
collection = db["CoordSets"]

# === Selenium Setup ===
options = Options()
# options.add_argument('--headless')  # Uncomment for headless mode
options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(service=Service(), options=options)

# Pages to scrape
base_url = "https://www2.hm.com/en_in/women/campaigns/co-ord-sets.html?page="
pages = [1, 2, 3]

all_products = []

for page in pages:
    url = base_url + str(page)
    driver.get(url)
    time.sleep(5)  # Let the page load
    
    product_names = driver.find_elements(By.CLASS_NAME, "da7fd3")
    prices = driver.find_elements(By.CLASS_NAME, "c2de6d")

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

