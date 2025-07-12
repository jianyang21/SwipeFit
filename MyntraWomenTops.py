import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from pymongo import MongoClient
from datetime import datetime
import time

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["Myntra"]
collection = db["womenstopwear"]

def scrape_and_store():
    print(f"\n--- Scraping at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---")

    # Start Chrome browser
    driver = webdriver.Chrome()

    # Open Myntra Tops page (replace with actual women's tops URL if needed)
    url = "https://www.myntra.com/women-tops"
    driver.get(url)
    time.sleep(5)  # Wait for JS content to load

    # Scrape product elements
    product_elements = driver.find_elements(By.CSS_SELECTOR, "h3.product-product")
    brand_elements = driver.find_elements(By.CSS_SELECTOR, "h4.product-brand")
    price_elements = driver.find_elements(By.CSS_SELECTOR, "span.product-discountedPrice")

    count = min(len(product_elements), len(brand_elements), len(price_elements))
    print(f"Found {count} products")

    for i in range(count):
        product_text = product_elements[i].text.strip()
        brand_text = brand_elements[i].text.strip()
        price_text = price_elements[i].text.strip()

        data = {
            "product": product_text,
            "brand": brand_text,
            "price": price_text,
            "timestamp": datetime.now()
        }

        collection.insert_one(data)
        print(f"🛍️ Stored: {brand_text} - {product_text} - {price_text}")

    driver.quit()

# Run scraper every 30 minutes
while True:
    scrape_and_store()
    print("Waiting 30 minutes before next scrape...\n")
    time.sleep(1800)  # 30 minutes

