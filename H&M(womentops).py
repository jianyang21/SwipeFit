from selenium import webdriver
from selenium.webdriver.common.by import By
from pymongo import MongoClient
from datetime import datetime
import time

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["H&M"]
collection = db["women_tops"]

def scrape_and_store():
    print(f"\n--- Scraping at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---")

    # Start Chrome normally (not headless)
    driver = webdriver.Chrome()

    # Open the page
    url = "https://www2.hm.com/en_in/women/shop-by-product/tops.html"
    driver.get(url)
    time.sleep(5)  # Wait for JavaScript to load

    # Scrape titles and prices
    titles = driver.find_elements(By.CSS_SELECTOR, "h2.f98e16.bd61d7.dbc452.c9f931")
    prices = driver.find_elements(By.CSS_SELECTOR, "span.e4ee18.cd6aee")

    count = min(len(titles), len(prices))
    print(f"Found {count} products")

    for i in range(count):
        title = titles[i].text.strip()
        price = prices[i].text.strip()

        data = {
            "title": title,
            "price": price,
            "timestamp": datetime.now()
        }

        collection.insert_one(data)  # Store in MongoDB

        print(f"Stored: {title} - {price}")

    driver.quit()

# Run the scraper every 30 minutes
while True:
    scrape_and_store()
    print("Waiting 30 minutes before next scrape...\n")
    time.sleep(1800)  # 1800 seconds = 30 minutes
