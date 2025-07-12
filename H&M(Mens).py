from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# options.add_argument('--headless')

# Set up driver (make sure chromedriver is in PATH or give full path)
driver = webdriver.Chrome()

url = 'https://www2.hm.com/en_in/men/shop-by-product/tshirts-tank-tops.html'
driver.get(url)

time.sleep(5)  # Let the page load

# Use correct selectors after inspecting the website
titles = driver.find_elements(By.CSS_SELECTOR, "h2.da7fd3 fcf345 c2f341 bfa3ef")
prices = driver.find_elements(By.CSS_SELECTOR, "span.c2de6d f1c5a4")

# Extract text from elements
for title, price in zip(titles, prices):
    print(f"{title.text.strip()} - {price.text.strip()}")

driver.quit()


