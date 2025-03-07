from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# for holding the resultant list
element_list = []

# Create Chrome options
chrome_options = Options()
# Add options as needed, e.g., headless mode
# chrome_options.add_argument("--headless")

for page in range(1, 3, 1):
    page_url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=" + str(page)

    # Initialize the Chrome driver with options
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Set a longer timeout value (in seconds)
    driver.set_page_load_timeout(300)  # Example: 30 seconds
    driver.get(page_url)

    title = driver.find_elements(By.CLASS_NAME, "title")
    price = driver.find_elements(By.CLASS_NAME, "price")
    description = driver.find_elements(By.CLASS_NAME, "description")
    rating = driver.find_elements(By.CLASS_NAME, "ratings")

    for i in range(len(title)):
        element_list.append([title[i].text, price[i].text, description[i].text, rating[i].text])

    # Closing the driver for each page
    driver.close()

print(element_list)